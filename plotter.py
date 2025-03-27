import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
seq_read_4k = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_4k_60_sec.csv'
seq_read_8k = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_8k_60_sec.csv'
seq_read_16k = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_16k_60_sec.csv'
seq_read_32k = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_32k_60_sec.csv'
seq_read_64k = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_64k_60_sec.csv'
seq_read_128k = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_128k_60_sec.csv'
seq_read_256k = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_256k_60_sec.csv'
seq_read_512k = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_512k_60_sec.csv'
seq_read_1m = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_1024k_60_sec.csv'
seq_read_2m = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_2048k_60_sec.csv'
seq_read_4m = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_4096k_60_sec.csv'
seq_read_8m = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_8192k_60_sec.csv'
seq_read_16m = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_16384k_60_sec.csv'
seq_read_32m = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_32768k_60_sec.csv'
seq_read_64m = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_65536k_60_sec.csv'
seq_read_128m = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_131072k_60_sec.csv'
seq_read_256m = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_262144k_60_sec.csv'
seq_read_512m = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_524288k_60_sec.csv'
seq_read_1g = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_1048576k_60_sec.csv'
seq_read_max = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_max_60_sec.csv'
seq_tmpfs = '/csl/daniel.br/swap_proj/disk_bench/seq_bench/io_bench_results_seq_read_4k_30_sec_tmpfs.csv'

rand_read_4k = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_4k_60_sec.csv'
rand_read_8k = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_8k_60_sec.csv'
rand_read_16k = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_16k_60_sec.csv'
rand_read_32k = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_32k_60_sec.csv'
rand_read_64k = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_64k_60_sec.csv'
rand_read_128k = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_128k_60_sec.csv'
rand_read_256k = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_256k_60_sec.csv'
rand_read_512k = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_512k_60_sec.csv'
rand_read_1m = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_1024k_60_sec.csv'
rand_read_2m = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_2048k_60_sec.csv'
rand_read_4m = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_4096k_60_sec.csv'
rand_read_8m = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_8192k_60_sec.csv'
rand_read_16m = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_16384k_60_sec.csv'
rand_read_32m = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_32768k_60_sec.csv'
rand_read_64m = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_65536k_60_sec.csv'
rand_read_128m = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_131072k_60_sec.csv'
rand_read_256m = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_262144k_60_sec.csv'
rand_read_512m = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_524288k_60_sec.csv'
rand_read_1g = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_1048576k_60_sec.csv'
rand_read_max = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_max_60_sec.csv'
rand_tmpfs = '/csl/daniel.br/swap_proj/disk_bench/rand_bench/io_bench_results_rand_read_4k_30_sec_tmpfs.csv'



headers = ['file_size','warmup_throughput','avg_throughput','user_time','kernel_time','read_syscalls','write_syscalls','rps','rqsz','r_lat','len']
seq_read_4k = pd.read_csv(seq_read_4k,header=None,names=headers)
seq_read_8k = pd.read_csv(seq_read_8k,header=None,names=headers)
seq_read_16k = pd.read_csv(seq_read_16k,header=None,names=headers)
seq_read_32k = pd.read_csv(seq_read_32k,header=None,names=headers)
seq_read_64k = pd.read_csv(seq_read_64k,header=None,names=headers)
seq_read_128k = pd.read_csv(seq_read_128k,header=None,names=headers)
seq_read_256k = pd.read_csv(seq_read_256k,header=None,names=headers)
seq_read_512k = pd.read_csv(seq_read_512k,header=None,names=headers)
seq_read_1m = pd.read_csv(seq_read_1m,header=None,names=headers)
seq_read_2m = pd.read_csv(seq_read_2m,header=None,names=headers)
seq_read_4m = pd.read_csv(seq_read_4m,header=None,names=headers)
seq_read_8m = pd.read_csv(seq_read_8m,header=None,names=headers)
seq_read_16m = pd.read_csv(seq_read_16m,header=None,names=headers)
seq_read_32m = pd.read_csv(seq_read_32m,header=None,names=headers)
seq_read_64m = pd.read_csv(seq_read_64m,header=None,names=headers)
seq_read_128m = pd.read_csv(seq_read_128m,header=None,names=headers)
seq_read_256m = pd.read_csv(seq_read_256m,header=None,names=headers)
seq_read_512m = pd.read_csv(seq_read_512m,header=None,names=headers)
seq_read_1g = pd.read_csv(seq_read_1g,header=None,names=headers)
seq_tmpfs = pd.read_csv(seq_tmpfs,header=None,names=headers)

rand_read_4k = pd.read_csv(rand_read_4k,header=None,names=headers)
rand_read_8k = pd.read_csv(rand_read_8k,header=None,names=headers)
rand_read_16k = pd.read_csv(rand_read_16k,header=None,names=headers)
rand_read_32k = pd.read_csv(rand_read_32k,header=None,names=headers)
rand_read_64k = pd.read_csv(rand_read_64k,header=None,names=headers)
rand_read_128k = pd.read_csv(rand_read_128k,header=None,names=headers)
rand_read_256k = pd.read_csv(rand_read_256k,header=None,names=headers)
rand_read_512k = pd.read_csv(rand_read_512k,header=None,names=headers)
rand_read_1m = pd.read_csv(rand_read_1m,header=None,names=headers)
rand_read_2m = pd.read_csv(rand_read_2m,header=None,names=headers)
rand_read_4m = pd.read_csv(rand_read_4m,header=None,names=headers)
rand_read_8m = pd.read_csv(rand_read_8m,header=None,names=headers)
rand_read_16m = pd.read_csv(rand_read_16m,header=None,names=headers)
rand_read_32m = pd.read_csv(rand_read_32m,header=None,names=headers)
rand_read_64m = pd.read_csv(rand_read_64m,header=None,names=headers)
rand_read_128m = pd.read_csv(rand_read_128m,header=None,names=headers)
rand_read_256m = pd.read_csv(rand_read_256m,header=None,names=headers)
rand_read_512m = pd.read_csv(rand_read_512m,header=None,names=headers)
rand_read_1g = pd.read_csv(rand_read_1g,header=None,names=headers)
rand_tmpfs = pd.read_csv(rand_tmpfs,header=None,names=headers)

