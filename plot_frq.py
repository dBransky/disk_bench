import matplotlib.pyplot as plt
import numpy as np

# Read the data from the file
file_path = '/csl/daniel.br/swap_proj/disk_bench/out.1m'
with open(file_path, 'r') as file:
    data = [int(line.strip()) for line in file]

# Convert data to a numpy array for easier manipulation
data = np.array(data)

# Calculate the IQR to identify outliers
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1

# Define a threshold to identify spikes (e.g., 1.5 times the IQR)
threshold = 1.5 * IQR

# Filter out spikes
filtered_data = data[(data >= Q1 - threshold) & (data <= Q3 + threshold)]

# Plot the filtered data
plt.figure(figsize=(10, 6))
plt.plot(filtered_data/1000,  linestyle='-', color='b')
plt.xlabel('iteration')
plt.ylabel('latency µs')
plt.grid(True)
plt.savefig('reads_freq_1m_filtered.png')