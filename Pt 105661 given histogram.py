import numpy as np
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("J-Shaped and Reverse J-Shaped Histograms", fontsize=16)

# Common settings for all histograms
num_samples = 2000
bin_count = 25
alpha = 0.75  # Transparency for histograms

# Custom colors from hex codes
colors = ['#838EF0', '#19C9D6', '#FAC88C', '#E69BA6']

# --- Version 1: Word Frequency (Forward J-shape) ---
# Most words are rare, a few are very common.
# The exponential distribution models this well (high frequency at low values).
data1 = np.random.exponential(scale=1.5, size=num_samples)
axes[0, 0].hist(data1, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
axes[0, 0].set_title("Word Frequency (Forward J-shape)")
axes[0, 0].set_xlabel("Word Rarity (Higher value is more rare)")
axes[0, 0].set_ylabel("Frequency")
axes[0, 0].set_xlim(left=0) # Ensure the plot starts at 0

# --- Version 2: Software Faults (Reverse J-shape) ---
# Most modules have many faults, few have none.
# We flip an exponential distribution to create this shape.
max_faults = 60
flipped_data2 = np.random.exponential(scale=10, size=num_samples)
data2 = max_faults - flipped_data2 # Flip the data
data2 = np.clip(data2, 0, max_faults) # Keep data within the [0, max_faults] range

axes[0, 1].hist(data2, bins=bin_count, alpha=alpha, color=colors[1], edgecolor='black')
axes[0, 1].set_title("Software Faults (Reverse J-shape)")
axes[0, 1].set_xlabel("Faults per Module")
axes[0, 1].set_ylabel("Number of Modules")

# --- Version 3: Wealth Distribution (Forward J-shape) ---
# The Pareto distribution is a classic model for wealth (many have little, few have a lot).
a = 1.5  # Shape parameter for Pareto
data3 = np.random.pareto(a, num_samples) * 1e5
data3 = np.clip(data3, 0, 2e6) # Clip extreme outliers for better visualization

axes[1, 0].hist(data3, bins=bin_count, alpha=alpha, color=colors[2], edgecolor='black')
axes[1, 0].set_title("Wealth Distribution (Forward J-shape)")
axes[1, 0].set_xlabel("Wealth ($)")
axes[1, 0].set_ylabel("Number of Individuals")
axes[1, 0].set_xlim(left=0)

# --- Version 4: Customer Service Time (Reverse J-shape) ---
# CORRECTED: To create the required reverse J-shape, most customers experience
# long service times, and very few are served quickly.
# We use the same "flipping" technique as for the software faults.
max_service_time = 20  # e.g., max wait is 20 minutes
# Generate data skewed towards 0
flipped_data4 = np.random.exponential(scale=5, size=num_samples)
# Flip it so the peak is at the high end (max_service_time)
data4 = max_service_time - flipped_data4
# Ensure all data points are non-negative and below the max
data4 = np.clip(data4, 0, max_service_time)

axes[1, 1].hist(data4, bins=bin_count, alpha=alpha, color=colors[3], edgecolor='black')
axes[1, 1].set_title("Customer Service Time (Reverse J-shape)")
axes[1, 1].set_xlabel("Service Time (minutes)")
axes[1, 1].set_ylabel("Number of Customers")

# Adjust layout to prevent titles and labels from overlapping
plt.tight_layout(rect=[0, 0, 1, 0.96]) # Adjust rect to make space for suptitle

# Save the figure to a file
plt.savefig("j_shaped_histograms_corrected.png", dpi=300, bbox_inches='tight')

# Display the plot
plt.show()