fig, axes = plt.subplots(2, 5, figsize=(30, 12))  # 2 rows, 5 columns
ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10 = axes.flatten()# from 4k to 1GB
file_size_ticks = [4096,8192,16384,32768, 65536, 131072,262144,524288,1048576,2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296, 8589934592]
file_size_labels = ['4KB','8KB', '16KB','32KB', '64KB','128KB','256KB','512KB','1MB', '2MB', '4MB', '8MB', '16MB', '32MB', '64MB', '128MB', '256MB', '512MB', '1GB','2GB','4GB','8GB']
file_size_ticks2 = [2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296, 8589934592]
file_size_labels2 = ['2MB', '4MB', '8MB', '16MB', '32MB', '64MB', '128MB', '256MB', '512MB', '1GB','2GB','4GB','8GB']
# plot all three columds, x axis is sizeds, y axis is throughput
ax1.plot(seq_read_1m['file_size'],seq_read_1m['avg_throughput'], label='seq 1MB',marker='*')
ax1.plot(seq_read_512k['file_size'],seq_read_512k['avg_throughput'], label='seq 512KB',marker='1')
ax1.plot(seq_read_256k['file_size'],seq_read_256k['avg_throughput'], label='seq 256KB',marker='d')
ax1.plot(seq_read_128k['file_size'],seq_read_128k['avg_throughput'], label='seq 128KB',marker='v')
ax1.plot(seq_read_64k['file_size'], seq_read_64k['avg_throughput'], label='seq 64KB',marker='<')
ax1.plot(seq_read_32k['file_size'], seq_read_32k['avg_throughput'], label='seq 32KB',marker='^')
ax1.plot(seq_read_16k['file_size'], seq_read_16k['avg_throughput'], label='seq 16KB',marker='>')
ax1.plot(seq_read_8k['file_size'], seq_read_8k['avg_throughput'], label='seq 8KB',marker='o')
ax1.plot(seq_read_4k['file_size'], seq_read_4k['avg_throughput'], label='seq 4KB',marker='x')
# ax1.plot(df_seq_read_10k_tmpfs['file_size'],df_seq_read_10k_tmpfs['avg_throughput'], label='seq tmpfs',marker='P')
ax1.set_xlabel('file size')
ax1.set_ylabel('throughput (MB/s)')
ax1.legend(loc='upper left')
ax1.grid()
ax1.set_xscale('log')
ax1.set_xticks(ticks=file_size_ticks, labels=file_size_labels, rotation=40)
ax1.set_yticks(ticks=[0,100,200,300,400,500,600,700,800],labels=["0","100","200","300","400","500","600","700","800"])
ax1.set_ylim(bottom=0)
ax2.plot(seq_read_1m['file_size'],(seq_read_1m['user_time']+seq_read_1m['kernel_time'])/seq_read_1m['len'], label='seq 1MB',marker='*')
ax2.plot(seq_read_512k['file_size'],(seq_read_512k['user_time']+seq_read_512k['kernel_time'])/seq_read_512k['len'], label='seq 512KB',marker='1')
ax2.plot(seq_read_256k['file_size'],(seq_read_256k['user_time']+seq_read_256k['kernel_time'])/seq_read_256k['len'], label='seq 256KB',marker='d')
ax2.plot(seq_read_128k['file_size'],(seq_read_128k['user_time']+seq_read_128k['kernel_time'])/seq_read_128k['len'], label='seq 128KB',marker='v')
ax2.plot(seq_read_64k['file_size'], (seq_read_64k['user_time']+seq_read_64k['kernel_time'])/seq_read_64k['len'], label='seq 64KB',marker='<')
ax2.plot(seq_read_32k['file_size'], (seq_read_32k['user_time']+seq_read_32k['kernel_time'])/seq_read_32k['len'], label='seq 32KB',marker='^')
ax2.plot(seq_read_16k['file_size'], (seq_read_16k['user_time']+seq_read_16k['kernel_time'])/seq_read_16k['len'], label='seq 16KB',marker='>')
ax2.plot(seq_read_8k['file_size'], (seq_read_8k['user_time']+seq_read_8k['kernel_time'])/seq_read_8k['len'], label='seq 8KB',marker='o')
ax2.plot(seq_read_4k['file_size'], (seq_read_4k['user_time']+seq_read_4k['kernel_time'])/seq_read_4k['len'], label='seq 4KB',marker='x')
ax2.set_xlabel('file size')
ax2.set_ylabel('CPU')
ax2.legend(loc='upper left')
ax2.grid()
ax2.set_xscale('log')
ax2.set_yticks(ticks=[0,0.05,0.1,0.15],labels=["0%","5%","10%","15%"])
ax2.set_xticks(ticks=file_size_ticks, labels=file_size_labels, rotation=40)

ax3.plot(seq_read_1m['file_size'],seq_read_1m['rps'], label='seq 1MB',marker='*')
ax3.plot(seq_read_512k['file_size'],seq_read_512k['rps'], label='seq 512KB',marker='1')
ax3.plot(seq_read_256k['file_size'],seq_read_256k['rps'], label='seq 256KB',marker='d')
ax3.plot(seq_read_128k['file_size'],seq_read_128k['rps'], label='seq 128KB',marker='v')
ax3.plot(seq_read_64k['file_size'], seq_read_64k['rps'], label='seq 64KB',marker='<')
ax3.plot(seq_read_32k['file_size'], seq_read_32k['rps'], label='seq 32KB',marker='^')
ax3.plot(seq_read_16k['file_size'],seq_read_16k['rps'], label='seq 16KB',marker='>')
ax3.plot(seq_read_8k['file_size'],seq_read_8k['rps'], label='seq 8KB',marker='o')
ax3.plot(seq_read_4k['file_size'],seq_read_4k['rps'], label='seq 4KB',marker='x')
ax3.set_xlabel('file size')
ax3.set_ylabel('IOps')
ax3.legend(loc='upper left')
ax3.grid()
ax3.set_xscale('log')
# ax3.set_yticks(ticks=[0,0.05,0.1,0.15,0.2,0.25,0.3],labels=["0%","5%","10%","15%","20%","25%","30%"])
ax3.set_xticks(ticks=file_size_ticks, labels=file_size_labels, rotation=40)

