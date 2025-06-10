import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon, pareto

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("J-Shaped and Reverse J-Shaped Histograms", fontsize=16)

# Common settings for all histograms
num_samples = 2000
bin_count = 25
alpha = 0.75  # Transparency for histograms
curve_color = 'black'  # Color for the curves

# Custom colors from hex codes
colors = ['#838EF0', '#19C9D6', '#FAC88C', '#E69BA6']

# --- Version 1: Word Frequency (Forward J-shape) ---
scale1 = 1.5
data1 = np.random.exponential(scale=scale1, size=num_samples)
counts1, bins1, _ = axes[0, 0].hist(data1, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
x1 = np.linspace(0, bins1[-1], 1000)
pdf1 = expon.pdf(x1, scale=scale1) * num_samples * (bins1[1] - bins1[0])
axes[0, 0].plot(x1, pdf1, color=curve_color, linewidth=2)
axes[0, 0].set_title("Word Frequency (Forward J-shape)")
axes[0, 0].set_xlabel("Word Rarity (Higher value is more rare)")
axes[0, 0].set_ylabel("Frequency")
axes[0, 0].set_xlim(left=0)
axes[0, 0].set_ylim(bottom=0, top=max(counts1)*1.1)

# --- Version 2: Software Faults (Reverse J-shape) ---
max_faults = 60
scale2 = 10
flipped_data2 = np.random.exponential(scale=scale2, size=num_samples)
data2 = max_faults - flipped_data2
data2 = np.clip(data2, 0, max_faults)
counts2, bins2, _ = axes[0, 1].hist(data2, bins=bin_count, alpha=alpha, color=colors[1], edgecolor='black')
x2 = np.linspace(0, max_faults, 1000)
pdf2 = expon.pdf(max_faults - x2, scale=scale2) * num_samples * (bins2[1] - bins2[0])
axes[0, 1].plot(x2, pdf2, color=curve_color, linewidth=2)
axes[0, 1].set_title("Software Faults (Reverse J-shape)")
axes[0, 1].set_xlabel("Faults per Module")
axes[0, 1].set_ylabel("Number of Modules")
axes[0, 1].set_ylim(bottom=0, top=max(counts2)*1.1)

# --- Version 3: Wealth Distribution (Forward J-shape) ---
a = 1.5  # Shape parameter for Pareto
scale3 = 1e5
clip_max = 2e6
data3 = np.random.pareto(a, num_samples) * scale3
data3 = np.clip(data3, 0, clip_max)
counts3, bins3, _ = axes[1, 0].hist(data3, bins=bin_count, alpha=alpha, color=colors[2], edgecolor='black')
x3 = np.linspace(0, clip_max, 1000)
pdf3 = pareto.pdf(x3/scale3, b=a) * num_samples * (bins3[1] - bins3[0]) / scale3
pdf3[x3 > clip_max] = 0
axes[1, 0].plot(x3, pdf3, color=curve_color, linewidth=2)
axes[1, 0].set_title("Wealth Distribution (Forward J-shape)")
axes[1, 0].set_xlabel("Wealth ($)")
axes[1, 0].set_ylabel("Number of Individuals")
axes[1, 0].set_xlim(left=0)
axes[1, 0].set_ylim(bottom=0, top=max(counts3)*1.1)

# --- Version 4: Customer Service Time (Reverse J-shape) ---
max_service_time = 20
scale4 = 5
flipped_data4 = np.random.exponential(scale=scale4, size=num_samples)
data4 = max_service_time - flipped_data4
data4 = np.clip(data4, 0, max_service_time)
counts4, bins4, _ = axes[1, 1].hist(data4, bins=bin_count, alpha=alpha, color=colors[3], edgecolor='black')
x4 = np.linspace(0, max_service_time, 1000)
pdf4 = expon.pdf(max_service_time - x4, scale=scale4) * num_samples * (bins4[1] - bins4[0])
axes[1, 1].plot(x4, pdf4, color=curve_color, linewidth=2)
axes[1, 1].set_title("Customer Service Time (Reverse J-shape)")
axes[1, 1].set_xlabel("Service Time (minutes)")
axes[1, 1].set_ylabel("Number of Customers")
axes[1, 1].set_ylim(bottom=0, top=max(counts4)*1.1)

# Adjust layout to prevent titles and labels from overlapping
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save the figure to a file
plt.savefig("j_shaped_histograms_with_curves.png", dpi=300, bbox_inches='tight')

# Display the plot
plt.show()