import matplotlib.pyplot as plt
import pandas as pd

rand_read = 'io_bench_results_rand_read.csv'
seq_read = 'io_bench_results_seq_read.csv'
seq_read_cached = 'io_bench_results_seq_read_cached.csv'
headers = ['file_size', 'avg_throughput']
headers_rand = ['file_size','warmup_throughput','avg_throughput']
df_rand_read = pd.read_csv(rand_read,header=None,names=headers_rand)
df_seq_read = pd.read_csv(seq_read,header=None,names=headers_rand)
df_seq_read_cached = pd.read_csv(seq_read_cached,header=None,names=headers_rand)
df_rand_read['avg_throughput'] = df_rand_read['avg_throughput']*1000000
df_rand_read['warmup_throughput'] = df_rand_read['warmup_throughput']*1000000
df_rand_read['run_time'] = (df_rand_read['file_size']*5)/df_rand_read['avg_throughput']
df_rand_read['warmup_time'] = (df_rand_read['file_size'])/df_rand_read['warmup_throughput']
df_rand_read['bytes_read'] = df_rand_read['file_size']*5
df_rand_read['normalized_throughput'] = (df_rand_read['bytes_read']-df_rand_read['file_size'])/(df_rand_read['run_time']-df_rand_read['warmup_time'])
df_rand_read['avg_throughput'] = df_rand_read['avg_throughput']/1000000
df_rand_read['warmup_throughput'] = df_rand_read['warmup_throughput']/1000000
df_rand_read['normalized_throughput'] = df_rand_read['normalized_throughput']/1000000

fig = plt.figure()
# from 4k to 1GB
file_size_ticks = [4096,8192,16384,32768, 65536, 131072,262144,524288,1048576,2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]
file_size_labels = ['4KB','8KB', '16KB','32KB', '64KB','256KB','128KB', '512KB','1MB', '2MB', '4MB', '8MB', '16MB', '32MB', '64MB', '128MB', '256MB', '512MB', '1GB']
# plot all three columds, x axis is sizeds, y axis is throughput
plt.plot(df_rand_read['file_size'], df_rand_read['warmup_throughput'], label='random',marker='o')
plt.plot(df_rand_read['file_size'], df_rand_read['normalized_throughput'], label='normalized random',marker='d')
plt.plot(df_seq_read['file_size'], df_seq_read['avg_throughput'], label='sequential no cache',marker='x')
plt.plot(df_seq_read_cached['file_size'],df_seq_read_cached['avg_throughput'], label='sequential cached',marker='s')
# x label is the arry file_size_labels
plt.xlabel('file size')
plt.ylabel('throughput (MB/s)')
plt.legend(loc='upper left')
plt.grid()
# make x axis logarithmic
plt.xscale('log')
plt.xticks(ticks=file_size_ticks, labels=file_size_labels, rotation=40)
plt.yticks(ticks=range(0, 210, 10))
plt.ylim(0, 200)
plt.tight_layout()
fig.savefig('io_bench_results_read.png')


df_seq_write_s = pd.read_csv('io_bench_results_seq_write_single.csv',header=None,names=headers_rand)
df_rand_write = pd.read_csv('io_bench_results_seq_write.csv',header=None,names=headers)
missing_file_sizes = set(df_seq_write_s['file_size']) - set(df_rand_write['file_size'])
for file_size in missing_file_sizes:
    avg_throughput = df_rand_write[df_rand_write['file_size'] < file_size]['avg_throughput'].mean()
    new_row = pd.DataFrame({'file_size': [file_size], 'avg_throughput': [avg_throughput]})
    df_rand_write = pd.concat([df_rand_write, new_row], ignore_index=True)
# Sort df_rand_write by file_size
df_rand_write = df_rand_write.sort_values(by='file_size').reset_index(drop=True)
fig = plt.figure()
# from 4k to 1GB
file_size_ticks = [4096,8192,16384,32768, 65536, 131072,262144,524288,1048576,2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296, 8589934592, 17179869184]
file_size_labels = ['4KB','8KB', '16KB','32KB', '64KB','256KB','128KB', '512KB','1MB', '2MB', '4MB', '8MB', '16MB', '32MB', '64MB', '128MB', '256MB', '512MB', '1GB','2GB','4GB','8GB','16GB']
# plot all three columds, x axis is sizeds, y axis is throughput
plt.plot(df_seq_write_s['file_size'], df_seq_write_s['avg_throughput'], label='sequential single chunk',marker='x')
plt.plot(df_rand_write['file_size'], df_rand_write['avg_throughput'], label='random',marker='o')
plt.axvline(x=2147483648, color='red', linestyle='--')
# x label is the arry file_size_labels
plt.xlabel('file size')
plt.ylabel('throughput (MB/s)')
plt.legend(loc='upper left')
plt.grid()
# make x axis logarithmic
plt.xscale('log')
plt.xticks(ticks=file_size_ticks, labels=file_size_labels, rotation=50)
plt.yticks(ticks=range(0, 220, 10))
plt.ylim(0, 210)
plt.text(2147483648, 210, 'max single I/O', color='red', ha='center', va='bottom')
plt.tight_layout()
fig.savefig('io_bench_results_write.png')