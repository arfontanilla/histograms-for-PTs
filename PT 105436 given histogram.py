import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Symmetric Bell-Shaped Histograms for Problem Templates", fontsize=16)

# Common settings for all histograms
num_samples = 1000
bin_count = 15
alpha = 0.7  # Transparency for histograms

# Custom colors from hex codes
colors = ['#838EF0', '#60B2DE', '#19C9D6', '#03A28D']

# --- Version 1: Measurement Errors ---
mu1, sigma1 = 0, 1  # Mean and standard deviation
data1 = np.random.normal(mu1, sigma1, num_samples)
axes[0, 0].hist(data1, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
axes[0, 0].set_title("Measurement Errors (mm)")
axes[0, 0].set_xlabel("Error (mm)")
axes[0, 0].set_ylabel("Frequency")

# --- Version 2: Heights of Adults ---
mu2, sigma2 = 170, 8  # Mean and standard deviation
data2 = np.random.normal(mu2, sigma2, num_samples)
axes[0, 1].hist(data2, bins=bin_count, alpha=alpha, color=colors[1], edgecolor='black')
axes[0, 1].set_title("Heights of Adults (cm)")
axes[0, 1].set_xlabel("Height (cm)")
axes[0, 1].set_ylabel("Frequency")

# --- Version 3: Weights of Manufactured Products ---
mu3, sigma3 = 500, 20  # Mean and standard deviation
data3 = np.random.normal(mu3, sigma3, num_samples)
axes[1, 0].hist(data3, bins=bin_count, alpha=alpha, color=colors[2], edgecolor='black')
axes[1, 0].set_title("Weights of Products (g)")
axes[1, 0].set_xlabel("Weight (g)")
axes[1, 0].set_ylabel("Frequency")

# --- Version 4: Test Scores ---
mu4, sigma4 = 75, 10  # Mean and standard deviation
data4 = np.random.normal(mu4, sigma4, num_samples)
axes[1, 1].hist(data4, bins=bin_count, alpha=alpha, color=colors[3], edgecolor='black')
axes[1, 1].set_title("Test Scores (out of 100)")
axes[1, 1].set_xlabel("Score")
axes[1, 1].set_ylabel("Frequency")

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("bell_shaped_histograms.png", dpi=300, bbox_inches='tight')
plt.show()