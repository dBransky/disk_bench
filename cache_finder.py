import subprocess
import csv
import re
import matplotlib.pyplot as plt
import os
import math
import pandas as pd
import io
# Function to run io_bench and collect output
epochs = 10000000 
test = 'seq'
execs = 1
len = 60
def run_io_bench(filesize,io_size):
    subprocess.run(['./io_bench', '-i','262144','-n', '/tmp/tempfile.1073741824'], capture_output=True, text=True)
    os.system('sudo sync')
    os.system('echo 3 | sudo tee /proc/sys/vm/drop_caches')
    # os.system(f'dd if=/dev/urandom of=/scratch/tmp/tempfile.{filesize} bs={filesize} count=1 oflag=direct')
    iostat = subprocess.Popen(["iostat","-p","sda2","-x","1","-d"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = subprocess.run(['sudo','./io_bench', '-i',f'{(file_size/io_size)*epochs}','-n', f'/tmp/tempfile.{filesize}','-o','read','-p',test,'-s',f'{io_size}','-l',f'{len}'],capture_output=True, text=True)
    iostat.terminate()
    iostat.wait()
    stdout, stderr = iostat.communicate()
    output = stdout.decode('utf-8')
    lines = output.strip().split("\n")
    def filter_function(line):
        return "sda2" in line  # Filter condition (modify as per your need)
    filtered_lines = [line for line in lines if filter_function(line)]
    data = [line.split() for line in filtered_lines]
    df = pd.DataFrame(data, columns=["Device", "r/s","rkB/s","rrqm/s","prec_rrqm","r_await","rareq-sz","w/s","wkB/s","wrqm/s","prec_wrqm","w_await","wareq-sz","d/s","dkB/s","drqm/s","prec_drqm","d_await","dareq-sz","f/s","f_await","aqu-sz","prec_util"])
    rps = df['r/s'].iloc[1:-1].astype(float).mean()
    rqsz = df['rareq-sz'].iloc[1:-1].astype(float).mean()
    r_lat = df['r_await'].iloc[1:-1].astype(float).mean()
    output = result.stdout.strip()
    print(output)
    warmup_throughput = float(re.search(r'warm up throughput:\s+([\d.]+)\s+MB/s', output).group(1))
    avg_throughput = float(re.search(r'total throughput:\s+([\d.]+)\s+MB/s', output).group(1))
    print(f'warmup throughput: {warmup_throughput}')
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
    return warmup_throughput,avg_throughput,user_time,kernel_time,read_syscalls,write_syscalls,rps,rqsz,r_lat

data = []
basic_file_size = 4096
io_size_multi = 4
for i in range(0,8):
    for exp in range(7,14):
        file_size = basic_file_size * 2**exp
        total_throughput = 0
        total_warmup = 0
        total_utime = 0
        total_ktime = 0
        total_read_syscalls = 0
        total_write_syscalls = 0
        total_rps = 0
        total_rqsz = 0
        total_rlat = 0
        for i in range(execs):
            print(f'Running io_bench for file size {file_size} for the {i+1}th time')
            try:
                warmup,avg,utime,ktime,read_syscalls,write_syscalls,rps,rqsz,r_lat = run_io_bench(file_size,basic_file_size*io_size_multi)
            except Exception:
                print(f'failing with io:{io_size_multi},{file}:file_size')
            # while(True):
            #     if warmup < 10:
            #         break
            if warmup and avg:
                total_throughput += avg
                total_warmup += warmup
                total_utime += utime
                total_ktime += ktime
                total_read_syscalls += read_syscalls
                total_write_syscalls += write_syscalls
                total_rps += rps
                total_rqsz += rqsz
                total_rlat += r_lat
        throughput =  total_throughput / execs
        warmup = total_warmup / execs
        utime = total_utime / execs
        ktime = total_ktime / execs
        read_syscalls = total_read_syscalls / execs
        write_syscalls = total_write_syscalls / execs
        rps = total_rps/execs
        rqsz = total_rqsz/execs
        r_lat = total_rlat/execs
        print(f'Average warmup for file size {file_size}: {warmup}')
        print(f'Average throughput for file size {file_size}: {throughput}')
        print(f'Average user time for file size {file_size}: {utime}')
        print(f'Average kernel time for file size {file_size}: {ktime}')
        print(f'Average read syscalls for file size {file_size}: {read_syscalls}')
        print(f'Average write syscalls for file size {file_size}: {write_syscalls}')
        data.append([file_size, warmup,throughput,utime,ktime,read_syscalls,write_syscalls])
    # Write data to CSV
        csv_file = f'{test}_bench/io_bench_results_{test}_read_{io_size_multi*4}k_60_sec.csv'
        with open(csv_file, 'a', newline='') as file:
            file.write(f'{file_size},{warmup},{throughput},{utime},{ktime},{read_syscalls},{write_syscalls},{rps},{rqsz},{r_lat},{len}\n')
    io_size_multi *= 2