ax4.plot(seq_read_1m['file_size'],seq_read_1m['rqsz'], label='seq 1MB',marker='*')
ax4.plot(seq_read_512k['file_size'],seq_read_512k['rqsz'], label='seq 512KB',marker='1')
ax4.plot(seq_read_256k['file_size'],seq_read_256k['rqsz'], label='seq 256KB',marker='d')
ax4.plot(seq_read_128k['file_size'],seq_read_128k['rqsz'], label='seq 128KB',marker='v')
ax4.plot(seq_read_64k['file_size'], seq_read_64k['rqsz'], label='seq 64KB',marker='<')
ax4.plot(seq_read_32k['file_size'], seq_read_32k['rqsz'], label='seq 32KB',marker='^')
ax4.plot(seq_read_16k['file_size'], seq_read_16k['rqsz'], label='seq 16KB',marker='>')
ax4.plot(seq_read_8k['file_size'], seq_read_8k['rqsz'], label='seq 8KB',marker='o')
ax4.plot(seq_read_4k['file_size'], seq_read_4k['rqsz'], label='seq 4KB',marker='x')
ax4.set_xlabel('file size')
ax4.set_ylabel('request size')
ax4.legend(loc='upper left')
ax4.grid()
ax4.set_xscale('log')
ax4.set_xticks(ticks=file_size_ticks, labels=file_size_labels, rotation=40)
ax4.set_yscale('log')
ax4.set_yticks(ticks=[1,2,4,8,16,32,64,128,256],labels=['1k','2k','4k','8k','16k','32k','64k','128k','256k'])
seq_read_4m['r_lat'].replace(0, np.nan, inplace=True)
seq_read_2m['r_lat'].replace(0, np.nan, inplace=True)
seq_read_1m['r_lat'].replace(0, np.nan, inplace=True)
seq_read_512k['r_lat'].replace(0, np.nan, inplace=True)
seq_read_256k['r_lat'].replace(0, np.nan, inplace=True)
seq_read_128k['r_lat'].replace(0, np.nan, inplace=True)
seq_read_64k['r_lat'].replace(0, np.nan, inplace=True)
seq_read_32k['r_lat'].replace(0, np.nan, inplace=True)
seq_read_16k['r_lat'].replace(0, np.nan, inplace=True)
seq_read_8k['r_lat'].replace(0, np.nan, inplace=True)
seq_read_4k['r_lat'].replace(0, np.nan, inplace=True)

ax5.plot(seq_read_1m['file_size'],seq_read_1m['r_lat'].astype(float)*1000, label='seq 1MB',marker='*')
ax5.plot(seq_read_512k['file_size'],seq_read_512k['r_lat'].astype(float)*1000, label='seq 512KB',marker='1')
ax5.plot(seq_read_256k['file_size'],seq_read_256k['r_lat'].astype(float)*1000, label='seq 256KB',marker='d')
ax5.plot(seq_read_128k['file_size'],seq_read_128k['r_lat'].astype(float)*1000, label='seq 128KB',marker='v')
ax5.plot(seq_read_64k['file_size'], seq_read_64k['r_lat'].astype(float)*1000, label='seq 64KB',marker='<')
ax5.plot(seq_read_32k['file_size'], seq_read_32k['r_lat'].astype(float)*1000, label='seq 32KB',marker='^')
ax5.plot(seq_read_16k['file_size'], seq_read_16k['r_lat'].astype(float)*1000, label='seq 16KB',marker='>')
ax5.plot(seq_read_8k['file_size'], seq_read_8k['r_lat'].astype(float)*1000, label='seq 8KB',marker='o') 
ax5.plot(seq_read_4k['file_size'], seq_read_4k['r_lat'].astype(float)*1000, label='seq 4KB',marker='x')
ax5.set_xlabel('file size')
ax5.set_ylabel('read latency')
ax5.legend(loc='upper left')
ax5.grid()
ax5.set_xscale('log')
ax5.set_yscale('log')
ax5.set_xticks(ticks=file_size_ticks[7:14], labels=file_size_labels[7:14], rotation=40)
ax5.set_yticks(ticks=[10,20,50,100,200,500,1000,2000,5000],labels=['10µs','20µs','50µs','100µs','200µs','500µs','1ms','2ms','5ms'])
# ax5.set_yticks(ticks=[0,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1],labels=["0%","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%"])

