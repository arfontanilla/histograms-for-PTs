import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Positively Skewed Histograms for Problem Templates", fontsize=16)

# Common settings for all histograms
num_samples = 1000
bin_count = 15
alpha = 0.7  # Transparency for histograms
skewness = 5  # Positive skewness parameter

# Custom colors from hex codes
colors = ['#838EF0', '#60B2DE', '#19C9D6', '#03A28D']

# Function to add INCORRECT positively skewed curve
def add_misaligned_curve(ax, data, color):
    # Create x values
    x = np.linspace(min(data)*0.5, max(data)*0.8, 1000)  # Intentionally too narrow
    
    # Parameters to make the curve clearly wrong:
    # - Reduced skewness (less extreme than data)
    # - Location shifted left
    # - Scale reduced to shorten the tail
    incorrect_skew = skewness * 0.6
    incorrect_loc = np.min(data) + (np.mean(data) - np.min(data))*0.7  # Shifted left
    incorrect_scale = np.std(data)*0.6  # Shorter tail
    
    # Generate incorrect skewed PDF
    y = skewnorm.pdf(x, incorrect_skew, incorrect_loc, incorrect_scale)
    
    # Scale the PDF to match histogram counts
    hist_height, _ = np.histogram(data, bins=bin_count)
    max_pdf = max(y)
    max_hist = max(hist_height)
    y_scaled = y * (max_hist / max_pdf)
    
    # Plot the incorrect curve
    ax.plot(x, y_scaled, color='black', linewidth=2)

# --- Version 1: Reaction Times ---
a1, loc1, scale1 = skewness, 0.2, 0.1
data1 = skewnorm.rvs(a1, loc=loc1, scale=scale1, size=num_samples)
axes[0, 0].hist(data1, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
add_misaligned_curve(axes[0, 0], data1, colors[0])
axes[0, 0].set_title("Reaction Times (seconds)")
axes[0, 0].set_xlabel("Reaction Time (seconds)")
axes[0, 0].set_ylabel("Frequency")
axes[0, 0].set_xlim([0, 1.2])

# --- Version 2: Annual Household Incomes ---
a2, loc2, scale2 = skewness, 40, 15
data2 = skewnorm.rvs(a2, loc=loc2, scale=scale2, size=num_samples)
axes[0, 1].hist(data2, bins=bin_count, alpha=alpha, color=colors[1], edgecolor='black')
add_misaligned_curve(axes[0, 1], data2, colors[1])
axes[0, 1].set_title("Annual Household Incomes ($ thousands)")
axes[0, 1].set_xlabel("Annual Household Income ($ thousands)")
axes[0, 1].set_ylabel("Number of Households")
axes[0, 1].set_xlim([0, 150])

# --- Version 3: Daily Customer Numbers ---
a3, loc3, scale3 = skewness, 50, 20
data3 = skewnorm.rvs(a3, loc=loc3, scale=scale3, size=num_samples)
axes[1, 0].hist(data3, bins=bin_count, alpha=alpha, color=colors[2], edgecolor='black')
add_misaligned_curve(axes[1, 0], data3, colors[2])
axes[1, 0].set_title("Daily Customer Numbers")
axes[1, 0].set_xlabel("Number of Customers per Day")
axes[1, 0].set_ylabel("Frequency (Days)")
axes[1, 0].set_xlim([0, 200])

# --- Version 4: Scores ---
a4, loc4, scale4 = skewness, 40, 15
data4 = skewnorm.rvs(a4, loc=loc4, scale=scale4, size=num_samples)
axes[1, 1].hist(data4, bins=bin_count, alpha=alpha, color=colors[3], edgecolor='black')
add_misaligned_curve(axes[1, 1], data4, colors[3])
axes[1, 1].set_title("Quiz Scores (out of 100)")
axes[1, 1].set_xlabel("Quiz Score")
axes[1, 1].set_ylabel("Number of Students")
axes[1, 1].set_xlim([0, 100])

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("misaligned_positively_skewed_curves.png", dpi=300, bbox_inches='tight')
plt.show()