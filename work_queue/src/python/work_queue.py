# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_work_queue', [dirname(__file__)])
        except ImportError:
            import _work_queue
            return _work_queue
        if fp is not None:
            try:
                _mod = imp.load_module('_work_queue', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _work_queue = swig_import_helper()
    del swig_import_helper
else:
    import _work_queue
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


D_SYSCALL = _work_queue.D_SYSCALL
D_CHANNEL = _work_queue.D_CHANNEL
D_PROCESS = _work_queue.D_PROCESS
D_NOTICE = _work_queue.D_NOTICE
D_RESOLVE = _work_queue.D_RESOLVE
D_LIBCALL = _work_queue.D_LIBCALL
D_LOCAL = _work_queue.D_LOCAL
D_DNS = _work_queue.D_DNS
D_TCP = _work_queue.D_TCP
D_AUTH = _work_queue.D_AUTH
D_IRODS = _work_queue.D_IRODS
D_CVMFS = _work_queue.D_CVMFS
D_HTTP = _work_queue.D_HTTP
D_FTP = _work_queue.D_FTP
D_NEST = _work_queue.D_NEST
D_GROW = _work_queue.D_GROW
D_CHIRP = _work_queue.D_CHIRP
D_DCAP = _work_queue.D_DCAP
D_RFIO = _work_queue.D_RFIO
D_GLITE = _work_queue.D_GLITE
D_MULTI = _work_queue.D_MULTI
D_PSTREE = _work_queue.D_PSTREE
D_ALLOC = _work_queue.D_ALLOC
D_LFC = _work_queue.D_LFC
D_GFAL = _work_queue.D_GFAL
D_SUMMARY = _work_queue.D_SUMMARY
D_DEBUG = _work_queue.D_DEBUG
D_LOGIN = _work_queue.D_LOGIN
D_CACHE = _work_queue.D_CACHE
D_POLL = _work_queue.D_POLL
D_HDFS = _work_queue.D_HDFS
D_WQ = _work_queue.D_WQ
D_BXGRID = _work_queue.D_BXGRID
D_USER = _work_queue.D_USER
D_XROOTD = _work_queue.D_XROOTD
D_MPI = _work_queue.D_MPI
D_REMOTE = _work_queue.D_REMOTE
D_ALL = _work_queue.D_ALL

def cctools_debug(*args):
  return _work_queue.cctools_debug(*args)
cctools_debug = _work_queue.cctools_debug

def cctools_fatal(*args):
  return _work_queue.cctools_fatal(*args)
cctools_fatal = _work_queue.cctools_fatal

def cctools_debug_config(*args):
  return _work_queue.cctools_debug_config(*args)
cctools_debug_config = _work_queue.cctools_debug_config

def cctools_debug_config_file(*args):
  return _work_queue.cctools_debug_config_file(*args)
cctools_debug_config_file = _work_queue.cctools_debug_config_file

def cctools_debug_config_file_size(*args):
  return _work_queue.cctools_debug_config_file_size(*args)
cctools_debug_config_file_size = _work_queue.cctools_debug_config_file_size

def cctools_debug_config_fatal(*args):
  return _work_queue.cctools_debug_config_fatal(*args)
cctools_debug_config_fatal = _work_queue.cctools_debug_config_fatal

def cctools_debug_config_getpid(*args):
  return _work_queue.cctools_debug_config_getpid(*args)
cctools_debug_config_getpid = _work_queue.cctools_debug_config_getpid

def cctools_debug_flags_set(*args):
  return _work_queue.cctools_debug_flags_set(*args)
cctools_debug_flags_set = _work_queue.cctools_debug_flags_set

def cctools_debug_flags_print(*args):
  return _work_queue.cctools_debug_flags_print(*args)
cctools_debug_flags_print = _work_queue.cctools_debug_flags_print

def cctools_debug_flags_clear():
  return _work_queue.cctools_debug_flags_clear()
cctools_debug_flags_clear = _work_queue.cctools_debug_flags_clear

def cctools_debug_set_flag_name(*args):
  return _work_queue.cctools_debug_set_flag_name(*args)
cctools_debug_set_flag_name = _work_queue.cctools_debug_set_flag_name

def cctools_debug_flags_restore(*args):
  return _work_queue.cctools_debug_flags_restore(*args)
cctools_debug_flags_restore = _work_queue.cctools_debug_flags_restore
INT8_FORMAT = _work_queue.INT8_FORMAT
INT16_FORMAT = _work_queue.INT16_FORMAT
INT32_FORMAT = _work_queue.INT32_FORMAT
INT64_FORMAT = _work_queue.INT64_FORMAT
PTR_FORMAT = _work_queue.PTR_FORMAT
UINT8_FORMAT = _work_queue.UINT8_FORMAT
UINT16_FORMAT = _work_queue.UINT16_FORMAT
UINT32_FORMAT = _work_queue.UINT32_FORMAT
UINT64_FORMAT = _work_queue.UINT64_FORMAT
UPTR_FORMAT = _work_queue.UPTR_FORMAT
TIMESTAMP_FORMAT = _work_queue.TIMESTAMP_FORMAT

def timestamp_get():
  return _work_queue.timestamp_get()
timestamp_get = _work_queue.timestamp_get

def timestamp_sleep(*args):
  return _work_queue.timestamp_sleep(*args)
timestamp_sleep = _work_queue.timestamp_sleep

def timestamp_file(*args):
  return _work_queue.timestamp_file(*args)
timestamp_file = _work_queue.timestamp_file
WORK_QUEUE_DEFAULT_PORT = _work_queue.WORK_QUEUE_DEFAULT_PORT
WORK_QUEUE_RANDOM_PORT = _work_queue.WORK_QUEUE_RANDOM_PORT
WORK_QUEUE_LINE_MAX = _work_queue.WORK_QUEUE_LINE_MAX
WORK_QUEUE_WAITFORTASK = _work_queue.WORK_QUEUE_WAITFORTASK
WORK_QUEUE_RETURN_STATUS_UNSET = _work_queue.WORK_QUEUE_RETURN_STATUS_UNSET
WORK_QUEUE_RESULT_UNSET = _work_queue.WORK_QUEUE_RESULT_UNSET
WORK_QUEUE_RESULT_INPUT_FAIL = _work_queue.WORK_QUEUE_RESULT_INPUT_FAIL
WORK_QUEUE_RESULT_INPUT_MISSING = _work_queue.WORK_QUEUE_RESULT_INPUT_MISSING
WORK_QUEUE_RESULT_FUNCTION_FAIL = _work_queue.WORK_QUEUE_RESULT_FUNCTION_FAIL
WORK_QUEUE_RESULT_OUTPUT_FAIL = _work_queue.WORK_QUEUE_RESULT_OUTPUT_FAIL
WORK_QUEUE_RESULT_OUTPUT_MISSING = _work_queue.WORK_QUEUE_RESULT_OUTPUT_MISSING
WORK_QUEUE_RESULT_LINK_FAIL = _work_queue.WORK_QUEUE_RESULT_LINK_FAIL
WORK_QUEUE_SCHEDULE_UNSET = _work_queue.WORK_QUEUE_SCHEDULE_UNSET
WORK_QUEUE_SCHEDULE_FCFS = _work_queue.WORK_QUEUE_SCHEDULE_FCFS
WORK_QUEUE_SCHEDULE_FILES = _work_queue.WORK_QUEUE_SCHEDULE_FILES
WORK_QUEUE_SCHEDULE_TIME = _work_queue.WORK_QUEUE_SCHEDULE_TIME
WORK_QUEUE_SCHEDULE_DEFAULT = _work_queue.WORK_QUEUE_SCHEDULE_DEFAULT
WORK_QUEUE_SCHEDULE_PREFERRED_HOSTS = _work_queue.WORK_QUEUE_SCHEDULE_PREFERRED_HOSTS
WORK_QUEUE_SCHEDULE_RAND = _work_queue.WORK_QUEUE_SCHEDULE_RAND
WORK_QUEUE_SCHEDULE_MAX = _work_queue.WORK_QUEUE_SCHEDULE_MAX
WORK_QUEUE_INPUT = _work_queue.WORK_QUEUE_INPUT
WORK_QUEUE_OUTPUT = _work_queue.WORK_QUEUE_OUTPUT
WORK_QUEUE_NOCACHE = _work_queue.WORK_QUEUE_NOCACHE
WORK_QUEUE_CACHE = _work_queue.WORK_QUEUE_CACHE
WORK_QUEUE_SYMLINK = _work_queue.WORK_QUEUE_SYMLINK
WORK_QUEUE_PREEXIST = _work_queue.WORK_QUEUE_PREEXIST
WORK_QUEUE_THIRDGET = _work_queue.WORK_QUEUE_THIRDGET
WORK_QUEUE_THIRDPUT = _work_queue.WORK_QUEUE_THIRDPUT
WORK_QUEUE_MASTER_MODE_STANDALONE = _work_queue.WORK_QUEUE_MASTER_MODE_STANDALONE
WORK_QUEUE_MASTER_MODE_CATALOG = _work_queue.WORK_QUEUE_MASTER_MODE_CATALOG
WORK_QUEUE_NAME_MAX = _work_queue.WORK_QUEUE_NAME_MAX
WORK_QUEUE_MASTER_PRIORITY_MAX = _work_queue.WORK_QUEUE_MASTER_PRIORITY_MAX
WORK_QUEUE_MASTER_PRIORITY_DEFAULT = _work_queue.WORK_QUEUE_MASTER_PRIORITY_DEFAULT
WORK_QUEUE_WORKER_MODE_SHARED = _work_queue.WORK_QUEUE_WORKER_MODE_SHARED
WORK_QUEUE_WORKER_MODE_EXCLUSIVE = _work_queue.WORK_QUEUE_WORKER_MODE_EXCLUSIVE
WORK_QUEUE_CATALOG_LINE_MAX = _work_queue.WORK_QUEUE_CATALOG_LINE_MAX
WORK_QUEUE_CATALOG_UPDATE_INTERVAL = _work_queue.WORK_QUEUE_CATALOG_UPDATE_INTERVAL
WORK_QUEUE_CATALOG_LIFETIME = _work_queue.WORK_QUEUE_CATALOG_LIFETIME
WORK_QUEUE_FS_CMD = _work_queue.WORK_QUEUE_FS_CMD
WORK_QUEUE_FS_PATH = _work_queue.WORK_QUEUE_FS_PATH
WORK_QUEUE_FS_SYMLINK = _work_queue.WORK_QUEUE_FS_SYMLINK
class work_queue_task(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, work_queue_task, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, work_queue_task, name)
    __repr__ = _swig_repr
    __swig_setmethods__["tag"] = _work_queue.work_queue_task_tag_set
    __swig_getmethods__["tag"] = _work_queue.work_queue_task_tag_get
    if _newclass:tag = _swig_property(_work_queue.work_queue_task_tag_get, _work_queue.work_queue_task_tag_set)
    __swig_setmethods__["command_line"] = _work_queue.work_queue_task_command_line_set
    __swig_getmethods__["command_line"] = _work_queue.work_queue_task_command_line_get
    if _newclass:command_line = _swig_property(_work_queue.work_queue_task_command_line_get, _work_queue.work_queue_task_command_line_set)
    __swig_setmethods__["worker_selection_algorithm"] = _work_queue.work_queue_task_worker_selection_algorithm_set
    __swig_getmethods__["worker_selection_algorithm"] = _work_queue.work_queue_task_worker_selection_algorithm_get
    if _newclass:worker_selection_algorithm = _swig_property(_work_queue.work_queue_task_worker_selection_algorithm_get, _work_queue.work_queue_task_worker_selection_algorithm_set)
    __swig_setmethods__["output"] = _work_queue.work_queue_task_output_set
    __swig_getmethods__["output"] = _work_queue.work_queue_task_output_get
    if _newclass:output = _swig_property(_work_queue.work_queue_task_output_get, _work_queue.work_queue_task_output_set)
    __swig_setmethods__["input_files"] = _work_queue.work_queue_task_input_files_set
    __swig_getmethods__["input_files"] = _work_queue.work_queue_task_input_files_get
    if _newclass:input_files = _swig_property(_work_queue.work_queue_task_input_files_get, _work_queue.work_queue_task_input_files_set)
    __swig_setmethods__["output_files"] = _work_queue.work_queue_task_output_files_set
    __swig_getmethods__["output_files"] = _work_queue.work_queue_task_output_files_get
    if _newclass:output_files = _swig_property(_work_queue.work_queue_task_output_files_get, _work_queue.work_queue_task_output_files_set)
    __swig_setmethods__["preferred_host"] = _work_queue.work_queue_task_preferred_host_set
    __swig_getmethods__["preferred_host"] = _work_queue.work_queue_task_preferred_host_get
    if _newclass:preferred_host = _swig_property(_work_queue.work_queue_task_preferred_host_get, _work_queue.work_queue_task_preferred_host_set)
    __swig_setmethods__["taskid"] = _work_queue.work_queue_task_taskid_set
    __swig_getmethods__["taskid"] = _work_queue.work_queue_task_taskid_get
    if _newclass:taskid = _swig_property(_work_queue.work_queue_task_taskid_get, _work_queue.work_queue_task_taskid_set)
    __swig_setmethods__["status"] = _work_queue.work_queue_task_status_set
    __swig_getmethods__["status"] = _work_queue.work_queue_task_status_get
    if _newclass:status = _swig_property(_work_queue.work_queue_task_status_get, _work_queue.work_queue_task_status_set)
    __swig_setmethods__["return_status"] = _work_queue.work_queue_task_return_status_set
    __swig_getmethods__["return_status"] = _work_queue.work_queue_task_return_status_get
    if _newclass:return_status = _swig_property(_work_queue.work_queue_task_return_status_get, _work_queue.work_queue_task_return_status_set)
    __swig_setmethods__["result"] = _work_queue.work_queue_task_result_set
    __swig_getmethods__["result"] = _work_queue.work_queue_task_result_get
    if _newclass:result = _swig_property(_work_queue.work_queue_task_result_get, _work_queue.work_queue_task_result_set)
    __swig_setmethods__["host"] = _work_queue.work_queue_task_host_set
    __swig_getmethods__["host"] = _work_queue.work_queue_task_host_get
    if _newclass:host = _swig_property(_work_queue.work_queue_task_host_get, _work_queue.work_queue_task_host_set)
    __swig_setmethods__["submit_time"] = _work_queue.work_queue_task_submit_time_set
    __swig_getmethods__["submit_time"] = _work_queue.work_queue_task_submit_time_get
    if _newclass:submit_time = _swig_property(_work_queue.work_queue_task_submit_time_get, _work_queue.work_queue_task_submit_time_set)
    __swig_setmethods__["transfer_start_time"] = _work_queue.work_queue_task_transfer_start_time_set
    __swig_getmethods__["transfer_start_time"] = _work_queue.work_queue_task_transfer_start_time_get
    if _newclass:transfer_start_time = _swig_property(_work_queue.work_queue_task_transfer_start_time_get, _work_queue.work_queue_task_transfer_start_time_set)
    __swig_setmethods__["start_time"] = _work_queue.work_queue_task_start_time_set
    __swig_getmethods__["start_time"] = _work_queue.work_queue_task_start_time_get
    if _newclass:start_time = _swig_property(_work_queue.work_queue_task_start_time_get, _work_queue.work_queue_task_start_time_set)
    __swig_setmethods__["finish_time"] = _work_queue.work_queue_task_finish_time_set
    __swig_getmethods__["finish_time"] = _work_queue.work_queue_task_finish_time_get
    if _newclass:finish_time = _swig_property(_work_queue.work_queue_task_finish_time_get, _work_queue.work_queue_task_finish_time_set)
    __swig_setmethods__["computation_time"] = _work_queue.work_queue_task_computation_time_set
    __swig_getmethods__["computation_time"] = _work_queue.work_queue_task_computation_time_get
    if _newclass:computation_time = _swig_property(_work_queue.work_queue_task_computation_time_get, _work_queue.work_queue_task_computation_time_set)
    __swig_setmethods__["total_bytes_transferred"] = _work_queue.work_queue_task_total_bytes_transferred_set
    __swig_getmethods__["total_bytes_transferred"] = _work_queue.work_queue_task_total_bytes_transferred_get
    if _newclass:total_bytes_transferred = _swig_property(_work_queue.work_queue_task_total_bytes_transferred_get, _work_queue.work_queue_task_total_bytes_transferred_set)
    __swig_setmethods__["total_transfer_time"] = _work_queue.work_queue_task_total_transfer_time_set
    __swig_getmethods__["total_transfer_time"] = _work_queue.work_queue_task_total_transfer_time_get
    if _newclass:total_transfer_time = _swig_property(_work_queue.work_queue_task_total_transfer_time_get, _work_queue.work_queue_task_total_transfer_time_set)
    def __init__(self): 
        this = _work_queue.new_work_queue_task()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _work_queue.delete_work_queue_task
    __del__ = lambda self : None;
work_queue_task_swigregister = _work_queue.work_queue_task_swigregister
work_queue_task_swigregister(work_queue_task)
cvar = _work_queue.cvar

class work_queue_stats(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, work_queue_stats, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, work_queue_stats, name)
    __repr__ = _swig_repr
    __swig_setmethods__["workers_init"] = _work_queue.work_queue_stats_workers_init_set
    __swig_getmethods__["workers_init"] = _work_queue.work_queue_stats_workers_init_get
    if _newclass:workers_init = _swig_property(_work_queue.work_queue_stats_workers_init_get, _work_queue.work_queue_stats_workers_init_set)
    __swig_setmethods__["workers_ready"] = _work_queue.work_queue_stats_workers_ready_set
    __swig_getmethods__["workers_ready"] = _work_queue.work_queue_stats_workers_ready_get
    if _newclass:workers_ready = _swig_property(_work_queue.work_queue_stats_workers_ready_get, _work_queue.work_queue_stats_workers_ready_set)
    __swig_setmethods__["workers_busy"] = _work_queue.work_queue_stats_workers_busy_set
    __swig_getmethods__["workers_busy"] = _work_queue.work_queue_stats_workers_busy_get
    if _newclass:workers_busy = _swig_property(_work_queue.work_queue_stats_workers_busy_get, _work_queue.work_queue_stats_workers_busy_set)
    __swig_setmethods__["tasks_running"] = _work_queue.work_queue_stats_tasks_running_set
    __swig_getmethods__["tasks_running"] = _work_queue.work_queue_stats_tasks_running_get
    if _newclass:tasks_running = _swig_property(_work_queue.work_queue_stats_tasks_running_get, _work_queue.work_queue_stats_tasks_running_set)
    __swig_setmethods__["tasks_waiting"] = _work_queue.work_queue_stats_tasks_waiting_set
    __swig_getmethods__["tasks_waiting"] = _work_queue.work_queue_stats_tasks_waiting_get
    if _newclass:tasks_waiting = _swig_property(_work_queue.work_queue_stats_tasks_waiting_get, _work_queue.work_queue_stats_tasks_waiting_set)
    __swig_setmethods__["tasks_complete"] = _work_queue.work_queue_stats_tasks_complete_set
    __swig_getmethods__["tasks_complete"] = _work_queue.work_queue_stats_tasks_complete_get
    if _newclass:tasks_complete = _swig_property(_work_queue.work_queue_stats_tasks_complete_get, _work_queue.work_queue_stats_tasks_complete_set)
    __swig_setmethods__["total_tasks_dispatched"] = _work_queue.work_queue_stats_total_tasks_dispatched_set
    __swig_getmethods__["total_tasks_dispatched"] = _work_queue.work_queue_stats_total_tasks_dispatched_get
    if _newclass:total_tasks_dispatched = _swig_property(_work_queue.work_queue_stats_total_tasks_dispatched_get, _work_queue.work_queue_stats_total_tasks_dispatched_set)
    __swig_setmethods__["total_tasks_complete"] = _work_queue.work_queue_stats_total_tasks_complete_set
    __swig_getmethods__["total_tasks_complete"] = _work_queue.work_queue_stats_total_tasks_complete_get
    if _newclass:total_tasks_complete = _swig_property(_work_queue.work_queue_stats_total_tasks_complete_get, _work_queue.work_queue_stats_total_tasks_complete_set)
    __swig_setmethods__["total_workers_joined"] = _work_queue.work_queue_stats_total_workers_joined_set
    __swig_getmethods__["total_workers_joined"] = _work_queue.work_queue_stats_total_workers_joined_get
    if _newclass:total_workers_joined = _swig_property(_work_queue.work_queue_stats_total_workers_joined_get, _work_queue.work_queue_stats_total_workers_joined_set)
    __swig_setmethods__["total_workers_removed"] = _work_queue.work_queue_stats_total_workers_removed_set
    __swig_getmethods__["total_workers_removed"] = _work_queue.work_queue_stats_total_workers_removed_get
    if _newclass:total_workers_removed = _swig_property(_work_queue.work_queue_stats_total_workers_removed_get, _work_queue.work_queue_stats_total_workers_removed_set)
    __swig_setmethods__["total_bytes_sent"] = _work_queue.work_queue_stats_total_bytes_sent_set
    __swig_getmethods__["total_bytes_sent"] = _work_queue.work_queue_stats_total_bytes_sent_get
    if _newclass:total_bytes_sent = _swig_property(_work_queue.work_queue_stats_total_bytes_sent_get, _work_queue.work_queue_stats_total_bytes_sent_set)
    __swig_setmethods__["total_bytes_received"] = _work_queue.work_queue_stats_total_bytes_received_set
    __swig_getmethods__["total_bytes_received"] = _work_queue.work_queue_stats_total_bytes_received_get
    if _newclass:total_bytes_received = _swig_property(_work_queue.work_queue_stats_total_bytes_received_get, _work_queue.work_queue_stats_total_bytes_received_set)
    __swig_setmethods__["total_send_time"] = _work_queue.work_queue_stats_total_send_time_set
    __swig_getmethods__["total_send_time"] = _work_queue.work_queue_stats_total_send_time_get
    if _newclass:total_send_time = _swig_property(_work_queue.work_queue_stats_total_send_time_get, _work_queue.work_queue_stats_total_send_time_set)
    __swig_setmethods__["total_receive_time"] = _work_queue.work_queue_stats_total_receive_time_set
    __swig_getmethods__["total_receive_time"] = _work_queue.work_queue_stats_total_receive_time_get
    if _newclass:total_receive_time = _swig_property(_work_queue.work_queue_stats_total_receive_time_get, _work_queue.work_queue_stats_total_receive_time_set)
    def __init__(self): 
        this = _work_queue.new_work_queue_stats()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _work_queue.delete_work_queue_stats
    __del__ = lambda self : None;
work_queue_stats_swigregister = _work_queue.work_queue_stats_swigregister
work_queue_stats_swigregister(work_queue_stats)


def work_queue_task_create(*args):
  return _work_queue.work_queue_task_create(*args)
work_queue_task_create = _work_queue.work_queue_task_create

def work_queue_task_specify_file(*args):
  return _work_queue.work_queue_task_specify_file(*args)
work_queue_task_specify_file = _work_queue.work_queue_task_specify_file

def work_queue_task_specify_buffer(*args):
  return _work_queue.work_queue_task_specify_buffer(*args)
work_queue_task_specify_buffer = _work_queue.work_queue_task_specify_buffer

def work_queue_task_specify_file_command(*args):
  return _work_queue.work_queue_task_specify_file_command(*args)
work_queue_task_specify_file_command = _work_queue.work_queue_task_specify_file_command

def work_queue_task_specify_tag(*args):
  return _work_queue.work_queue_task_specify_tag(*args)
work_queue_task_specify_tag = _work_queue.work_queue_task_specify_tag

def work_queue_task_specify_algorithm(*args):
  return _work_queue.work_queue_task_specify_algorithm(*args)
work_queue_task_specify_algorithm = _work_queue.work_queue_task_specify_algorithm

def work_queue_task_specify_preferred_host(*args):
  return _work_queue.work_queue_task_specify_preferred_host(*args)
work_queue_task_specify_preferred_host = _work_queue.work_queue_task_specify_preferred_host

def work_queue_task_delete(*args):
  return _work_queue.work_queue_task_delete(*args)
work_queue_task_delete = _work_queue.work_queue_task_delete

def work_queue_create(*args):
  return _work_queue.work_queue_create(*args)
work_queue_create = _work_queue.work_queue_create

def work_queue_submit(*args):
  return _work_queue.work_queue_submit(*args)
work_queue_submit = _work_queue.work_queue_submit

def work_queue_wait(*args):
  return _work_queue.work_queue_wait(*args)
work_queue_wait = _work_queue.work_queue_wait

def work_queue_hungry(*args):
  return _work_queue.work_queue_hungry(*args)
work_queue_hungry = _work_queue.work_queue_hungry

def work_queue_empty(*args):
  return _work_queue.work_queue_empty(*args)
work_queue_empty = _work_queue.work_queue_empty

def work_queue_port(*args):
  return _work_queue.work_queue_port(*args)
work_queue_port = _work_queue.work_queue_port

def work_queue_name(*args):
  return _work_queue.work_queue_name(*args)
work_queue_name = _work_queue.work_queue_name

def work_queue_get_stats(*args):
  return _work_queue.work_queue_get_stats(*args)
work_queue_get_stats = _work_queue.work_queue_get_stats

def work_queue_activate_fast_abort(*args):
  return _work_queue.work_queue_activate_fast_abort(*args)
work_queue_activate_fast_abort = _work_queue.work_queue_activate_fast_abort

def work_queue_specify_algorithm(*args):
  return _work_queue.work_queue_specify_algorithm(*args)
work_queue_specify_algorithm = _work_queue.work_queue_specify_algorithm

def work_queue_specify_name(*args):
  return _work_queue.work_queue_specify_name(*args)
work_queue_specify_name = _work_queue.work_queue_specify_name

def work_queue_specify_priority(*args):
  return _work_queue.work_queue_specify_priority(*args)
work_queue_specify_priority = _work_queue.work_queue_specify_priority

def work_queue_specify_master_mode(*args):
  return _work_queue.work_queue_specify_master_mode(*args)
work_queue_specify_master_mode = _work_queue.work_queue_specify_master_mode

def work_queue_specify_worker_mode(*args):
  return _work_queue.work_queue_specify_worker_mode(*args)
work_queue_specify_worker_mode = _work_queue.work_queue_specify_worker_mode

def work_queue_shut_down_workers(*args):
  return _work_queue.work_queue_shut_down_workers(*args)
work_queue_shut_down_workers = _work_queue.work_queue_shut_down_workers

def work_queue_delete(*args):
  return _work_queue.work_queue_delete(*args)
work_queue_delete = _work_queue.work_queue_delete

def work_queue_task_specify_input_buf(*args):
  return _work_queue.work_queue_task_specify_input_buf(*args)
work_queue_task_specify_input_buf = _work_queue.work_queue_task_specify_input_buf

def work_queue_task_specify_input_file(*args):
  return _work_queue.work_queue_task_specify_input_file(*args)
work_queue_task_specify_input_file = _work_queue.work_queue_task_specify_input_file

def work_queue_task_specify_input_file_do_not_cache(*args):
  return _work_queue.work_queue_task_specify_input_file_do_not_cache(*args)
work_queue_task_specify_input_file_do_not_cache = _work_queue.work_queue_task_specify_input_file_do_not_cache

def work_queue_task_specify_output_file(*args):
  return _work_queue.work_queue_task_specify_output_file(*args)
work_queue_task_specify_output_file = _work_queue.work_queue_task_specify_output_file

def work_queue_task_specify_output_file_do_not_cache(*args):
  return _work_queue.work_queue_task_specify_output_file_do_not_cache(*args)
work_queue_task_specify_output_file_do_not_cache = _work_queue.work_queue_task_specify_output_file_do_not_cache


## @package WorkQueuePython
#
# Python Work Queue bindings.
#
# The objects and methods provided by this package should correspond to the
# native C API in @ref work_queue.h.
#
# The new SWIG-based bindings provides two levels of access to the Work Queue
# library.  The first version provides a 1-to-1 function correspondance to the
# C API.
#
# The second version provides a more Pythonic or higher-level interface that
# revolves around the following objects:
#
# - @ref work_queue::WorkQueue
# - @ref work_queue::Task

import os

def set_debug_flag(*flags):
    for flag in flags:
    	cctools_debug_flags_set(flag)

cctools_debug_config('work_queue_python')

##
# Python Task object
#
# This class is used to create a task specification.
#
# Example:
# @code
# # Create and specify Task
# task = Task('date > current.date')
# task.specify_algorithm(WORK_QUEUE_SCHEDULE_FCFS)
# task.specify_input_file('/usr/bin/date', 'date')
# task.specify_tag('my date task')
#
# # Create Work Queue and submit Task
# work_queue = WorkQueue()
# work_queue.submit(task)
# @endcode
class Task(_object):

    ##
    # Create a new task specification.
    #
    # @param self	Reference to the current task object.
    # @param command	The shell command line to be exected by the task.
    def __init__(self, command):
    	self._task = work_queue_task_create(command)

    def __del__(self):
    	work_queue_task_delete(self._task)

    @staticmethod
    def _determine_file_flags(flags, cache):
	if flags is None:
	    flags = WORK_QUEUE_CACHE

	if cache:
	    flags |= WORK_QUEUE_CACHE
	else:
	    flags &= ~WORK_QUEUE_CACHE

	return flags

    @property
    def algorithm(self):
    	return self._task.worker_selection_algorithm

    @property
    def command(self):
    	return self._task.command_line

    @property
    def tag(self):
    	return self._task.tag

    @property
    def output(self):
    	return self._task.output

    @property
    def id(self):
    	return self._task.taskid

    @property
    def preferred_host(self):
    	return self._task.preferred_host

    @property
    def status(self):
    	return self._task.status

    @property
    def return_status(self):
    	return self._task.return_status

    @property
    def result(self):
    	return self._task.result

    @property
    def host(self):
    	return self._task.host

    @property
    def submit_time(self):
    	return self._task.submit_time

    @property
    def start_time(self):
    	return self._task.start_time

    @property
    def finish_time(self):
    	return self._task.finish_time

    @property
    def transfer_start_time(self):
    	return self._task.transfer_start_time

    @property
    def computation_time(self):
    	return self._task.computation_time

    @property
    def total_bytes_transferred(self):
    	return self._task.total_bytes_transferred

    @property
    def total_transfer_time(self):
    	return self._task.total_transfer_time

    ##
    # Set the worker selection algorithm for task.
    #
    # @param self	Reference to the current task object.
    # @param algorithm	One of the following algorithms to use in assigning a
    #			task to a worker:
    #			- @ref WORK_QUEUE_SCHEDULE_FCFS
    #			- @ref WORK_QUEUE_SCHEDULE_FILES
    #			- @ref WORK_QUEUE_SCHEDULE_TIME
    #			- @ref WORK_QUEUE_SCHEDULE_DEFAULT
    #			- @ref WORK_QUEUE_SCHEDULE_PREFERRED_HOSTS
    #			- @ref WORK_QUEUE_SCHEDULE_RAND
    def specify_algorithm(self, algorithm):
    	return work_queue_task_specify_algorithm(self._task, algorithm)

    ##
    # Attach a user defined logical name to the task.
    #
    # @param self	Reference to the current task object.
    # @param tag	The tag to attach to task.
    def specify_tag(self, tag):
    	return work_queue_task_specify_tag(self._task, tag)
   
    ##
    # Indicate that the task would be optimally run on a given host.
    #
    # @param self	Reference to the current task object.
    # @param hostname	The hostname to which this task would optimally be sent.
    def specify_preferred_host(self, hostname):
    	return work_queue_task_specify_preferred_host(self._task, hostname)

    ##
    # Add a file to the task.
    #
    # @param self	    Reference to the current task object.
    # @param local_name	    The name of the file on local disk or shared filesystem.
    # @param remote_name    The name of the file at the execution site.
    # @param type	    Must be one of the following values: @ref WORK_QUEUE_INPUT or @ref WORK_QUEUE_OUTPUT
    # @param flags	    May be zero to indicate no special handling, or any of the following or'd together:
    #			    - @ref WORK_QUEUE_NOCACHE
    #			    - @ref WORK_QUEUE_CACHE
    #			    - @ref WORK_QUEUE_SYMLINK
    #			    - @ref WORK_QUEUE_THIRDGET
    #			    - @ref WORK_QUEUE_THIRDPUT
    # @param cache	    Legacy parameter for setting file caching attribute.  By default this is enabled.
    #
    # Example:
    # @code
    # # The following are equivalent
    # >>> task.specify_file("/etc/hosts", type=WORK_QUEUE_INPUT, flags=WORK_QUEUE_NOCACHE)
    # >>> task.specify_file("/etc/hosts", "hosts", type=WORK_QUEUE_INPUT, cache=false)
    # @endcode
    def specify_file(self, local_name, remote_name=None, type=None, flags=None, cache=True):
	if remote_name is None:
	    remote_name = os.path.basename(local_name)

	if type is None:
	    type = WORK_QUEUE_INPUT

	flags = Task._determine_file_flags(flags, cache)
	return work_queue_task_specify_file(self._task, local_name, remote_name, type, flags)

    ##
    # Add a input file to the task.
    #
    # This is just a wrapper for @ref specify_file with type set to @ref WORK_QUEUE_INPUT.
    def specify_input_file(self, local_name, remote_name=None, flags=None, cache=True):
    	return self.specify_file(local_name, remote_name, WORK_QUEUE_INPUT, flags, cache)

    ##
    # Add a output file to the task.
    #
    # This is just a wrapper for @ref specify_file with type set to @ref WORK_QUEUE_OUTPUT.
    def specify_output_file(self, local_name, remote_name=None, flags=None, cache=True):
    	return self.specify_file(local_name, remote_name, WORK_QUEUE_OUTPUT, flags, cache)

    ##
    # Add an input bufer to the task.
    #
    # @param self	    Reference to the current task object.
    # @param buffer	    The contents of the buffer to pass as input.
    # @param remote_name    The name of the remote file to create.
    # @param flags	    May take the same values as @ref specify_file.
    # @param cache	    Legacy parameter for setting file caching attribute.  By default this is enabled.
    def specify_buffer(self, buffer, remote_name, flags=None, cache=True):
	flags = Task._determine_file_flags(flags, cache)
	return work_queue_task_specify_buffer(self._task, buffer, len(buffer), remote_name, flags)

    ##
    # Add a file created or handled by an arbitrary command to a task (eg. wget, ftp, chirp_get|put).
    #
    # @param self	    Reference to the current task object.
    # @param remote_name    The name of the remote file at the execution site.
    # @param command	    The contents of the buffer to pass as input.
    # @param type	    Must be one of the following values: @ref WORK_QUEUE_INPUT or @ref WORK_QUEUE_OUTPUT
    # @param flags	    May take the same values as @ref specify_file.
    # @param cache	    Legacy parameter for setting file caching attribute.  By default this is enabled.
    def specify_file_command(self, remote_name, command, type, flags, cache=True):
	flags = Task._determine_file_flags(flags, cache)
	return work_queue_task_specify_file_command(self._task, remote_name, command, type, flags)


##
# Python Work Queue object
#
# This class uses a dictionary to map between the task pointer objects and the
# @ref work_queue::Task.
class WorkQueue(_object):
    ##
    # Create a new work queue.
    #
    # @param self	Reference to the current work queue object.
    # @param port	The port number to listen on. If zero is specified, then the default is chosen, and if -1 is specified, a random port is chosen.
    # @param name	The project name to use.
    # @param catalog	Whether or not to enable catalog mode.
    # @param exclusive	Whether or not the workers should be exclusive.
    # @param shutdown	Automatically shutdown workers when queue is finished. Disabled by default.
    #
    # @see work_queue_create	- For more information about environmental variables that affect the behavior this method.
    def __init__(self, port=WORK_QUEUE_DEFAULT_PORT, name=None, catalog=True, exclusive=True, shutdown=False):
    	self._work_queue = work_queue_create(port)
    	self._stats	 = work_queue_stats()
    	self._task_table = {}
    	self._shutdown	 = shutdown

	if name:
	    work_queue_specify_name(self._work_queue, name)

    	work_queue_specify_master_mode(self._work_queue, catalog)
    	work_queue_specify_worker_mode(self._work_queue, exclusive)

    def __del__(self):
	if self._shutdown:
	    self.shutdown_workers(0)
    	work_queue_delete(self._work_queue)
    
    @property
    def name(self):
    	return work_queue_name(self._work_queue)

    @property
    def port(self):
    	return work_queue_port(self._work_queue)

    @property
    def stats(self):
    	work_queue_get_stats(self._work_queue, self._stats)
    	return self._stats

    ##
    # Turn on or off fast abort functionality for a given queue.
    #
    # @param self	Reference to the current work queue object.
    # @param multiplier	The multiplier of the average task time at which point to abort; if negative (the default) fast_abort is deactivated.
    def activate_fast_abort(self, multiplier):
    	return work_queue_activate_fast_abort(self._work_queue, multiplier)

    ##
    # Determine whether there are any known tasks queued, running, or waiting to be collected.
    #
    # Returns 0 if there are tasks remaining in the system, 1 if the system is "empty".
    #
    # @param self	Reference to the current work queue object.
    def empty(self):
    	return work_queue_empty(self._work_queue)

    ##
    # Determine whether the queue can support more tasks.
    #
    # Returns the number of additional tasks it can support if "hungry" and 0 if "sated".
    #
    # @param self	Reference to the current work queue object.
    def hungry(self):
    	return work_queue_hungry(self._work_queue)

    ##
    # Set the worker selection algorithm for queue.
    #
    # @param self	Reference to the current work queue object.
    # @param algorithm	One of the following algorithms to use in assigning a
    #			task to a worker:
    #			- @ref WORK_QUEUE_SCHEDULE_FCFS
    #			- @ref WORK_QUEUE_SCHEDULE_FILES
    #			- @ref WORK_QUEUE_SCHEDULE_TIME
    #			- @ref WORK_QUEUE_SCHEDULE_DEFAULT
    #			- @ref WORK_QUEUE_SCHEDULE_PREFERRED_HOSTS
    #			- @ref WORK_QUEUE_SCHEDULE_RAND
    def specify_algorithm(self, algorithm):
    	return work_queue_specify_algorithm(self._work_queue, algorithm)

    ##
    # Change the project name for the given queue.
    #
    # @param self   Reference to the current work queue object.
    # @param name   The new project name.
    def specify_name(self, name):
    	return work_queue_specify_name(self._work_queue, name)

    ##
    # Change the project priority for the given queue.
    #
    # @param self	Reference to the current work queue object.
    # @param priority	An integer that presents the priorty of this work queue master. The higher the value, the higher the priority.
    def specify_priority(self, priority):
    	return work_queue_specify_priority(self._work_queue, priority)

    ##
    # Specify the master mode for the given queue.
    #
    # @param self   Reference to the current work queue object.
    # @param mode   This may be one of the following values: @ref WORK_QUEUE_MASTER_MODE_STANDALONE or @ref WORK_QUEUE_MASTER_MODE_CATALOG.
    def specify_master_mode(self, mode):
    	return work_queue_specify_master_mode(self._work_queue, mode)

    ##
    # Specify the worker mode for the given queue.
    #
    # @param self   Reference to the current work queue object.
    # @param mode   This may be one of the following values: @ref WORK_QUEUE_WORKER_MODE_SHARED or @ref WORK_QUEUE_WORKER_MODE_EXCLUSIVE.
    def specify_worker_mode(self, mode):
    	return work_queue_specify_worker_mode(self._work_queue, mode)

    ##
    # Shutdown workers connected to queue.
    #
    # Gives a best effort and then returns the number of workers given the shutdown order.
    #
    # @param self   Reference to the current work queue object.
    # @param n	    The number to shutdown.  To shut down all workers, specify "0".
    def shutdown_workers(self, n):
    	return work_queue_shut_down_workers(self._work_queue, n)

    ##
    # Submit a task to the queue.
    #
    # It is safe to re-submit a task returned by @ref wait.
    #
    # @param self   Reference to the current work queue object.
    # @param task   A task description created from @ref work_queue::Task.
    def submit(self, task):
    	self._task_table[task.id] = task
    	return work_queue_submit(self._work_queue, task._task)

    ##
    # Wait for tasks to complete.
    #
    # This call will block until the timeout has elapsed
    #
    # @param self	Reference to the current work queue object.
    # @param timeout	The number of seconds to wait for a completed task
    #			before returning.  Use an integer to set the timeout or the constant @ref
    #			WORK_QUEUE_WAITFORTASK to block until a task has completed.
    def wait(self, timeout=WORK_QUEUE_WAITFORTASK):
    	task_pointer = work_queue_wait(self._work_queue, timeout)
	if task_pointer:
	    task = self._task_table[int(task_pointer.taskid)]
	    del(self._task_table[task_pointer.taskid])
	    return task
	return None