#plot second row 
ax6.plot(seq_read_1g['file_size'],seq_read_1g['avg_throughput'], label='seq 1GB',marker='.')
ax6.plot(seq_read_512m['file_size'],seq_read_512m['avg_throughput'], label='seq 512MB',marker='*')
ax6.plot(seq_read_256m['file_size'],seq_read_256m['avg_throughput'], label='seq 256MB',marker='1')
ax6.plot(seq_read_128m['file_size'],seq_read_128m['avg_throughput'], label='seq 128MB',marker='d')
ax6.plot(seq_read_64m['file_size'],seq_read_64m['avg_throughput'], label='seq 64MB',marker='v')
ax6.plot(seq_read_32m['file_size'], seq_read_32m['avg_throughput'], label='seq 32MB',marker='<')
ax6.plot(seq_read_16m['file_size'], seq_read_16m['avg_throughput'], label='seq 16MB',marker='^')
ax6.plot(seq_read_8m['file_size'], seq_read_8m['avg_throughput'], label='seq 8MB',marker='>')
ax6.plot(seq_read_4m['file_size'], seq_read_4m['avg_throughput'], label='seq 4MB',marker='o')
ax6.plot(seq_read_2m['file_size'], seq_read_2m['avg_throughput'], label='seq 2MB',marker='x')
# ax6.plot(df_seq_read_10k_tmpfs['file_size'],df_seq_read_10k_tmpfs['avg_throughput'], label='seq tmpfs',marker='P')
ax6.set_xlabel('file size')
ax6.set_ylabel('throughput (MB/s)')
ax6.legend(loc='upper right')
ax6.grid()
ax6.set_xscale('log')
ax6.set_xticks(ticks=file_size_ticks2, labels=file_size_labels2, rotation=40)
ax6.set_yticks(ticks=[0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500],labels=["0","100","200","300","400","500","600","700","800","900","1000","1100","1200","1300","1400","1500"])
ax6.set_ylim(bottom=0)
ax7.plot(seq_read_1g['file_size'],(seq_read_1g['user_time']+seq_read_1g['kernel_time'])/seq_read_1g['len'], label='seq 1GB',marker='.')
ax7.plot(seq_read_512m['file_size'],(seq_read_512m['user_time']+seq_read_512m['kernel_time'])/seq_read_512m['len'], label='seq 512MB',marker='*')
ax7.plot(seq_read_256m['file_size'],(seq_read_256m['user_time']+seq_read_256m['kernel_time'])/seq_read_256m['len'], label='seq 256MB',marker='1')
ax7.plot(seq_read_128m['file_size'],(seq_read_128m['user_time']+seq_read_128m['kernel_time'])/seq_read_128m['len'], label='seq 128MB',marker='d')
ax7.plot(seq_read_64m['file_size'],(seq_read_64m['user_time']+seq_read_64m['kernel_time'])/seq_read_64m['len'], label='seq 64MB',marker='v')
ax7.plot(seq_read_32m['file_size'], (seq_read_32m['user_time']+seq_read_32m['kernel_time'])/seq_read_32m['len'], label='seq 32MB',marker='<')
ax7.plot(seq_read_16m['file_size'], (seq_read_16m['user_time']+seq_read_16m['kernel_time'])/seq_read_16m['len'], label='seq 16MB',marker='^')
ax7.plot(seq_read_8m['file_size'], (seq_read_8m['user_time']+seq_read_8m['kernel_time'])/seq_read_8m['len'], label='seq 8MB',marker='>')
ax7.plot(seq_read_4m['file_size'], (seq_read_4m['user_time']+seq_read_4m['kernel_time'])/seq_read_4m['len'], label='seq 4MB',marker='o')
ax7.plot(seq_read_2m['file_size'], (seq_read_2m['user_time']+seq_read_2m['kernel_time'])/seq_read_2m['len'], label='seq 2MB',marker='x')
ax7.set_xlabel('file size')
ax7.set_ylabel('CPU')
ax7.legend(loc='upper right')
ax7.grid()
ax7.set_xscale('log')
ax7.set_yticks(ticks=[0,0.05,0.1,0.15],labels=["0%","5%","10%","15%"])
ax7.set_xticks(ticks=file_size_ticks2, labels=file_size_labels2, rotation=40)

ax8.plot(seq_read_1g['file_size'],seq_read_1g['rps'], label='seq 1GB',marker='.')
ax8.plot(seq_read_512m['file_size'],seq_read_512m['rps'], label='seq 512MB',marker='*')
ax8.plot(seq_read_256m['file_size'],seq_read_256m['rps'], label='seq 256MB',marker='1')
ax8.plot(seq_read_128m['file_size'],seq_read_128m['rps'], label='seq 128MB',marker='d')
ax8.plot(seq_read_64m['file_size'],seq_read_64m['rps'], label='seq 64MB',marker='v')
ax8.plot(seq_read_32m['file_size'], seq_read_32m['rps'], label='seq 32MB',marker='<')
ax8.plot(seq_read_16m['file_size'], seq_read_16m['rps'], label='seq 16MB',marker='^')
ax8.plot(seq_read_8m['file_size'],seq_read_8m['rps'], label='seq 8MB',marker='>')
ax8.plot(seq_read_4m['file_size'],seq_read_4m['rps'], label='seq 4MB',marker='o')
ax8.plot(seq_read_2m['file_size'],seq_read_2m['rps'], label='seq 2MB',marker='x')
ax8.set_xlabel('file size')
ax8.set_ylabel('IOps')
ax8.legend(loc='upper right')
ax8.grid()
ax8.set_xscale('log')
# ax8.set_yticks(ticks=[0,0.05,0.1,0.15,0.2,0.25,0.3],labels=["0%","5%","10%","15%","20%","25%","30%"])
ax8.set_xticks(ticks=file_size_ticks2, labels=file_size_labels2, rotation=40)

ax9.plot(seq_read_1g['file_size'],seq_read_1g['rqsz'], label='seq 1GB',marker='.')
ax9.plot(seq_read_512m['file_size'],seq_read_512m['rqsz'], label='seq 512MB',marker='*')
ax9.plot(seq_read_256m['file_size'],seq_read_256m['rqsz'], label='seq 256MB',marker='1')
ax9.plot(seq_read_128m['file_size'],seq_read_128m['rqsz'], label='seq 128MB',marker='d')
ax9.plot(seq_read_64m['file_size'],seq_read_64m['rqsz'], label='seq 64MB',marker='v')
ax9.plot(seq_read_32m['file_size'], seq_read_32m['rqsz'], label='seq 32MB',marker='<')
ax9.plot(seq_read_16m['file_size'], seq_read_16m['rqsz'], label='seq 16MB',marker='^')
ax9.plot(seq_read_8m['file_size'], seq_read_8m['rqsz'], label='seq 8MB',marker='>')
ax9.plot(seq_read_4m['file_size'], seq_read_4m['rqsz'], label='seq 4MB',marker='o')
ax9.plot(seq_read_2m['file_size'], seq_read_2m['rqsz'], label='seq 2MB',marker='x')
ax9.set_xlabel('file size')
ax9.set_ylabel('request size')
ax9.legend(loc='upper left')
ax9.grid()
ax9.set_xscale('log')
ax9.set_xticks(ticks=file_size_ticks2, labels=file_size_labels2, rotation=40)
ax9.set_yscale('log')
ax9.set_yticks(ticks=[1,2,4,8,16,32,64,128,256],labels=['1k','2k','4k','8k','16k','32k','64k','128k','256k'])
# ax9.set_yticks(ticks=[0,0.05,0.1,0.15,0.2,0.25,0.3],labels=["0%","5%","10%","15%","20%","25%","30%"])

