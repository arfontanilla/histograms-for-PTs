import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import cosine # Import the cosine distribution for its platykurtic shape

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

# Reconstruct raw data from frequency tables
data1 = np.repeat(score_bins, score_freqs)
data2 = np.repeat(height_bins, height_freqs)
data3 = np.repeat(sales_bins, sales_freqs)
data4 = np.repeat(commute_bins, commute_freqs)

# --- Plotting Setup ---

# Create a figure with 4 subplots, increased size for better spacing
fig, axes = plt.subplots(2, 2, figsize=(12, 6))
fig.suptitle("Histograms with Platykurtic Curves", fontsize=18)

# Common settings for all plots
alpha = 0.75
edgecolor = 'black'
curve_color = 'black'
curve_linewidth = 2.5
colors = ['#9EDAE2', '#60B2DE', '#A5CDF2', '#03A28D']

# --- Helper function to calculate bin edges ---
def get_bin_edges(bin_centers):
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
# Add platykurtic curve
mu1, sigma1 = np.mean(data1), np.std(data1)
x1 = np.linspace(mu1 - 4 * sigma1, mu1 + 4 * sigma1, 200)
bin_width1 = score_bins[1] - score_bins[0]
pdf1 = cosine.pdf(x1, loc=mu1, scale=sigma1) * len(data1) * bin_width1
axes[0, 0].plot(x1, pdf1, color=curve_color, linewidth=curve_linewidth)

# --- Version 2: Plant Heights ---
bins2 = get_bin_edges(height_bins)
axes[0, 1].hist(data2, bins=bins2, alpha=alpha, color=colors[0], edgecolor=edgecolor)
axes[0, 1].set_title("Plant Heights")
axes[0, 1].set_xlabel("Height (cm)")
axes[0, 1].set_ylabel("Frequency (# of Plants)")
# Add platykurtic curve
mu2, sigma2 = np.mean(data2), np.std(data2)
x2 = np.linspace(mu2 - 4 * sigma2, mu2 + 4 * sigma2, 200)
bin_width2 = height_bins[1] - height_bins[0]
pdf2 = cosine.pdf(x2, loc=mu2, scale=sigma2) * len(data2) * bin_width2
axes[0, 1].plot(x2, pdf2, color=curve_color, linewidth=curve_linewidth)

# --- Version 3: Daily Product Sales ---
bins3 = get_bin_edges(sales_bins)
axes[1, 0].hist(data3, bins=bins3, alpha=alpha, color=colors[0], edgecolor=edgecolor)
axes[1, 0].set_title("Daily Product Sales")
axes[1, 0].set_xlabel("Daily Sales (Units)")
axes[1, 0].set_ylabel("Frequency (# of Days)")
# Add platykurtic curve
mu3, sigma3 = np.mean(data3), np.std(data3)
x3 = np.linspace(mu3 - 4 * sigma3, mu3 + 4 * sigma3, 200)
bin_width3 = sales_bins[1] - sales_bins[0]
pdf3 = cosine.pdf(x3, loc=mu3, scale=sigma3) * len(data3) * bin_width3
axes[1, 0].plot(x3, pdf3, color=curve_color, linewidth=curve_linewidth)

# --- Version 4: Commute Times ---
bins4 = get_bin_edges(commute_bins)
axes[1, 1].hist(data4, bins=bins4, alpha=alpha, color=colors[0], edgecolor=edgecolor)
axes[1, 1].set_title("Commute Times")
axes[1, 1].set_xlabel("Commute Time (minutes)")
axes[1, 1].set_ylabel("Frequency (# of Employees)")
# Add platykurtic curve
mu4, sigma4 = np.mean(data4), np.std(data4)
x4 = np.linspace(mu4 - 4 * sigma4, mu4 + 4 * sigma4, 200)
bin_width4 = commute_bins[1] - commute_bins[0]
pdf4 = cosine.pdf(x4, loc=mu4, scale=sigma4) * len(data4) * bin_width4
axes[1, 1].plot(x4, pdf4, color=curve_color, linewidth=curve_linewidth)

# Adjust layout to prevent titles and labels from overlapping
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Save the figure to a file
plt.savefig("histograms_with_platykurtic_curves_v3.png", dpi=300, bbox_inches='tight')

# Display the plot
plt.show()