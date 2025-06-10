import numpy as np
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("J-Shaped Histograms with Incorrect Uniform Curve Fit", fontsize=16)

# Common settings for all histograms
num_samples = 2000
bin_count = 25
alpha = 0.75  # Transparency for histograms
curve_color = 'black'
curve_linewidth = 2.5

# Custom colors from hex codes
colors = ['#838EF0', '#19C9D6', '#FAC88C', '#E69BA6']

# --- Helper function to create a uniform (flat) line ---
def create_uniform_curve(ax, bin_edges, num_samples, bin_count):
    """Generates and plots a scaled uniform (flat) line on a given axis."""
    # Calculate the expected frequency for a true uniform distribution
    line_height = num_samples / bin_count
    
    # Get the start and end points for the line
    xmin, xmax = bin_edges[0], bin_edges[-1]
    
    # Plot the horizontal line
    ax.plot([xmin, xmax], [line_height, line_height], color=curve_color, linewidth=curve_linewidth)


# --- Version 1: Word Frequency (Forward J-shape) ---
data1 = np.random.exponential(scale=1.5, size=num_samples)
_, bin_edges1, _ = axes[0, 0].hist(data1, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
axes[0, 0].set_title("Word Frequency (Forward J-shape)")
axes[0, 0].set_xlabel("Word Rarity (Higher value is more rare)")
axes[0, 0].set_ylabel("Frequency")
axes[0, 0].set_xlim(left=0)
create_uniform_curve(axes[0, 0], bin_edges1, num_samples, bin_count)

# --- Version 2: Software Faults (Reverse J-shape) ---
max_faults = 60
flipped_data2 = np.random.exponential(scale=10, size=num_samples)
data2 = max_faults - flipped_data2
data2 = np.clip(data2, 0, max_faults)

_, bin_edges2, _ = axes[0, 1].hist(data2, bins=bin_count, alpha=alpha, color=colors[1], edgecolor='black')
axes[0, 1].set_title("Software Faults (Reverse J-shape)")
axes[0, 1].set_xlabel("Faults per Module")
axes[0, 1].set_ylabel("Number of Modules")
create_uniform_curve(axes[0, 1], bin_edges2, num_samples, bin_count)

# --- Version 3: Wealth Distribution (Forward J-shape) ---
a = 1.5
data3 = np.random.pareto(a, num_samples) * 1e5
data3_clipped = np.clip(data3, 0, 2e6)

_, bin_edges3, _ = axes[1, 0].hist(data3_clipped, bins=bin_count, alpha=alpha, color=colors[2], edgecolor='black')
axes[1, 0].set_title("Wealth Distribution (Forward J-shape)")
axes[1, 0].set_xlabel("Wealth ($)")
axes[1, 0].set_ylabel("Number of Individuals")
axes[1, 0].set_xlim(left=0, right=2e6)
create_uniform_curve(axes[1, 0], bin_edges3, num_samples, bin_count)

# --- Version 4: Customer Service Time (Reverse J-shape) ---
max_service_time = 20
flipped_data4 = np.random.exponential(scale=5, size=num_samples)
data4 = max_service_time - flipped_data4
data4 = np.clip(data4, 0, max_service_time)

_, bin_edges4, _ = axes[1, 1].hist(data4, bins=bin_count, alpha=alpha, color=colors[3], edgecolor='black')
axes[1, 1].set_title("Customer Service Time (Reverse J-shape)")
axes[1, 1].set_xlabel("Service Time (minutes)")
axes[1, 1].set_ylabel("Number of Customers")
create_uniform_curve(axes[1, 1], bin_edges4, num_samples, bin_count)


# Adjust layout to prevent titles and labels from overlapping
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save the figure to a file
plt.savefig("j_shaped_histograms_with_incorrect_uniform_curves.png", dpi=300, bbox_inches='tight')

# Display the plot
plt.show()