ax10.plot(seq_read_1g['file_size'],seq_read_1g['r_lat'].astype(float)/100, label='seq 1GB',marker='.')
ax10.plot(seq_read_512m['file_size'],seq_read_512m['r_lat'].astype(float)/100, label='seq 512MB',marker='*')
ax10.plot(seq_read_256m['file_size'],seq_read_256m['r_lat'].astype(float)/100, label='seq 256MB',marker='1')
ax10.plot(seq_read_128m['file_size'],seq_read_128m['r_lat'].astype(float)/100, label='seq 128MB',marker='d')
ax10.plot(seq_read_64m['file_size'],seq_read_64m['r_lat'].astype(float)/100, label='seq 64MB',marker='v')
ax10.plot(seq_read_32m['file_size'], seq_read_32m['r_lat'].astype(float)/100, label='seq 32MB',marker='<')
ax10.plot(seq_read_16m['file_size'], seq_read_16m['r_lat'].astype(float)/100, label='seq 16MB',marker='^')
ax10.plot(seq_read_8m['file_size'], seq_read_8m['r_lat'].astype(float)/100, label='seq 8MB',marker='>')
ax10.plot(seq_read_4m['file_size'], seq_read_4m['r_lat'].astype(float)/100, label='seq 4MB',marker='o')
ax10.plot(seq_read_2m['file_size'], seq_read_2m['r_lat'].astype(float)/100, label='seq 2MB',marker='x')
ax10.set_xlabel('file size')
ax10.set_ylabel('disk util')
ax10.legend(loc='upper left')
ax10.grid()
ax10.set_xscale('log')
ax10.set_xticks(ticks=file_size_ticks2, labels=file_size_labels2, rotation=40)
ax10.set_yticks(ticks=[0,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1],labels=["0%","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%"])




plt.tight_layout()
fig.savefig('seq_bench/results_read_seq.png')











fig, axes = plt.subplots(2, 5, figsize=(30, 12))  # 2 rows, 5 columns
ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10 = axes.flatten()# from 4k to 1GB
file_size_ticks = [4096,8192,16384,32768, 65536, 131072,262144,524288,1048576,2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296,8589934592]
file_size_labels = ['4KB','8KB', '16KB','32KB', '64KB','128KB','256KB','512KB','1MB', '2MB', '4MB', '8MB', '16MB', '32MB', '64MB', '128MB', '256MB', '512MB', '1GB','2GB','4GB','8GB']
file_size_ticks2 = [2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296,8589934592]
file_size_labels2 = ['2MB', '4MB', '8MB', '16MB', '32MB', '64MB', '128MB', '256MB', '512MB', '1GB','2GB','4GB','8GB']
# plot all three columds, x axis is sizeds, y axis is throughput
ax1.plot(rand_read_1m['file_size'],rand_read_1m['avg_throughput'], label='rand 1MB',marker='*')
ax1.plot(rand_read_512k['file_size'],rand_read_512k['avg_throughput'], label='rand 512KB',marker='1')
ax1.plot(rand_read_256k['file_size'],rand_read_256k['avg_throughput'], label='rand 256KB',marker='d')
ax1.plot(rand_read_128k['file_size'],rand_read_128k['avg_throughput'], label='rand 128KB',marker='v')
ax1.plot(rand_read_64k['file_size'], rand_read_64k['avg_throughput'], label='rand 64KB',marker='<')
ax1.plot(rand_read_32k['file_size'], rand_read_32k['avg_throughput'], label='rand 32KB',marker='^')
ax1.plot(rand_read_16k['file_size'], rand_read_16k['avg_throughput'], label='rand 16KB',marker='>')
ax1.plot(rand_read_8k['file_size'], rand_read_8k['avg_throughput'], label='rand 8KB',marker='o')
ax1.plot(rand_read_4k['file_size'], rand_read_4k['avg_throughput'], label='rand 4KB',marker='x')
# ax1.plot(df_rand_read_10k_tmpfs['file_size'],df_rand_read_10k_tmpfs['avg_throughput'], label='rand tmpfs',marker='P')
ax1.set_xlabel('file size')
ax1.set_ylabel('throughput (MB/s)')
ax1.legend(loc='upper left')
ax1.grid()
ax1.set_xscale('log')
ax1.set_xticks(ticks=file_size_ticks, labels=file_size_labels, rotation=40)
ax1.set_yticks(ticks=[0,100,200,300,400,500,600,700,800],labels=["0","100","200","300","400","500","600","700","800"])
ax1.set_ylim(bottom=0)
ax2.plot(rand_read_1m['file_size'],(rand_read_1m['user_time']+rand_read_1m['kernel_time'])/rand_read_1m['len'], label='rand 1MB',marker='*')
ax2.plot(rand_read_512k['file_size'],(rand_read_512k['user_time']+rand_read_512k['kernel_time'])/rand_read_512k['len'], label='rand 512KB',marker='1')
ax2.plot(rand_read_256k['file_size'],(rand_read_256k['user_time']+rand_read_256k['kernel_time'])/rand_read_256k['len'], label='rand 256KB',marker='d')
ax2.plot(rand_read_128k['file_size'],(rand_read_128k['user_time']+rand_read_128k['kernel_time'])/rand_read_128k['len'], label='rand 128KB',marker='v')
ax2.plot(rand_read_64k['file_size'], (rand_read_64k['user_time']+rand_read_64k['kernel_time'])/rand_read_64k['len'], label='rand 64KB',marker='<')
ax2.plot(rand_read_32k['file_size'], (rand_read_32k['user_time']+rand_read_32k['kernel_time'])/rand_read_32k['len'], label='rand 32KB',marker='^')
ax2.plot(rand_read_16k['file_size'], (rand_read_16k['user_time']+rand_read_16k['kernel_time'])/rand_read_16k['len'], label='rand 16KB',marker='>')
ax2.plot(rand_read_8k['file_size'], (rand_read_8k['user_time']+rand_read_8k['kernel_time'])/rand_read_8k['len'], label='rand 8KB',marker='o')
ax2.plot(rand_read_4k['file_size'], (rand_read_4k['user_time']+rand_read_4k['kernel_time'])/rand_read_4k['len'], label='rand 4KB',marker='x')
ax2.set_xlabel('file size')
ax2.set_ylabel('CPU')
ax2.legend(loc='upper left')
ax2.grid()
ax2.set_xscale('log')
ax2.set_yticks(ticks=[0,0.05,0.1,0.15],labels=["0%","5%","10%","15%"])
ax2.set_xticks(ticks=file_size_ticks, labels=file_size_labels, rotation=40)

