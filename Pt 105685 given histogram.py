import numpy as np
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 6))
fig.suptitle("Histograms with Subtle Positive Skew for Problem Templates", fontsize=16)

# Common settings for all histograms
num_samples = 1000
bin_count = 20  # Increased slightly for better resolution of the skew
alpha = 0.75 # Transparency for histograms

# To create a subtle positive skew, we use the Gamma distribution.
# A larger 'shape' parameter makes the distribution more symmetric (less skewed).
subtle_skew_shape = 15 

# Custom colors from hex codes
colors = ['#9EDAE2', '#A5CDF2', '#60B2DE', '#B6A1F5']

# --- Version 1: Student Test Scores ---
# Mean score ~ 80. Mean of Gamma is shape * scale. So, scale = 80 / 15 = 5.33
scale1 = 5.33
data1 = np.random.gamma(shape=subtle_skew_shape, scale=scale1, size=num_samples)
# Clip data to be within a realistic range (e.g., 0-100)
data1 = np.clip(data1, 0, 100)
axes[0, 0].hist(data1, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
axes[0, 0].set_title("Student Test Scores")
axes[0, 0].set_xlabel("Score (out of 100)")
axes[0, 0].set_ylabel("Frequency")

# --- Version 2: Daily Coffee Shop Customers ---
# Mean customers ~ 120. scale = 120 / 15 = 8
scale2 = 8
data2 = np.random.gamma(shape=subtle_skew_shape, scale=scale2, size=num_samples)
axes[0, 1].hist(data2, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
axes[0, 1].set_title("Daily Coffee Shop Customers")
axes[0, 1].set_xlabel("Number of Customers")
axes[0, 1].set_ylabel("Frequency")

# --- Version 3: Duration of Customer Service Calls ---
# Mean duration ~ 5 minutes. scale = 5 / 15 = 0.33
scale3 = 0.33
data3 = np.random.gamma(shape=subtle_skew_shape, scale=scale3, size=num_samples)
axes[1, 0].hist(data3, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
axes[1, 0].set_title("Duration of Customer Service Calls")
axes[1, 0].set_xlabel("Duration (minutes)")
axes[1, 0].set_ylabel("Frequency")

# --- Version 4: Commute Times to Work ---
# Mean commute ~ 25 minutes. scale = 25 / 15 = 1.67
scale4 = 1.67
data4 = np.random.gamma(shape=subtle_skew_shape, scale=scale4, size=num_samples)
axes[1, 1].hist(data4, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
axes[1, 1].set_title("Commute Times to Work")
axes[1, 1].set_xlabel("Commute Time (minutes)")
axes[1, 1].set_ylabel("Frequency")

# Adjust layout to prevent titles and labels from overlapping
plt.tight_layout(rect=[0, 0, 1, 0.96]) # Adjust rect to make space for suptitle
plt.show()