import numpy as np
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("J-Shaped Histograms with Incorrect U-Shaped Curve Fit", fontsize=16)

# Common settings for all histograms
num_samples = 2000
bin_count = 25
alpha = 0.75  # Transparency for histograms
curve_color = 'black'
curve_linewidth = 2.5

# Custom colors from hex codes
colors = ['#838EF0', '#19C9D6', '#FAC88C', '#E69BA6']

# --- Helper function to create a U-shaped curve ---
def create_u_curve(ax, bin_edges, counts):
    """Generates and plots a scaled U-shaped parabola on a given axis."""
    # Get the range and center of the x-axis
    xmin, xmax = bin_edges[0], bin_edges[-1]
    center = (xmin + xmax) / 2.0
    
    # Create x-values for the smooth curve
    x_curve = np.linspace(xmin, xmax, 500)
    
    # Create a basic parabola (U-shape) centered at x=0
    # We normalize the x-values to be in [-1, 1] to make the parabola y=(x^2)
    x_normalized = (x_curve - center) / (xmax - center)
    y_parabola = x_normalized**2
    
    # Scale the parabola to fit the plot visually
    max_hist_height = np.max(counts)
    min_curve_height = max_hist_height * 0.05  # Bottom of the U sits near the bottom
    max_curve_height = max_hist_height * 0.70  # Top of the U reaches a visible height
    
    y_curve_scaled = y_parabola * (max_curve_height - min_curve_height) + min_curve_height
    
    ax.plot(x_curve, y_curve_scaled, color=curve_color, linewidth=curve_linewidth)


# --- Version 1: Word Frequency (Forward J-shape) ---
data1 = np.random.exponential(scale=1.5, size=num_samples)
counts1, bin_edges1, _ = axes[0, 0].hist(data1, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
axes[0, 0].set_title("Word Frequency (Forward J-shape)")
axes[0, 0].set_xlabel("Word Rarity (Higher value is more rare)")
axes[0, 0].set_ylabel("Frequency")
axes[0, 0].set_xlim(left=0)
create_u_curve(axes[0, 0], bin_edges1, counts1)

# --- Version 2: Software Faults (Reverse J-shape) ---
max_faults = 60
flipped_data2 = np.random.exponential(scale=10, size=num_samples)
data2 = max_faults - flipped_data2
data2 = np.clip(data2, 0, max_faults)

counts2, bin_edges2, _ = axes[0, 1].hist(data2, bins=bin_count, alpha=alpha, color=colors[1], edgecolor='black')
axes[0, 1].set_title("Software Faults (Reverse J-shape)")
axes[0, 1].set_xlabel("Faults per Module")
axes[0, 1].set_ylabel("Number of Modules")
create_u_curve(axes[0, 1], bin_edges2, counts2)

# --- Version 3: Wealth Distribution (Forward J-shape) ---
a = 1.5
data3 = np.random.pareto(a, num_samples) * 1e5
data3_clipped = np.clip(data3, 0, 2e6)

counts3, bin_edges3, _ = axes[1, 0].hist(data3_clipped, bins=bin_count, alpha=alpha, color=colors[2], edgecolor='black')
axes[1, 0].set_title("Wealth Distribution (Forward J-shape)")
axes[1, 0].set_xlabel("Wealth ($)")
axes[1, 0].set_ylabel("Number of Individuals")
axes[1, 0].set_xlim(left=0, right=2e6)
create_u_curve(axes[1, 0], bin_edges3, counts3)

# --- Version 4: Customer Service Time (Reverse J-shape) ---
max_service_time = 20
flipped_data4 = np.random.exponential(scale=5, size=num_samples)
data4 = max_service_time - flipped_data4
data4 = np.clip(data4, 0, max_service_time)

counts4, bin_edges4, _ = axes[1, 1].hist(data4, bins=bin_count, alpha=alpha, color=colors[3], edgecolor='black')
axes[1, 1].set_title("Customer Service Time (Reverse J-shape)")
axes[1, 1].set_xlabel("Service Time (minutes)")
axes[1, 1].set_ylabel("Number of Customers")
create_u_curve(axes[1, 1], bin_edges4, counts4)

# Adjust layout to prevent titles and labels from overlapping
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save the figure to a file
plt.savefig("j_shaped_histograms_with_incorrect_u_curves.png", dpi=300, bbox_inches='tight')

# Display the plot
plt.show()