ax3.plot(rand_read_1m['file_size'],rand_read_1m['rps'], label='rand 1MB',marker='*')
ax3.plot(rand_read_512k['file_size'],rand_read_512k['rps'], label='rand 512KB',marker='1')
ax3.plot(rand_read_256k['file_size'],rand_read_256k['rps'], label='rand 256KB',marker='d')
ax3.plot(rand_read_128k['file_size'],rand_read_128k['rps'], label='rand 128KB',marker='v')
ax3.plot(rand_read_64k['file_size'], rand_read_64k['rps'], label='rand 64KB',marker='<')
ax3.plot(rand_read_32k['file_size'], rand_read_32k['rps'], label='rand 32KB',marker='^')
ax3.plot(rand_read_16k['file_size'],rand_read_16k['rps'], label='rand 16KB',marker='>')
ax3.plot(rand_read_8k['file_size'],rand_read_8k['rps'], label='rand 8KB',marker='o')
ax3.plot(rand_read_4k['file_size'],rand_read_4k['rps'], label='rand 4KB',marker='x')
ax3.set_xlabel('file size')
ax3.set_ylabel('IOps')
ax3.legend(loc='upper left')
ax3.grid()
ax3.set_xscale('log')
# ax3.set_yticks(ticks=[0,0.05,0.1,0.15,0.2,0.25,0.3],labels=["0%","5%","10%","15%","20%","25%","30%"])
ax3.set_xticks(ticks=file_size_ticks, labels=file_size_labels, rotation=40)

ax4.plot(rand_read_1m['file_size'],rand_read_1m['rqsz'], label='rand 1MB',marker='*')
ax4.plot(rand_read_512k['file_size'],rand_read_512k['rqsz'], label='rand 512KB',marker='1')
ax4.plot(rand_read_256k['file_size'],rand_read_256k['rqsz'], label='rand 256KB',marker='d')
ax4.plot(rand_read_128k['file_size'],rand_read_128k['rqsz'], label='rand 128KB',marker='v')
ax4.plot(rand_read_64k['file_size'], rand_read_64k['rqsz'], label='rand 64KB',marker='<')
ax4.plot(rand_read_32k['file_size'], rand_read_32k['rqsz'], label='rand 32KB',marker='^')
ax4.plot(rand_read_16k['file_size'], rand_read_16k['rqsz'], label='rand 16KB',marker='>')
ax4.plot(rand_read_8k['file_size'], rand_read_8k['rqsz'], label='rand 8KB',marker='o')
ax4.plot(rand_read_4k['file_size'], rand_read_4k['rqsz'], label='rand 4KB',marker='x')
ax4.set_xlabel('file size')
ax4.set_ylabel('request size')
ax4.legend(loc='upper left')
ax4.grid()
ax4.set_xscale('log')
ax4.set_xticks(ticks=file_size_ticks, labels=file_size_labels, rotation=40)
ax4.set_yscale('log')
ax4.set_yticks(ticks=[1,2,4,8,16,32,64,128,256],labels=['1k','2k','4k','8k','16k','32k','64k','128k','256k'])

ax5.plot(rand_read_1m['file_size'],rand_read_1m['r_lat'].astype(float)*1000, label='rand 1MB',marker='*')
ax5.plot(rand_read_512k['file_size'],rand_read_512k['r_lat'].astype(float)*1000, label='rand 512KB',marker='1')
ax5.plot(rand_read_256k['file_size'],rand_read_256k['r_lat'].astype(float)*1000, label='rand 256KB',marker='d')
ax5.plot(rand_read_128k['file_size'],rand_read_128k['r_lat'].astype(float)*1000, label='rand 128KB',marker='v')
ax5.plot(rand_read_64k['file_size'], rand_read_64k['r_lat'].astype(float)*1000, label='rand 64KB',marker='<')
ax5.plot(rand_read_32k['file_size'], rand_read_32k['r_lat'].astype(float)*1000, label='rand 32KB',marker='^')
ax5.plot(rand_read_16k['file_size'], rand_read_16k['r_lat'].astype(float)*1000, label='rand 16KB',marker='>')
ax5.plot(rand_read_8k['file_size'], rand_read_8k['r_lat'].astype(float)*1000, label='rand 8KB',marker='o')
ax5.plot(rand_read_4k['file_size'], rand_read_4k['r_lat'].astype(float)*1000, label='rand 4KB',marker='x')
ax5.set_xlabel('file size')
ax5.set_ylabel('disk util')
ax5.legend(loc='upper left')
ax5.grid()
ax5.set_xscale('log')
ax5.set_xticks(ticks=file_size_ticks, labels=file_size_labels, rotation=40)
ax5.set_yticks(ticks=[0,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1],labels=["0%","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%"])

