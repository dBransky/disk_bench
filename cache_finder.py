import subprocess
import csv
import re
import matplotlib.pyplot as plt

# Function to run io_bench and collect output
def run_io_bench(filesize):
    result = subprocess.run(['./io_bench', '-i',f'{(filesize/4096)}','-n', f'/tmp/tempfile.{filesize}','-o','write'], capture_output=True, text=True)
    output = result.stdout.strip()
    print(output)
    avg_throughput = float(re.search(r'total throughput:\s+([\d.]+)\s+MB/s', output).group(1))
    print(f'Average throughput: {avg_throughput}')
    return avg_throughput

data = []
basic_file_size = 4096
for exp in range(0,19):
    file_size = basic_file_size * 2**exp
    total_throughput = 0
    execs = 1
    for i in range(execs):
        print(f'Running io_bench for file size {file_size} for the {i+1}th time')
        output = run_io_bench(file_size)
        if output:
            total_throughput += output
    throughput =  total_throughput / execs
    print(f'Average throughput for file size {file_size}: {throughput}')
    data.append([file_size, throughput])
# Write data to CSV
    csv_file = 'io_bench_results_seq_write.csv'
    with open(csv_file, 'a', newline='') as file:
        file.write(f'{file_size},{throughput}\n')

# Read data from CSV and plot
csv_file = 'io_bench_results_seq_write.csv'
filesizes = []
throughputs = []
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        filesizes.append(float(row[0]))
        throughputs.append(float(row[-1])*1000)

fig = plt.figure()

color = 'tab:blue'
plt.set_xlabel('file size')
plt.legend(loc='upper left')
file_size_ticks = [
262144,
1048576,
4194304,
33554432,
134217728,
268435456,
536870912,
1073741824,
]
file_size_labels = ['256KB', '1MB', '4MB', '32MB', '128MB','256MB', '512MB', '1GB']

color = 'tab:red'
plt.set_ylabel('throughput (KB/s)')  # we already handled the x-label with ax1
plt.plot(filesizes, throughputs, label='throughput', color=color)
plt.set_yticks([50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000])
plt.grid()
plt.show()
plt.savefig('io_bench_results_read_rand.png')