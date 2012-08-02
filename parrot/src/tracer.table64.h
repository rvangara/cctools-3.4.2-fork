#define SYSCALL64_read 0
#define SYSCALL64_write 1
#define SYSCALL64_open 2
#define SYSCALL64_close 3
#define SYSCALL64_stat 4
#define SYSCALL64_fstat 5
#define SYSCALL64_lstat 6
#define SYSCALL64_poll 7
#define SYSCALL64_lseek 8
#define SYSCALL64_mmap 9
#define SYSCALL64_mprotect 10
#define SYSCALL64_munmap 11
#define SYSCALL64_brk 12
#define SYSCALL64_rt_sigaction 13
#define SYSCALL64_rt_sigprocmask 14
#define SYSCALL64_rt_sigreturn 15
#define SYSCALL64_ioctl 16
#define SYSCALL64_pread 17
#define SYSCALL64_pwrite 18
#define SYSCALL64_readv 19
#define SYSCALL64_writev 20
#define SYSCALL64_access 21
#define SYSCALL64_pipe 22
#define SYSCALL64_select 23
#define SYSCALL64_sched_yield 24
#define SYSCALL64_mremap 25
#define SYSCALL64_msync 26
#define SYSCALL64_mincore 27
#define SYSCALL64_madvise 28
#define SYSCALL64_shmget 29
#define SYSCALL64_shmat 30
#define SYSCALL64_shmctl 31
#define SYSCALL64_dup 32
#define SYSCALL64_dup2 33
#define SYSCALL64_pause 34
#define SYSCALL64_nanosleep 35
#define SYSCALL64_getitimer 36
#define SYSCALL64_alarm 37
#define SYSCALL64_setitimer 38
#define SYSCALL64_getpid 39
#define SYSCALL64_sendfile 40
#define SYSCALL64_socket 41
#define SYSCALL64_connect 42
#define SYSCALL64_accept 43
#define SYSCALL64_sendto 44
#define SYSCALL64_recvfrom 45
#define SYSCALL64_sendmsg 46
#define SYSCALL64_recvmsg 47
#define SYSCALL64_shutdown 48
#define SYSCALL64_bind 49
#define SYSCALL64_listen 50
#define SYSCALL64_getsockname 51
#define SYSCALL64_getpeername 52
#define SYSCALL64_socketpair 53
#define SYSCALL64_setsockopt 54
#define SYSCALL64_getsockopt 55
#define SYSCALL64_clone 56
#define SYSCALL64_fork 57
#define SYSCALL64_vfork 58
#define SYSCALL64_execve 59
#define SYSCALL64_exit 60
#define SYSCALL64_wait4 61
#define SYSCALL64_kill 62
#define SYSCALL64_uname 63
#define SYSCALL64_semget 64
#define SYSCALL64_semop 65
#define SYSCALL64_semctl 66
#define SYSCALL64_shmdt 67
#define SYSCALL64_msgget 68
#define SYSCALL64_msgsnd 69
#define SYSCALL64_msgrcv 70
#define SYSCALL64_msgctl 71
#define SYSCALL64_fcntl 72
#define SYSCALL64_flock 73
#define SYSCALL64_fsync 74
#define SYSCALL64_fdatasync 75
#define SYSCALL64_truncate 76
#define SYSCALL64_ftruncate 77
#define SYSCALL64_getdents 78
#define SYSCALL64_getcwd 79
#define SYSCALL64_chdir 80
#define SYSCALL64_fchdir 81
#define SYSCALL64_rename 82
#define SYSCALL64_mkdir 83
#define SYSCALL64_rmdir 84
#define SYSCALL64_creat 85
#define SYSCALL64_link 86
#define SYSCALL64_unlink 87
#define SYSCALL64_symlink 88
#define SYSCALL64_readlink 89
#define SYSCALL64_chmod 90
#define SYSCALL64_fchmod 91
#define SYSCALL64_chown 92
#define SYSCALL64_fchown 93
#define SYSCALL64_lchown 94
#define SYSCALL64_umask 95
#define SYSCALL64_gettimeofday 96
#define SYSCALL64_getrlimit 97
#define SYSCALL64_getrusage 98
#define SYSCALL64_sysinfo 99
#define SYSCALL64_times 100
#define SYSCALL64_ptrace 101
#define SYSCALL64_getuid 102
#define SYSCALL64_syslog 103
#define SYSCALL64_getgid 104
#define SYSCALL64_setuid 105
#define SYSCALL64_setgid 106
#define SYSCALL64_geteuid 107
#define SYSCALL64_getegid 108
#define SYSCALL64_setpgid 109
#define SYSCALL64_getppid 110
#define SYSCALL64_getpgrp 111
#define SYSCALL64_setsid 112
#define SYSCALL64_setreuid 113
#define SYSCALL64_setregid 114
#define SYSCALL64_getgroups 115
#define SYSCALL64_setgroups 116
#define SYSCALL64_setresuid 117
#define SYSCALL64_getresuid 118
#define SYSCALL64_setresgid 119
#define SYSCALL64_getresgid 120
#define SYSCALL64_getpgid 121
#define SYSCALL64_setfsuid 122
#define SYSCALL64_setfsgid 123
#define SYSCALL64_getsid 124
#define SYSCALL64_capget 125
#define SYSCALL64_capset 126
#define SYSCALL64_rt_sigpending 127
#define SYSCALL64_rt_sigtimedwait 128
#define SYSCALL64_rt_sigqueueinfo 129
#define SYSCALL64_rt_sigsuspend 130
#define SYSCALL64_sigaltstack 131
#define SYSCALL64_utime 132
#define SYSCALL64_mknod 133
#define SYSCALL64_uselib 134
#define SYSCALL64_personality 135
#define SYSCALL64_ustat 136
#define SYSCALL64_statfs 137
#define SYSCALL64_fstatfs 138
#define SYSCALL64_sysfs 139
#define SYSCALL64_getpriority 140
#define SYSCALL64_setpriority 141
#define SYSCALL64_sched_setparam 142
#define SYSCALL64_sched_getparam 143
#define SYSCALL64_sched_setscheduler 144
#define SYSCALL64_sched_getscheduler 145
#define SYSCALL64_sched_get_priority_max 146
#define SYSCALL64_sched_get_priority_min 147
#define SYSCALL64_sched_rr_get_interval 148
#define SYSCALL64_mlock 149
#define SYSCALL64_munlock 150
#define SYSCALL64_mlockall 151
#define SYSCALL64_munlockall 152
#define SYSCALL64_vhangup 153
#define SYSCALL64_modify_ldt 154
#define SYSCALL64_pivot_root 155
#define SYSCALL64__sysctl 156
#define SYSCALL64_prctl 157
#define SYSCALL64_arch_prctl 158
#define SYSCALL64_adjtimex 159
#define SYSCALL64_setrlimit 160
#define SYSCALL64_chroot 161
#define SYSCALL64_sync 162
#define SYSCALL64_acct 163
#define SYSCALL64_settimeofday 164
#define SYSCALL64_mount 165
#define SYSCALL64_umount2 166
#define SYSCALL64_swapon 167
#define SYSCALL64_swapoff 168
#define SYSCALL64_reboot 169
#define SYSCALL64_sethostname 170
#define SYSCALL64_setdomainname 171
#define SYSCALL64_iopl 172
#define SYSCALL64_ioperm 173
#define SYSCALL64_create_module 174
#define SYSCALL64_init_module 175
#define SYSCALL64_delete_module 176
#define SYSCALL64_get_kernel_syms 177
#define SYSCALL64_query_module 178
#define SYSCALL64_quotactl 179
#define SYSCALL64_nfsservctl 180
#define SYSCALL64_getpmsg 181
#define SYSCALL64_putpmsg 182
#define SYSCALL64_afs_syscall 183
#define SYSCALL64_tuxcall 184
#define SYSCALL64_security 185
#define SYSCALL64_gettid 186
#define SYSCALL64_readahead 187
#define SYSCALL64_setxattr 188
#define SYSCALL64_lsetxattr 189
#define SYSCALL64_fsetxattr 190
#define SYSCALL64_getxattr 191
#define SYSCALL64_lgetxattr 192
#define SYSCALL64_fgetxattr 193
#define SYSCALL64_listxattr 194
#define SYSCALL64_llistxattr 195
#define SYSCALL64_flistxattr 196
#define SYSCALL64_removexattr 197
#define SYSCALL64_lremovexattr 198
#define SYSCALL64_fremovexattr 199
#define SYSCALL64_tkill 200
#define SYSCALL64_time 201
#define SYSCALL64_futex 202
#define SYSCALL64_sched_setaffinity 203
#define SYSCALL64_sched_getaffinity 204
#define SYSCALL64_set_thread_area 205
#define SYSCALL64_io_setup 206
#define SYSCALL64_io_destroy 207
#define SYSCALL64_io_getevents 208
#define SYSCALL64_io_submit 209
#define SYSCALL64_io_cancel 210
#define SYSCALL64_get_thread_area 211
#define SYSCALL64_lookup_dcookie 212
#define SYSCALL64_epoll_create 213
#define SYSCALL64_epoll_ctl_old 214
#define SYSCALL64_epoll_wait_old 215
#define SYSCALL64_remap_file_pages 216
#define SYSCALL64_getdents64 217
#define SYSCALL64_set_tid_address 218
#define SYSCALL64_restart_syscall 219
#define SYSCALL64_semtimedop 220
#define SYSCALL64_fadvise64 221
#define SYSCALL64_timer_create 222
#define SYSCALL64_timer_settime 223
#define SYSCALL64_timer_gettime 224
#define SYSCALL64_timer_getoverrun 225
#define SYSCALL64_timer_delete 226
#define SYSCALL64_clock_settime 227
#define SYSCALL64_clock_gettime 228
#define SYSCALL64_clock_getres 229
#define SYSCALL64_clock_nanosleep 230
#define SYSCALL64_exit_group 231
#define SYSCALL64_epoll_wait 232
#define SYSCALL64_epoll_ctl 233
#define SYSCALL64_tgkill 234
#define SYSCALL64_utimes 235
#define SYSCALL64_vserver 236
#define SYSCALL64_mbind 237
#define SYSCALL64_set_mempolicy 238
#define SYSCALL64_get_mempolicy 239
#define SYSCALL64_mq_open 240
#define SYSCALL64_mq_unlink 241
#define SYSCALL64_mq_timedsend 242
#define SYSCALL64_mq_timedreceive 243
#define SYSCALL64_mq_notify 244
#define SYSCALL64_mq_getsetattr 245
#define SYSCALL64_kexec_load 246
#define SYSCALL64_waitid 247
#define SYSCALL64_add_key 248
#define SYSCALL64_request_key 249
#define SYSCALL64_keyctl 250
#define SYSCALL64_ioprio_set 251
#define SYSCALL64_ioprio_get 252
#define SYSCALL64_inotify_init 253
#define SYSCALL64_inotify_add_watch 254
#define SYSCALL64_inotify_rm_watch 255
#define SYSCALL64_migrate_pages 256
#define SYSCALL64_openat 257
#define SYSCALL64_mkdirat 258
#define SYSCALL64_mknodat 259
#define SYSCALL64_fchownat 260
#define SYSCALL64_futimesat 261
#define SYSCALL64_newfstatat 262
#define SYSCALL64_unlinkat 263
#define SYSCALL64_renameat 264
#define SYSCALL64_linkat 265
#define SYSCALL64_symlinkat 266
#define SYSCALL64_readlinkat 267
#define SYSCALL64_fchmodat 268
#define SYSCALL64_faccessat 269
#define SYSCALL64_pselect6 270
#define SYSCALL64_ppoll 271
#define SYSCALL64_unshare 272
#define SYSCALL64_set_robust_list 273
#define SYSCALL64_get_robust_list 274
#define SYSCALL64_splice 275
#define SYSCALL64_tee 276
#define SYSCALL64_sync_file_range 277
#define SYSCALL64_vmsplice 278
#define SYSCALL64_move_pages 279
#define SYSCALL64_utimensat 280
#define SYSCALL64_epoll_pwait 281
#define SYSCALL64_signalfd 282
#define SYSCALL64_timerfd_create 283
#define SYSCALL64_eventfd 284
#define SYSCALL64_fallocate 285
#define SYSCALL64_timerfd_settime 286
#define SYSCALL64_timerfd_gettime 287
#define SYSCALL64_accept4 288
#define SYSCALL64_signalfd4 289
#define SYSCALL64_eventfd2 290
#define SYSCALL64_epoll_create1 291
#define SYSCALL64_dup3 292
#define SYSCALL64_pipe2 293
#define SYSCALL64_inotify_init1 294
#define SYSCALL64_preadv 295
#define SYSCALL64_pwritev 296
#define SYSCALL64_rt_tgsigqueueinfo 297
#define SYSCALL64_perf_event_open 298
#define SYSCALL64_recvmmsg 299
#define SYSCALL64_fanotify_init 300
#define SYSCALL64_fanotify_mark 201
#define SYSCALL64_prlimit64 302
#define SYSCALL64_unknown303 303
#define SYSCALL64_unknown304 304
#define SYSCALL64_unknown305 305
#define SYSCALL64_unknown306 306
#define SYSCALL64_unknown307 307
#define SYSCALL64_unknown308 308
#define SYSCALL64_unknown309 309
#define SYSCALL64_parrot_lsalloc 310
#define SYSCALL64_parrot_mkalloc 311
#define SYSCALL64_parrot_getacl 312
#define SYSCALL64_parrot_setacl 313
#define SYSCALL64_parrot_whoami 314
#define SYSCALL64_parrot_copyfile 315
#define SYSCALL64_parrot_md5 316
#define SYSCALL64_parrot_locate 317
#define SYSCALL64_parrot_timeout 318
#define SYSCALL64_MAX 318