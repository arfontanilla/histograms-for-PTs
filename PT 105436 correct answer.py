import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Symmetric Bell-Shaped Histograms with Correct Normal Curves", fontsize=16)

# Common settings for all histograms
num_samples = 1000
bin_count = 15
alpha = 0.7  # Transparency for histograms
curve_color = 'black'
linewidth = 2

# Custom colors from hex codes
colors = ['#98A4AE']

# Generate x values for curves
x_range_multiplier = 3  # How many standard deviations to show

# --- Version 1: Measurement Errors ---
mu1, sigma1 = 0, 1  # Mean and standard deviation
data1 = np.random.normal(mu1, sigma1, num_samples)
x1 = np.linspace(mu1 - x_range_multiplier*sigma1, mu1 + x_range_multiplier*sigma1, 500)
#counts1, bins1, _ = axes[0, 0].hist(data1, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
# Scale the normal curve to match histogram counts
scale_factor1 = counts1.max() / norm.pdf(mu1, mu1, sigma1)
normal_curve1 = norm.pdf(x1, mu1, sigma1) * scale_factor1
axes[0, 0].plot(x1, normal_curve1, color=curve_color, linewidth=linewidth)
axes[0, 0].set_title("Measurement Errors (mm)")
axes[0, 0].set_xlabel("Error (mm)")
axes[0, 0].set_ylabel("Frequency")

# --- Version 2: Heights of Adults ---
mu2, sigma2 = 170, 8  # Mean and standard deviation
data2 = np.random.normal(mu2, sigma2, num_samples)
x2 = np.linspace(mu2 - x_range_multiplier*sigma2, mu2 + x_range_multiplier*sigma2, 500)
#counts2, bins2, _ = axes[0, 1].hist(data2, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
scale_factor2 = counts2.max() / norm.pdf(mu2, mu2, sigma2)
normal_curve2 = norm.pdf(x2, mu2, sigma2) * scale_factor2
axes[0, 1].plot(x2, normal_curve2, color=curve_color, linewidth=linewidth)
axes[0, 1].set_title("Heights of Adults (cm)")
axes[0, 1].set_xlabel("Height (cm)")
axes[0, 1].set_ylabel("Frequency")

# --- Version 3: Weights of Manufactured Products ---
mu3, sigma3 = 500, 20  # Mean and standard deviation
data3 = np.random.normal(mu3, sigma3, num_samples)
x3 = np.linspace(mu3 - x_range_multiplier*sigma3, mu3 + x_range_multiplier*sigma3, 500)
#counts3, bins3, _ = axes[1, 0].hist(data3, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
scale_factor3 = counts3.max() / norm.pdf(mu3, mu3, sigma3)
normal_curve3 = norm.pdf(x3, mu3, sigma3) * scale_factor3
axes[1, 0].plot(x3, normal_curve3, color=curve_color, linewidth=linewidth)
axes[1, 0].set_title("Weights of Products (g)")
axes[1, 0].set_xlabel("Weight (g)")
axes[1, 0].set_ylabel("Frequency")

# --- Version 4: Test Scores ---
mu4, sigma4 = 75, 10  # Mean and standard deviation
data4 = np.random.normal(mu4, sigma4, num_samples)
x4 = np.linspace(mu4 - x_range_multiplier*sigma4, mu4 + x_range_multiplier*sigma4, 500)
#counts4, bins4, _ = axes[1, 1].hist(data4, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
scale_factor4 = counts4.max() / norm.pdf(mu4, mu4, sigma4)
normal_curve4 = norm.pdf(x4, mu4, sigma4) * scale_factor4
axes[1, 1].plot(x4, normal_curve4, color=curve_color, linewidth=linewidth)
axes[1, 1].set_title("Test Scores (out of 100)")
axes[1, 1].set_xlabel("Score")
axes[1, 1].set_ylabel("Frequency")

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("bell_shaped_histograms_with_normal_curves.png", dpi=300, bbox_inches='tight')
plt.show()