import subprocess
import csv
import re
import matplotlib.pyplot as plt
import os
import math
import pandas as pd


def run_io_bench(filesize,io_size,epochs,file_name,length,cluster_size,cluster_amount,test):
    print('cleaning up caches')
    subprocess.run(['./io_bench', '-i','262144','-n', '/tmp/tempfile.1073741824'], capture_output=True, text=True)
    os.system('sudo sync')
    os.system('echo 3 | sudo tee /proc/sys/vm/drop_caches')
    print('starting io_bench')
    result = subprocess.run(['sudo','./io_bench', '-i',f'{epochs*(filesize/io_size)}','-n', f'/scratch/{file_name}','-o','read','-p',test,'-s',f'{io_size}','-l',f'{length}','-c',f'{cluster_size}','-a',f'{cluster_amount}'],capture_output=True, text=True)
    output = result.stdout.strip()
    print(output)
    # warmup_throughput = float(re.search(r'warm up throughput:\s+([\d.]+)\s+MB/s', output).group(1))
    avg_throughput = float(re.search(r'total throughput:\s+([\d.]+)\s+MB/s', output).group(1))
    # print(f'warmup throughput: {warmup_throughput}')
    print(f'Average throughput: {avg_throughput}')
    # parse the last line of the output to a list of strings
    last_line = output.split('\n')[-1]
    last_line = last_line.split()
    print(*last_line)
    print(last_line[1])
    assert last_line[1] == "(io_bench)"
    user_time = float(last_line[13])/ os.sysconf('SC_CLK_TCK')
    kernel_time = float(last_line[14]) / os.sysconf('SC_CLK_TCK')
    print(f'User time: {user_time}')
    print(f'Kernel time: {kernel_time}')
    read_syscalls = int(re.search(r'syscr:\s+(\d+)', output).group(1))
    print(f'Number of read syscalls: {read_syscalls}')
    write_syscalls = int(re.search(r'syscw:\s+(\d+)', output).group(1))
    return avg_throughput,user_time,kernel_time,read_syscalls,write_syscalls
total_memory=2**32
file_name = 'tempfile.128G'
test = 'seq'
epochs = 1
length = 60
filesize =128*(2**30)
cluster_amount = 1
clusters_sizes = [4*2**20,8*2**20,32*2**20,64*2**20]
# clusters_sizes = [2**21]
execs = 3
data = []
# with open(f'out_{test}_clusters_write_128G.csv', 'w', newline='') as file:
#     file.write(f'File Size,Cluster Size,Cluster Amount,Throughput,User Time,Kernel Time\n')
for cluster_size in clusters_sizes:
    io_size = 8*4096
    cluster_amount = total_memory/cluster_size
    print(f'Cluster size: {cluster_size}')
    print(f'Cluster amount: {cluster_amount}')
    total_throughput = 0
    total_utime = 0
    total_ktime = 0
    for i in range(execs):
        print(f'Execution {i+1}')
        avg_throughput,user_time,kernel_time,read_syscalls,write_syscalls = run_io_bench(filesize,io_size,epochs,file_name,length,cluster_size,cluster_amount,test)
        total_throughput += avg_throughput
        total_utime += user_time
        total_ktime += kernel_time
    throughput=total_throughput/execs
    utime = total_utime/execs
    ktime = total_ktime/execs
    # Write data to CSV
    csv_file = f'out_{test}_128G.csv'
    with open(csv_file, 'a', newline='') as file:
        file.write(f'{filesize},{cluster_size},{cluster_amount},{throughput},{utime},{ktime}\n')