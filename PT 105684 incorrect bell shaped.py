import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm # We need the Normal distribution for the incorrect curve

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots - adjusted size for better clarity
fig, axes = plt.subplots(2, 2, figsize=(12, 6))
fig.suptitle("Histograms with Incorrect (Bell-Shaped) Curve", fontsize=18, y=0.98)

# --- Common Settings ---
num_samples = 2000
bin_count = 25
alpha = 0.75
edge_color = 'black'
curve_color = 'black'
curve_linewidth = 2.5

# Custom colors from hex codes as provided
colors = ['#9EDAE2', '#A5CDF2', '#60B2DE', '#B6A1F5']

# --- Helper function to plot histogram and the INCORRECT curve ---
def plot_hist_and_incorrect_curve(ax, data, loc, scale, color, title, xlabel, ylabel):
    """Generates a leptokurtic histogram and overlays a scaled Normal (bell-shaped) curve."""
    # Plot the histogram from the Laplace data
    counts, bin_edges, _ = ax.hist(data, bins=bin_count, alpha=alpha, color=color, edgecolor=edge_color)
    
    # Calculate the width of the histogram bins for scaling
    bin_width = bin_edges[1] - bin_edges[0]
    
    # --- Define parameters for the INCORRECT Normal (bell-shaped) curve ---
    # The mean is the same as the Laplace location parameter.
    mean_norm = loc
    # To make it a plausible fit, we match the variance.
    # Variance of Laplace(loc, scale) is 2*scale^2.
    # Standard deviation (sigma) for the Normal curve is sqrt(variance).
    std_dev_norm = scale * np.sqrt(2)
    
    # Create a smooth range of x-values for the curve
    x_curve = np.linspace(bin_edges[0], bin_edges[-1], 200)
    
    # Calculate the Normal PDF for the x-values
    pdf_curve = norm.pdf(x_curve, loc=mean_norm, scale=std_dev_norm)
    
    # Scale the PDF to match the frequency scale of the histogram
    scaled_pdf_curve = pdf_curve * num_samples * bin_width
    
    # Plot the incorrectly shaped (but plausibly fitted) curve
    ax.plot(x_curve, scaled_pdf_curve, color=curve_color, linewidth=curve_linewidth)
    
    # Set titles and labels
    ax.set_title(title, fontsize=14)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.grid(axis='y', alpha=0.5, linestyle='--')

# --- Version 1: Sprinter Reaction Times ---
loc1, scale1 = 150, 5
data1 = np.random.laplace(loc1, scale1, num_samples)
plot_hist_and_incorrect_curve(axes[0, 0], data1, loc1, scale1, colors[0],
                              "Sprinter Reaction Times", "Reaction Time (ms)", "Frequency of Trials")

# --- Version 2: Precision-Cut Washer Thickness ---
loc2, scale2 = 5.0, 0.02
data2 = np.random.laplace(loc2, scale2, num_samples)
plot_hist_and_incorrect_curve(axes[0, 1], data2, loc2, scale2, colors[0],
                              "Precision-Cut Washer Thickness", "Washer Thickness (mm)", "Number of Washers")

# --- Version 3: Server Response Times ---
loc3, scale3 = 80, 8
data3 = np.random.laplace(loc3, scale3, num_samples)
plot_hist_and_incorrect_curve(axes[1, 0], data3, loc3, scale3, colors[0],
                              "Server Response Times", "Server Response Time (ms)", "Number of Queries")

# --- Version 4: Scientific Measurement Deviations ---
loc4, scale4 = 0, 0.5
data4 = np.random.laplace(loc4, scale4, num_samples)
plot_hist_and_incorrect_curve(axes[1, 1], data4, loc4, scale4, colors[0],
                              "Scientific Measurement Deviations", "Measurement Deviation (units)", "Frequency")

# Adjust layout and save the figure
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("peaked_histograms_with_incorrect_curves.png", dpi=300, bbox_inches='tight')
plt.show()