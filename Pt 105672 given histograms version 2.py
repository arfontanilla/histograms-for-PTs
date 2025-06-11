import numpy as np
import matplotlib.pyplot as plt

# --- Data from Provided Tables (Third Version) ---

# 1. Student Test Scores
score_bins = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200]
score_freqs = [5, 8, 12, 18, 25, 35, 50, 65, 80, 95, 95, 100, 105, 95, 100, 105, 95, 110, 95, 105, 100, 100, 100, 85, 70, 55, 45, 35, 25, 15, 10, 5, 2]

# 2. Plant Heights
height_bins = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
height_freqs = [5, 8, 12, 18, 25, 35, 50, 65, 80, 95, 95, 85, 90, 105, 100, 105, 100, 95, 100, 95, 100, 100, 95, 80, 70, 55, 45, 35, 25, 15, 10, 5, 2]

# 3. Daily Product Sales
sales_bins = [70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230]
sales_freqs = [5, 8, 12, 18, 25, 35, 50, 65, 80, 85, 80, 90, 95, 90, 95, 85, 95, 100, 90, 95, 90, 85, 95, 85, 70, 55, 45, 35, 25, 15, 10, 5, 2]

# 4. Commute Times
commute_bins = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74]
commute_freqs = [5, 8, 12, 18, 25, 35, 50, 65, 80, 95, 95, 100, 95, 100, 105, 100, 95, 95, 90, 90, 85, 90, 90, 85, 70, 55, 45, 35, 25, 15, 10, 5, 2]


# Reconstruct raw data from frequency tables using np.repeat
data1 = np.repeat(score_bins, score_freqs)
data2 = np.repeat(height_bins, height_freqs)
data3 = np.repeat(sales_bins, sales_freqs)
data4 = np.repeat(commute_bins, commute_freqs)

# --- Plotting Setup ---

# Create a figure with 4 subplots (2 rows, 2 columns)
fig, axes = plt.subplots(2, 2, figsize=(12, 6))
fig.suptitle("Histograms of Various Datasets", fontsize=18)

# Common settings for all histograms
alpha = 0.75  # Transparency for histograms
edgecolor = 'black'

# Custom colors from hex codes for each plot
colors = ['#9EDAE2', '#60B2DE', '#A5CDF2', '#03A28D']


# --- Helper function to calculate bin edges from bin centers ---
def get_bin_edges(bin_centers):
    """Calculates the edges of histogram bins given their center points."""
    bin_width = bin_centers[1] - bin_centers[0]
    start_edge = bin_centers[0] - bin_width / 2
    end_edge = bin_centers[-1] + bin_width / 2
    return np.linspace(start_edge, end_edge, len(bin_centers) + 1)

# --- Version 1: Student Test Scores ---
bins1 = get_bin_edges(score_bins)
axes[0, 0].hist(data1, bins=bins1, alpha=alpha, color=colors[0], edgecolor=edgecolor)
axes[0, 0].set_title("Student Test Scores")
axes[0, 0].set_xlabel("Test Score")
axes[0, 0].set_ylabel("Frequency (# of Students)")

# --- Version 2: Plant Heights ---
bins2 = get_bin_edges(height_bins)
axes[0, 1].hist(data2, bins=bins2, alpha=alpha, color=colors[0], edgecolor=edgecolor)
axes[0, 1].set_title("Plant Heights")
axes[0, 1].set_xlabel("Height (cm)")
axes[0, 1].set_ylabel("Frequency (# of Plants)")

# --- Version 3: Daily Product Sales ---
bins3 = get_bin_edges(sales_bins)
axes[1, 0].hist(data3, bins=bins3, alpha=alpha, color=colors[0], edgecolor=edgecolor)
axes[1, 0].set_title("Daily Product Sales")
axes[1, 0].set_xlabel("Daily Sales (Units)")
axes[1, 0].set_ylabel("Frequency (# of Days)")

# --- Version 4: Commute Times ---
bins4 = get_bin_edges(commute_bins)
axes[1, 1].hist(data4, bins=bins4, alpha=alpha, color=colors[0], edgecolor=edgecolor)
axes[1, 1].set_title("Commute Times")
axes[1, 1].set_xlabel("Commute Time (minutes)")
axes[1, 1].set_ylabel("Frequency (# of Employees)")

# Adjust layout to prevent titles and labels from overlapping
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Save the figure to a file
plt.savefig("third_version_histograms.png", dpi=300, bbox_inches='tight')

# Display the plot
plt.show()