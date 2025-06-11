import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma, norm

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 6))
fig.suptitle("Histograms with Incorrect Symmetric Curve Overlay", fontsize=16)

# Common settings for all histograms
num_samples = 1000
bin_count = 20
alpha = 0.75  # Transparency for histograms
curve_linewidth = 2.5 # Linewidth for the smooth curve

# To create a subtle positive skew, we use the Gamma distribution.
subtle_skew_shape = 15

# Custom colors from hex codes
colors = ['#9EDAE2', '#A5CDF2', '#60B2DE', '#B6A1F5']

# --- Function to plot histogram and an INCORRECT symmetric curve ---
def plot_hist_and_incorrect_curve(ax, data, bins, color, title, xlabel):
    """Plots a histogram and an incorrect, symmetric (Normal) curve."""
    # Plot the histogram and get bin information
    counts, bin_edges, _ = ax.hist(data, bins=bins, alpha=alpha, color=color, edgecolor='black')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Frequency")

    # To create a plausible but incorrect symmetric curve, we fit a Normal distribution
    # to the mean and standard deviation of the *actual* skewed data.
    mu = np.mean(data)
    sigma = np.std(data)

    # To overlay the curve on a frequency histogram, we must scale the PDF.
    # The scale factor is N * w, where N is the number of samples and w is the bin width.
    bin_width = bin_edges[1] - bin_edges[0]
    scale_factor = num_samples * bin_width

    # Generate x-values for the smooth curve
    x_curve = np.linspace(min(bin_edges), max(bin_edges), 200)

    # Calculate the y-values (PDF) for the NORMAL curve
    y_pdf = norm.pdf(x_curve, loc=mu, scale=sigma)

    # Scale the PDF and plot the incorrect symmetric curve
    ax.plot(x_curve, y_pdf * scale_factor, color='black', linewidth=curve_linewidth)


# --- Version 1: Student Test Scores ---
scale1 = 5.33
data1 = np.random.gamma(shape=subtle_skew_shape, scale=scale1, size=num_samples)
data1 = np.clip(data1, 0, 100)
plot_hist_and_incorrect_curve(axes[0, 0], data1, bin_count, colors[0],
                              "Student Test Scores", "Score (out of 100)")

# --- Version 2: Daily Coffee Shop Customers ---
scale2 = 8
data2 = np.random.gamma(shape=subtle_skew_shape, scale=scale2, size=num_samples)
plot_hist_and_incorrect_curve(axes[0, 1], data2, bin_count, colors[0],
                              "Daily Coffee Shop Customers", "Number of Customers")

# --- Version 3: Duration of Customer Service Calls ---
scale3 = 0.33
data3 = np.random.gamma(shape=subtle_skew_shape, scale=scale3, size=num_samples)
plot_hist_and_incorrect_curve(axes[1, 0], data3, bin_count, colors[0],
                              "Duration of Customer Service Calls", "Duration (minutes)")

# --- Version 4: Commute Times to Work ---
scale4 = 1.67
data4 = np.random.gamma(shape=subtle_skew_shape, scale=scale4, size=num_samples)
plot_hist_and_incorrect_curve(axes[1, 1], data4, bin_count, colors[0],
                              "Commute Times to Work", "Commute Time (minutes)")

# Adjust layout to prevent titles and labels from overlapping
plt.tight_layout(rect=[0, 0, 1, 0.96]) # Adjust rect to make space for suptitle
plt.show()