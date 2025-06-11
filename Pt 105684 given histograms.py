import numpy as np
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 6))
fig.suptitle("Highly Peaked (Leptokurtic) Symmetric Histograms", fontsize=18, y=0.98)

# --- Common Settings ---
# We use the Laplace distribution to create a symmetric distribution that is more
# peaked than a standard bell curve (Normal distribution).
# np.random.laplace takes a mean (loc) and a scale parameter.
num_samples = 2000  # Increased samples for a clearer distribution shape
bin_count = 25      # Increased bins for a more defined peak
alpha = 0.75        # Transparency for histograms
edge_color = 'black'

# Custom colors from hex codes as provided
colors = ['#9EDAE2', '#A5CDF2', '#60B2DE', '#B6A1F5']

# --- Version 1: Sprinter Reaction Times ---
# Elite sprinters have very consistent reaction times around a mean.
loc1, scale1 = 150, 5  # Mean (loc) in ms, small scale for low variability
data1 = np.random.laplace(loc1, scale1, num_samples)
axes[0, 0].hist(data1, bins=bin_count, alpha=alpha, color=colors[0], edgecolor=edge_color)
axes[0, 0].set_title("Sprinter Reaction Times", fontsize=14)
axes[0, 0].set_xlabel("Reaction Time (ms)", fontsize=12)
axes[0, 0].set_ylabel("Frequency of Trials", fontsize=12)
axes[0, 0].grid(axis='y', alpha=0.5, linestyle='--')


# --- Version 2: Precision-Cut Washer Thickness ---
# A highly calibrated machine produces items with very little deviation from the target thickness.
loc2, scale2 = 5.0, 0.02  # Mean (loc) in mm, very small scale for high precision
data2 = np.random.laplace(loc2, scale2, num_samples)
axes[0, 1].hist(data2, bins=bin_count, alpha=alpha, color=colors[0], edgecolor=edge_color)
axes[0, 1].set_title("Precision-Cut Washer Thickness", fontsize=14)
axes[0, 1].set_xlabel("Washer Thickness (mm)", fontsize=12)
axes[0, 1].set_ylabel("Number of Washers", fontsize=12)
axes[0, 1].grid(axis='y', alpha=0.5, linestyle='--')


# --- Version 3: Server Response Times ---
# A highly optimized server shows consistent response times.
loc3, scale3 = 80, 8  # Mean (loc) in ms, small scale for consistent performance
data3 = np.random.laplace(loc3, scale3, num_samples)
axes[1, 0].hist(data3, bins=bin_count, alpha=alpha, color=colors[0], edgecolor=edge_color)
axes[1, 0].set_title("Server Response Times", fontsize=14)
axes[1, 0].set_xlabel("Server Response Time (ms)", fontsize=12)
axes[1, 0].set_ylabel("Number of Queries", fontsize=12)
axes[1, 0].grid(axis='y', alpha=0.5, linestyle='--')


# --- Version 4: Scientific Measurement Deviations ---
# Precise measurements cluster tightly around a central value, which is zero deviation.
loc4, scale4 = 0, 0.5  # Mean (loc) is 0 for deviation, small scale for high precision
data4 = np.random.laplace(loc4, scale4, num_samples)
axes[1, 1].hist(data4, bins=bin_count, alpha=alpha, color=colors[0], edgecolor=edge_color)
axes[1, 1].set_title("Scientific Measurement Deviations", fontsize=14)
axes[1, 1].set_xlabel("Measurement Deviation (units)", fontsize=12)
axes[1, 1].set_ylabel("Frequency", fontsize=12)
axes[1, 1].grid(axis='y', alpha=0.5, linestyle='--')


# Adjust layout to prevent titles from overlapping and save the figure
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("peaked_symmetric_histograms.png", dpi=300, bbox_inches='tight')
plt.show()