#plot second row 
ax6.plot(rand_read_1g['file_size'],rand_read_1g['avg_throughput'], label='rand 1GB',marker='.')
ax6.plot(rand_read_512m['file_size'],rand_read_512m['avg_throughput'], label='rand 512MB',marker='*')
ax6.plot(rand_read_256m['file_size'],rand_read_256m['avg_throughput'], label='rand 256MB',marker='1')
ax6.plot(rand_read_128m['file_size'],rand_read_128m['avg_throughput'], label='rand 128MB',marker='d')
ax6.plot(rand_read_64m['file_size'],rand_read_64m['avg_throughput'], label='rand 64MB',marker='v')
ax6.plot(rand_read_32m['file_size'], rand_read_32m['avg_throughput'], label='rand 32MB',marker='<')
ax6.plot(rand_read_16m['file_size'], rand_read_16m['avg_throughput'], label='rand 16MB',marker='^')
ax6.plot(rand_read_8m['file_size'], rand_read_8m['avg_throughput'], label='rand 8MB',marker='>')
ax6.plot(rand_read_4m['file_size'], rand_read_4m['avg_throughput'], label='rand 4MB',marker='o')
ax6.plot(rand_read_2m['file_size'], rand_read_2m['avg_throughput'], label='rand 2MB',marker='x')
# ax6.plot(df_rand_read_10k_tmpfs['file_size'],df_rand_read_10k_tmpfs['avg_throughput'], label='rand tmpfs',marker='P')
ax6.set_xlabel('file size')
ax6.set_ylabel('throughput (MB/s)')
ax6.legend(loc='upper right')
ax6.grid()
ax6.set_xscale('log')
ax6.set_xticks(ticks=file_size_ticks2, labels=file_size_labels2, rotation=40)
ax6.set_yticks(ticks=[0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500],labels=["0","100","200","300","400","500","600","700","800","900","1000","1100","1200","1300","1400","1500"])
ax6.set_ylim(bottom=0)
ax7.plot(rand_read_1g['file_size'],(rand_read_1g['user_time']+rand_read_1g['kernel_time'])/rand_read_1g['len'], label='rand 1GB',marker='.')
ax7.plot(rand_read_512m['file_size'],(rand_read_512m['user_time']+rand_read_512m['kernel_time'])/rand_read_512m['len'], label='rand 512MB',marker='*')
ax7.plot(rand_read_256m['file_size'],(rand_read_256m['user_time']+rand_read_256m['kernel_time'])/rand_read_256m['len'], label='rand 256MB',marker='1')
ax7.plot(rand_read_128m['file_size'],(rand_read_128m['user_time']+rand_read_128m['kernel_time'])/rand_read_128m['len'], label='rand 128MB',marker='d')
ax7.plot(rand_read_64m['file_size'],(rand_read_64m['user_time']+rand_read_64m['kernel_time'])/rand_read_64m['len'], label='rand 64MB',marker='v')
ax7.plot(rand_read_32m['file_size'], (rand_read_32m['user_time']+rand_read_32m['kernel_time'])/rand_read_32m['len'], label='rand 32MB',marker='<')
ax7.plot(rand_read_16m['file_size'], (rand_read_16m['user_time']+rand_read_16m['kernel_time'])/rand_read_16m['len'], label='rand 16MB',marker='^')
ax7.plot(rand_read_8m['file_size'], (rand_read_8m['user_time']+rand_read_8m['kernel_time'])/rand_read_8m['len'], label='rand 8MB',marker='>')
ax7.plot(rand_read_4m['file_size'], (rand_read_4m['user_time']+rand_read_4m['kernel_time'])/rand_read_4m['len'], label='rand 4MB',marker='o')
ax7.plot(rand_read_2m['file_size'], (rand_read_2m['user_time']+rand_read_2m['kernel_time'])/rand_read_2m['len'], label='rand 2MB',marker='x')
ax7.set_xlabel('file size')
ax7.set_ylabel('CPU')
ax7.legend(loc='upper right')
ax7.grid()
ax7.set_xscale('log')
ax7.set_yticks(ticks=[0,0.05,0.1,0.15],labels=["0%","5%","10%","15%"])
ax7.set_xticks(ticks=file_size_ticks2, labels=file_size_labels2, rotation=40)

ax8.plot(rand_read_1g['file_size'],rand_read_1g['rps'], label='rand 1GB',marker='.')
ax8.plot(rand_read_512m['file_size'],rand_read_512m['rps'], label='rand 512MB',marker='*')
ax8.plot(rand_read_256m['file_size'],rand_read_256m['rps'], label='rand 256MB',marker='1')
ax8.plot(rand_read_128m['file_size'],rand_read_128m['rps'], label='rand 128MB',marker='d')
ax8.plot(rand_read_64m['file_size'],rand_read_64m['rps'], label='rand 64MB',marker='v')
ax8.plot(rand_read_32m['file_size'], rand_read_32m['rps'], label='rand 32MB',marker='<')
ax8.plot(rand_read_16m['file_size'], rand_read_16m['rps'], label='rand 16MB',marker='^')
ax8.plot(rand_read_8m['file_size'],rand_read_8m['rps'], label='rand 8MB',marker='>')
ax8.plot(rand_read_4m['file_size'],rand_read_4m['rps'], label='rand 4MB',marker='o')
ax8.plot(rand_read_2m['file_size'],rand_read_2m['rps'], label='rand 2MB',marker='x')
ax8.set_xlabel('file size')
ax8.set_ylabel('IOps')
ax8.legend(loc='upper right')
ax8.grid()
ax8.set_xscale('log')
# ax8.set_yticks(ticks=[0,0.05,0.1,0.15,0.2,0.25,0.3],labels=["0%","5%","10%","15%","20%","25%","30%"])
ax8.set_xticks(ticks=file_size_ticks2, labels=file_size_labels2, rotation=40)

