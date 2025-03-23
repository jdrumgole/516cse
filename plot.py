import numpy as np
import matplotlib.pyplot as plt

p_values = np.array([.01, .05, .1, .15, .2, .25, .3, .35, .4, .45, .5, .55, .6, .65, .7, .75])
N_values = [1, 2, 3, 4, 5]

throughput_results = {}
for N in N_values:
    S_values = N * p_values * ((1 - p_values) ** (2 * (N - 1)))
    throughput_results[N] = S_values

for N in N_values:
    plt.figure()
    plt.plot(p_values, throughput_results[N], marker='o')
    plt.title(f"Throughput vs Probability for N = {N}")
    plt.xlabel("Probability (p)")
    plt.ylabel("Throughput (S)")
    plt.grid(True)
    plt.savefig(f"Throughput_N{N}.png")

max_throughput_info = {N: (p_values[np.argmax(S)], np.max(S)) for N, S in throughput_results.items()}
print(max_throughput_info)
