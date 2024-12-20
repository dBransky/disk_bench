import subprocess
import re
import sys
import itertools

def config_system(optimizations):
    write_back = optimizations[0]
    physical_disk_cache = optimizations[1]
    read_ahead_controller = optimizations[2]
    if write_back:
        res = subprocess.run(["sudo","/opt/MegaRAID/perccli/perccli64","/c0/v239","set","wrcache=WB"], capture_output=True, text=True)
        #check the print statement has the correct value
        assert 'Success' in res.stdout and 'WB' in res.stdout
    else:
        res = subprocess.run(["sudo","/opt/MegaRAID/perccli/perccli64","/c0/v239","set","wrcache=WT"], capture_output=True, text=True)
        assert 'Success' in res.stdout and 'WT' in res.stdout
    if physical_disk_cache:
        res = subprocess.run(['sudo','/opt/MegaRAID/perccli/perccli64','/c0/v239','set','pdcache=On'], capture_output=True, text=True)
        assert 'Success' in res.stdout and 'On' in res.stdout
    else:
        res = subprocess.run(['sudo','/opt/MegaRAID/perccli/perccli64','/c0/v239','set','pdcache=Off'], capture_output=True, text=True)
        assert 'Success' in res.stdout and 'Off' in res.stdout
    if read_ahead_controller:
        res = subprocess.run(['sudo','/opt/MegaRAID/perccli/perccli64','/c0/v239','set','rdcache=RA'], capture_output=True, text=True)
        assert 'Success' in res.stdout and 'RA' in res.stdout
    else:
        res = subprocess.run(['sudo','/opt/MegaRAID/perccli/perccli64','/c0/v239','set','rdcache=NoRA'], capture_output=True, text=True)
        assert 'Success' in res.stdout and 'NoRA' in res.stdout
    return

total_latency = 0
total_throughput = 0
runs = 5
# each value in the list can be true or false and i want a permutation of all possible values
write_back = [False]
physical_disk_cache = [False,True]
read_ahead_controller = [False,True]
patterns = ['rand','seq']
operations = ['write','read']
file_size = 83886080
single_chuck = [False,True]
iterables = [write_back, physical_disk_cache, read_ahead_controller, single_chuck, patterns, operations]
permutations = list(itertools.product(*iterables))
print(permutations)
with open('results_no_WT.csv','w') as f:
    f.write('write_back,physical_disk_cache,read_ahead_controller,single_chuck,pattern,operation,avg_latency,avg_throughput\n')
for perm in permutations:
    config_system(perm)
    single_chuck = perm[3]
    pattern = perm[4]
    operation = perm[5]
    if single_chuck:
        io_size = file_size
        iterations = 1
    else:
        io_size = 4096
        iterations = file_size / io_size
    print(f'benchmarking configuration WB: {perm[0]}, pdcache: {perm[1]}, rdcache: {perm[2]}, single_chunk: {perm[3]}, pattern: {perm[4]}, operation: {perm[5]}')
    total_latency = 0
    total_throughput = 0
    for i in range(5):
        result = subprocess.run(['taskset','-c','12','./io_bench', '-i',f'{iterations}','-p', f'{pattern}', '-o', f'{operation}', '-s', f'{io_size}', '-f', f'{file_size}','-t','0'], capture_output=True, text=True,check=True)
        output = result.stdout.strip()
        print(output)
        avg_latency = re.search(r'avg latency:\s+([\d.]+)\s+ns', output)
        avg_throughput = re.search(r'avg throughput:\s+([\d.]+)\s+MB/s', output)
        if avg_latency and avg_throughput:
            total_latency += float(avg_latency.group(1))
            total_throughput += float(avg_throughput.group(1))
    if single_chuck:
        total_latency /= (file_size/4096)
        total_throughput /= (file_size/4096)
    print(f'Average latency: {total_latency/5} ns')
    print(f'Average throughput: {total_throughput/5} MB/s')
    with open('results_no_WT.csv','a') as f:
        f.write(f'{perm[0]},{perm[1]},{perm[2]},{perm[3]},{perm[4]},{perm[5]},{total_latency/5},{total_throughput/5}\n')
