#include "batch_job.h"
#include "batch_job_internal.h"
#include "debug.h"
#include "process.h"
#include "stringtools.h"

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <fcntl.h>

#include <sys/stat.h>

struct batch_job_hadoop_job {
	char jobname[BATCH_JOB_LINE_MAX];
	int jobid;
};

struct batch_job_hadoop_job *batch_job_hadoop_job_create(char *jname)
{
	static int jobid = 1;
	struct batch_job_hadoop_job *job;
	job = malloc(sizeof(*job));
	if(!job)
		return NULL;
	snprintf(job->jobname, BATCH_JOB_LINE_MAX, "%s", jname);
	job->jobid = jobid++;
	return job;
}

static int setup_hadoop_wrapper(const char *wrapperfile, const char *cmd)
{
	FILE *file;

	file = fopen(wrapperfile, "w");
	if(!file)
		return -1;

	char *escaped_cmd = escape_shell_string(cmd);
	if (escaped_cmd == NULL) return -1;

	fprintf(file, "#!/bin/sh\n");
	fprintf(file, "cmd=%s\n", escaped_cmd);
	/* fprintf(file, "exec %s -- /bin/sh -c %s\n", getenv("HADOOP_PARROT_PATH"), escaped_cmd); */ /* random bash bug, look into later */
	fprintf(file, "exec %s -- /bin/sh <<EOF\n", getenv("HADOOP_PARROT_PATH"));
	fprintf(file, "$cmd\n");
	fprintf(file, "EOF\n");
	free(escaped_cmd);
	fclose(file);

	chmod(wrapperfile, 0755);

	return 0;
}

static char *get_hadoop_target_file(const char *input_files)
{
	static char result[BATCH_JOB_LINE_MAX];
	char *match_string = string_format("%s%%[^,]", getenv("HDFS_ROOT_DIR"));
	sscanf(input_files, match_string, result);
	free(match_string);
	return result;
}

batch_job_id_t batch_job_fork_hadoop(struct batch_queue *q, const char *cmd)
{
	int fd_pipe[2];
	int childpid;

	if(pipe(fd_pipe) < 0)
		return -1;

	fflush(NULL);
	debug(D_HDFS, "forking hadoop_status_wrapper\n");
	if((childpid = fork()) < 0) {
		return -1;
	} else if(!childpid) {
		// CHILD
		char line[BATCH_JOB_LINE_MAX];
		char outname[BATCH_JOB_LINE_MAX];
		FILE *cmd_pipe, *parent;
		struct flock lock; {
			lock.l_whence = SEEK_SET;
			lock.l_start = lock.l_len = 0;
			lock.l_pid = getpid();
		}

		close(fd_pipe[0]);
		parent = fdopen(fd_pipe[1], "w");
		setvbuf(parent, NULL, _IOLBF, 0);

		cmd_pipe = popen(cmd, "r");
		if(!cmd_pipe) {
			debug(D_DEBUG, "hadoop_status_wrapper: couldn't submit job: %s", strerror(errno));
			fclose(parent);
			_exit(-1);
		}

		outname[0] = 0;
		while(fgets(line, sizeof(line), cmd_pipe)) {
			debug(D_DEBUG, "batch_job_hadoop child [%d] output: %s", (int)getpid(), line);
			char jobname[BATCH_JOB_LINE_MAX];
			char error_string[BATCH_JOB_LINE_MAX];
			int mapdone, reddone;
			if(!strlen(outname) && sscanf(line, "%*s %*s INFO streaming.StreamJob: Running job: %s", jobname) == 1) {
				fprintf(parent, "%s\n", jobname);
				fclose(parent);
				sprintf(outname, "%s.status", jobname);
			} else if(strlen(outname) && sscanf(line, "%*s %*s INFO streaming.StreamJob:\tmap %d%%\treduce %d%%", &mapdone, &reddone) == 2) {
				FILE *output = NULL;
				sprintf(line, "%ld\tM%03d\tR%03d\n", (long int) time(0), mapdone, reddone);

				output = fopen(outname, "w");
				lock.l_type = F_WRLCK;
				fcntl(fileno(output), F_SETLKW, &lock);
				fprintf(output, "%s", line);
				lock.l_type = F_UNLCK;
				fcntl(fileno(output), F_SETLKW, &lock);
				fclose(output);

				debug(D_HDFS, "hadoop_status_wrapper: %s", line);

			} else if(strlen(outname) && sscanf(line, "%*s %*s INFO streaming.StreamJob: Job complete: %s", jobname) == 1) {
				FILE *output = NULL;

				output = fopen(outname, "w");
				lock.l_type = F_WRLCK;
				fcntl(fileno(output), F_SETLKW, &lock);
				fprintf(output, "%ld\tSUCCESS\t%s\n", (long int) time(0), jobname);
				lock.l_type = F_UNLCK;
				fcntl(fileno(output), F_SETLKW, &lock);
				fclose(output);

				debug(D_HDFS, "hadoop_status_wrapper: %ld\tSUCCESS\t%s", (long int) time(0), jobname);
				_exit(0);
			} else if(strlen(outname) && sscanf(line, "%*s %*s ERROR streaming.StreamJob: %s", error_string) == 1) {
				FILE *output = NULL;

				output = fopen(outname, "w");
				lock.l_type = F_WRLCK;
				fcntl(fileno(output), F_SETLKW, &lock);
				fprintf(output, "%ld\tFAILURE\t%s\n", (long int) time(0), error_string);
				lock.l_type = F_UNLCK;
				fcntl(fileno(output), F_SETLKW, &lock);
				fclose(output);

				debug(D_HDFS, "hadoop_status_wrapper: %ld\tFAILURE\t%s", (long int) time(0), error_string);
				_exit(0);
			}
		}
		_exit(0);

	} else {
		//PARENT
		char line[BATCH_JOB_LINE_MAX];
		char jobname[BATCH_JOB_LINE_MAX];
		FILE *child;
		struct batch_job_info *info;
		struct batch_job_hadoop_job *hadoop_job;

		close(fd_pipe[1]);
		child = fdopen(fd_pipe[0], "r");
		setvbuf(child, NULL, _IOLBF, 0);

		jobname[0] = 0;
		while(fgets(line, sizeof(line), child)) {
			if(sscanf(line, "%s", jobname) == 1) {
				break;
			}
		}

		fclose(child);
		if(!strlen(jobname))
			return -1;

		debug(D_HDFS, "jobname received: %s\n", jobname);
		hadoop_job = batch_job_hadoop_job_create(jobname);

		info = malloc(sizeof(*info));
		memset(info, 0, sizeof(*info));
		info->submitted = time(0);
		itable_insert(q->job_table, hadoop_job->jobid, info);
		itable_insert(q->hadoop_jobs, hadoop_job->jobid, hadoop_job);
		debug(D_DEBUG, "job %d (%s) submitted", hadoop_job->jobid, jobname);
		return (hadoop_job->jobid);
	}
}

