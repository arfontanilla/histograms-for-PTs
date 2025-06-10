import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("J-Shaped Histograms with Incorrect Bell Curve Fit", fontsize=16)

# Common settings for all histograms
num_samples = 2000
bin_count = 25
alpha = 0.75  # Transparency for histograms
curve_color = 'black'
curve_linewidth = 2.5

# Custom colors from hex codes
colors = ['#838EF0', '#19C9D6', '#FAC88C', '#E69BA6']

# --- Version 1: Word Frequency (Forward J-shape) ---
data1 = np.random.exponential(scale=1.5, size=num_samples)
counts, bin_edges, _ = axes[0, 0].hist(data1, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
axes[0, 0].set_title("Word Frequency (Forward J-shape)")
axes[0, 0].set_xlabel("Word Rarity (Higher value is more rare)")
axes[0, 0].set_ylabel("Frequency")
axes[0, 0].set_xlim(left=0)

# Create and plot the incorrect bell curve
bin_width1 = bin_edges[1] - bin_edges[0]
mu1 = np.mean(bin_edges)  # Center the curve in the middle of the x-axis
sigma1 = np.std(bin_edges) / 1.5 # Adjust std dev to look good
x_smooth1 = np.linspace(bin_edges[0], bin_edges[-1], 500)
pdf1 = norm.pdf(x_smooth1, loc=mu1, scale=sigma1)
axes[0, 0].plot(x_smooth1, pdf1 * num_samples * bin_width1, color=curve_color, linewidth=curve_linewidth)

# --- Version 2: Software Faults (Reverse J-shape) ---
max_faults = 60
flipped_data2 = np.random.exponential(scale=10, size=num_samples)
data2 = max_faults - flipped_data2
data2 = np.clip(data2, 0, max_faults)

counts, bin_edges, _ = axes[0, 1].hist(data2, bins=bin_count, alpha=alpha, color=colors[1], edgecolor='black')
axes[0, 1].set_title("Software Faults (Reverse J-shape)")
axes[0, 1].set_xlabel("Faults per Module")
axes[0, 1].set_ylabel("Number of Modules")

# Create and plot the incorrect bell curve
bin_width2 = bin_edges[1] - bin_edges[0]
mu2 = max_faults / 2  # Center the curve
sigma2 = max_faults / 5 # Set a reasonable width
x_smooth2 = np.linspace(bin_edges[0], bin_edges[-1], 500)
pdf2 = norm.pdf(x_smooth2, loc=mu2, scale=sigma2)
axes[0, 1].plot(x_smooth2, pdf2 * num_samples * bin_width2, color=curve_color, linewidth=curve_linewidth)

# --- Version 3: Wealth Distribution (Forward J-shape) ---
a = 1.5
data3 = np.random.pareto(a, num_samples) * 1e5
data3_clipped = np.clip(data3, 0, 2e6)

counts, bin_edges, _ = axes[1, 0].hist(data3_clipped, bins=bin_count, alpha=alpha, color=colors[2], edgecolor='black')
axes[1, 0].set_title("Wealth Distribution (Forward J-shape)")
axes[1, 0].set_xlabel("Wealth ($)")
axes[1, 0].set_ylabel("Number of Individuals")
axes[1, 0].set_xlim(left=0, right=2e6)

# Create and plot the incorrect bell curve
bin_width3 = bin_edges[1] - bin_edges[0]
mu3 = 1e6 # Center at 1 million
sigma3 = 0.4e6 # Set a reasonable width
x_smooth3 = np.linspace(bin_edges[0], bin_edges[-1], 500)
pdf3 = norm.pdf(x_smooth3, loc=mu3, scale=sigma3)
axes[1, 0].plot(x_smooth3, pdf3 * num_samples * bin_width3, color=curve_color, linewidth=curve_linewidth)

# --- Version 4: Customer Service Time (Reverse J-shape) ---
max_service_time = 20
flipped_data4 = np.random.exponential(scale=5, size=num_samples)
data4 = max_service_time - flipped_data4
data4 = np.clip(data4, 0, max_service_time)

counts, bin_edges, _ = axes[1, 1].hist(data4, bins=bin_count, alpha=alpha, color=colors[3], edgecolor='black')
axes[1, 1].set_title("Customer Service Time (Reverse J-shape)")
axes[1, 1].set_xlabel("Service Time (minutes)")
axes[1, 1].set_ylabel("Number of Customers")

# Create and plot the incorrect bell curve
bin_width4 = bin_edges[1] - bin_edges[0]
mu4 = max_service_time / 2 # Center the curve
sigma4 = max_service_time / 5 # Set a reasonable width
x_smooth4 = np.linspace(bin_edges[0], bin_edges[-1], 500)
pdf4 = norm.pdf(x_smooth4, loc=mu4, scale=sigma4)
axes[1, 1].plot(x_smooth4, pdf4 * num_samples * bin_width4, color=curve_color, linewidth=curve_linewidth)

# Adjust layout to prevent titles and labels from overlapping
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save the figure to a file
plt.savefig("j_shaped_histograms_with_incorrect_bell_curves.png", dpi=300, bbox_inches='tight')

# Display the plot
plt.show()