ax9.plot(rand_read_1g['file_size'],rand_read_1g['rqsz'], label='rand 1GB',marker='.')
ax9.plot(rand_read_512m['file_size'],rand_read_512m['rqsz'], label='rand 512MB',marker='*')
ax9.plot(rand_read_256m['file_size'],rand_read_256m['rqsz'], label='rand 256MB',marker='1')
ax9.plot(rand_read_128m['file_size'],rand_read_128m['rqsz'], label='rand 128MB',marker='d')
ax9.plot(rand_read_64m['file_size'],rand_read_64m['rqsz'], label='rand 64MB',marker='v')
ax9.plot(rand_read_32m['file_size'], rand_read_32m['rqsz'], label='rand 32MB',marker='<')
ax9.plot(rand_read_16m['file_size'], rand_read_16m['rqsz'], label='rand 16MB',marker='^')
ax9.plot(rand_read_8m['file_size'], rand_read_8m['rqsz'], label='rand 8MB',marker='>')
ax9.plot(rand_read_4m['file_size'], rand_read_4m['rqsz'], label='rand 4MB',marker='o')
ax9.plot(rand_read_2m['file_size'], rand_read_2m['rqsz'], label='rand 2MB',marker='x')
ax9.set_xlabel('file size')
ax9.set_ylabel('request size')
ax9.legend(loc='upper left')
ax9.grid()
ax9.set_xscale('log')
ax9.set_xticks(ticks=file_size_ticks2, labels=file_size_labels2, rotation=40)
ax9.set_yscale('log')
ax9.set_yticks(ticks=[1,2,4,8,16,32,64,128,256],labels=['1k','2k','4k','8k','16k','32k','64k','128k','256k'])
# ax9.set_yticks(ticks=[0,0.05,0.1,0.15,0.2,0.25,0.3],labels=["0%","5%","10%","15%","20%","25%","30%"])

ax10.plot(rand_read_1g['file_size'],rand_read_1g['r_lat'].astype(float)/100, label='rand 1GB',marker='.')
ax10.plot(rand_read_512m['file_size'],rand_read_512m['r_lat'].astype(float)/100, label='rand 512MB',marker='*')
ax10.plot(rand_read_256m['file_size'],rand_read_256m['r_lat'].astype(float)/100, label='rand 256MB',marker='1')
ax10.plot(rand_read_128m['file_size'],rand_read_128m['r_lat'].astype(float)/100, label='rand 128MB',marker='d')
ax10.plot(rand_read_64m['file_size'],rand_read_64m['r_lat'].astype(float)/100, label='rand 64MB',marker='v')
ax10.plot(rand_read_32m['file_size'], rand_read_32m['r_lat'].astype(float)/100, label='rand 32MB',marker='<')
ax10.plot(rand_read_16m['file_size'], rand_read_16m['r_lat'].astype(float)/100, label='rand 16MB',marker='^')
ax10.plot(rand_read_8m['file_size'], rand_read_8m['r_lat'].astype(float)/100, label='rand 8MB',marker='>')
ax10.plot(rand_read_4m['file_size'], rand_read_4m['r_lat'].astype(float)/100, label='rand 4MB',marker='o')
ax10.plot(rand_read_2m['file_size'], rand_read_2m['r_lat'].astype(float)/100, label='rand 2MB',marker='x')
ax10.set_xlabel('file size')
ax10.set_ylabel('disk util')
ax10.legend(loc='upper left')
ax10.grid()
ax10.set_xscale('log')
ax10.set_xticks(ticks=file_size_ticks2, labels=file_size_labels2, rotation=40)
ax10.set_yticks(ticks=[0,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1],labels=["0%","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%"])



plt.tight_layout()
fig.savefig('rand_bench/results_read_rand.png')

# for (df,name) in [(rand_tmpfs,'rand_tmpfs_4KB'),(seq_tmpfs,'seq_tmpfs_4KB')]:
# for (df,name) in [(seq_read_4k,'4k')]:
#     fig, ax1 = plt.subplots()
#     df['nor_usertime'] = (df['user_time'] / (df['len']/60))
#     df['nor_kerneltime'] = df['kernel_time'] / (df['len']/60)
#     df['rand_syscall_persec'] = ((df['read_syscalls'] + df['write_syscalls'])/(df['len']/60))/60
#     file_size_ticks = [4096,8192,16384,32768, 65536, 131072,262144,524288,1048576,2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]
#     file_size_ticks = file_size_ticks[-len(df):]
#     file_size_labels = ['4KB','8KB', '16KB','32KB', '64KB','128KB','256KB','512KB','1MB', '2MB', '4MB', '8MB', '16MB', '32MB', '64MB', '128MB', '256MB', '512MB', '1GB']
#     file_size_labels = file_size_labels[-len(df):]
#     print(len(df))
#     print(file_size_ticks)
#     print(file_size_labels)
#     ax1.plot(df['file_size'], df['avg_throughput'], label=f'random {name}', marker='x')
#     ax1.set_xlabel('file size')
#     ax1.set_ylabel('throughput (MB/s)')
#     ax1.set_xscale('log')
#     ax1.set_xticks(file_size_ticks)
#     ax1.set_xticklabels(file_size_labels, rotation=40)
#     # ax1.set_yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
#     # ax1.set_yticklabels(["0", "5", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "60", "65"])
#     ax1.set_ylim(bottom=0)
#     ax1.grid(True)
#     ax2 = ax1.twinx()
#     ax2.set_ylabel('seconds')
#     ax2.bar(df['file_size'], df['nor_usertime'] + df['nor_kerneltime'], label='cpu time', width=0.3 * df['file_size'], color='red',alpha=0.45)
#     ax2.bar(df['file_size'], df['nor_kerneltime'], label='kernel time', width=0.3 * df['file_size'], color='green',alpha=0.45)
#     ax2.set_xticks(file_size_ticks)
#     ax2.set_xticklabels(file_size_labels, rotation=40)
#     # ax2.set_yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5])
#     # ax2.set_yticklabels(["0","0.5", "1","1.5","2","2.5","3","3.5","4","4.5","5","5.5","6"," 6.5"])
#     ax2.set_ylim(bottom=0)
#     ax2.grid(True)
#     fig.legend(loc='upper right')
#     fig.savefig(f'{name}.png')