batch_job_id_t batch_job_submit_simple_hadoop(struct batch_queue *q, const char *cmd, const char *extra_input_files, const char *extra_output_files)
{
	char *target_file;

	target_file = get_hadoop_target_file(extra_input_files);
	if(!target_file) {
		debug(D_DEBUG, "couldn't create new hadoop task: no input file specified\n");
		return -1;
	} else
		debug(D_HDFS, "input file %s specified\n", target_file);

	setup_hadoop_wrapper("./hadoop.wrapper", cmd);

	char *command = string_format("%s/bin/hadoop jar %s/mapred/contrib/streaming/hadoop-*-streaming.jar -D mapreduce.job.reduces=0 -input file:///dev/null -mapper ./hadoop.wrapper -file ./hadoop.wrapper -output '%s/job-%010d' 2>&1", getenv("HADOOP_HOME"), getenv("HADOOP_HOME"), getenv("HADOOP_USER_TMP"), (int)time(0));

	debug(D_HDFS, "%s", command);

	batch_job_id_t status = batch_job_fork_hadoop(q, command);
	free(command);
	return status;
}

batch_job_id_t batch_job_submit_hadoop(struct batch_queue *q, const char *cmd, const char *args, const char *infile, const char *outfile, const char *errfile, const char *extra_input_files, const char *extra_output_files)
{
	char *command = string_format("%s %s", cmd, args);
	if (infile) {
		char *new = string_format("%s <%s", command, infile);
		free(command);
		command = new;
	}
	if (outfile) {
		char *new = string_format("%s >%s", command, outfile);
		free(command);
		command = new;
	}
	if (errfile) {
		char *new = string_format("%s 2>%s", command, errfile);
		free(command);
		command = new;
	}

	batch_job_id_t status = batch_job_submit_simple_hadoop(q, command, extra_input_files, extra_output_files);
	free(command);
	return status;
}


batch_job_id_t batch_job_wait_hadoop(struct batch_queue * q, struct batch_job_info * info_out, time_t stoptime)
{
	struct batch_job_info *info;
	batch_job_id_t jobid;
	struct batch_job_hadoop_job *hadoop_job;

	while(1) {
		UINT64_T ujobid;
		itable_firstkey(q->job_table);
		while(itable_nextkey(q->job_table, &ujobid, (void **) &info)) {
			FILE *status;
			struct flock lock; {
				lock.l_whence = SEEK_SET;
				lock.l_start = lock.l_len = 0;
				lock.l_pid = getpid();
			}
			jobid = ujobid;
			hadoop_job = (struct batch_job_hadoop_job *) itable_lookup(q->hadoop_jobs, jobid);

			char *statusfile = string_format("%s.status", hadoop_job->jobname);
			status = fopen(statusfile, "r");

			if(status) {
				int map, red;
				long logtime;
				char result[BATCH_JOB_LINE_MAX];
				char message[BATCH_JOB_LINE_MAX];
				char line[BATCH_JOB_LINE_MAX] = "";

				lock.l_type = F_RDLCK;
				fcntl(fileno(status), F_SETLKW, &lock);
				fgets(line, sizeof(line), status);
				lock.l_type = F_UNLCK;
				fcntl(fileno(status), F_SETLKW, &lock);
				fclose(status);

				result[0] = message[0] = 0;
				sscanf(line, "%ld\t%s\t%s", &logtime, result, message);

				if(!strncmp(result, "SUCCESS", 7)) {
					debug(D_DEBUG, "job %d success", jobid);
					info->finished = logtime;
					info->exited_normally = 1;
				} else if(!strncmp(result, "FAILURE", 7)) {
					debug(D_DEBUG, "hadoop execution failed: %s", message);
					info->finished = logtime;
					info->exited_normally = 0;
				}

				if(info->finished != 0) {
					info = itable_remove(q->job_table, jobid);
					*info_out = *info;
					unlink(statusfile);
					free(info);
					free(statusfile);
					return jobid;
				}

				if(sscanf(line, "%ld\tM%d\tR%d", &logtime, &map, &red) == 3) {
					if(map && !info->started)
						info->started = logtime;
					if(red == 100)
						debug(D_DEBUG, "job %d end execution", jobid);
				}

			}
			free(statusfile);
		}

		if(itable_size(q->job_table) <= 0)
			return 0;

		if(stoptime != 0 && time(0) >= stoptime)
			return -1;

		if(process_pending())
			return -1;

		sleep(1);
	}

	return -1;
}


int batch_job_remove_hadoop(struct batch_queue *q, batch_job_id_t jobid)
{
	return 0;
}

