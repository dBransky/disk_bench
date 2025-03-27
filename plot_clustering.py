import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
# Load CSV files
cols=['File Size','Cluster Size','Cluster Amount','Throughput','User Time','Kernel Time']
csv1 = pd.read_csv('out_rand_128G.csv')
csv2 = pd.read_csv('out_seq_128G.csv')
csv3 = pd.read_csv('out_rand_clusters_128G.csv')
csv4 = pd.read_csv('out_seq_clusters_128G.csv')
csv5 = pd.read_csv('out_seq_clusters_write_128G.csv')
for csv in [csv1, csv2, csv3, csv4, csv5]:
    csv['Throughput'] = csv['Throughput'].astype(float)
    csv['Cluster Size'] = csv['Cluster Size'].astype(float)
# Plot data
plt.figure(figsize=(5, 5))
x = np.linspace(0, 4 * 2**30, 1000000)  # 4 GiB = 4 * 2^30 bytes
epsilon = 1e-9  # To avoid division by zero at x = 0
x = x + epsilon

# Formula for y
y = (x / ((30/7200) + (x / (195*1024*1024))))/(1024*1024)
# y = (x / ((0.00466896287) + (x / (195*1024*1024))))/(1024*1024)
# Create the plot
plt.plot(x, y,label='model', linestyle='-')
# plt.plot(csv4['Cluster Size'], csv4['Throughput'], label='seq   | io=cluster size | r', linestyle='--',marker='v',fillstyle='none',markersize=12)
# plt.plot(csv3['Cluster Size'], csv3['Throughput'], label='rand | io=cluster size | r', linestyle='-',marker='x')
plt.plot(csv2['Cluster Size'], csv2['Throughput'], label='seq   | io=8 pages      | r', marker='d',linestyle='-.')
plt.plot(csv5['Cluster Size'], csv5['Throughput'], label='seq   | io=cluster size | w', linestyle='--',marker='o',fillstyle='none',markersize=12)
plt.plot(csv1['Cluster Size'], csv1['Throughput'], label='rand | io=8 pages      | r', marker='s',linestyle=':',fillstyle='none')
plt.xlabel('cluster size')
plt.ylabel('MiB/s')
plt.xscale('log')
plt.xticks([(2**i) for i in range(15,33,3)]+[2**32],['32KiB','256KiB','2MiB','16MiB','128MiB','1GiB','4GiB'])
plt.legend()
plt.grid()
plt.xlim(2**15,2**32)
plt.ylim(0)
plt.tight_layout()
plt.savefig('clustering.png')