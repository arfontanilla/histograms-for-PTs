import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Uniform Distribution Histograms with Skewed Curves", fontsize=16)

# Common settings for all histograms
num_samples = 1000
alpha = 0.7  # Transparency for histograms

# Custom colors from hex codes
colors = ['#F7B24B', '#FF9B6F', '#FC7E8D', '#A68DF2']

def plot_skewed_curve(ax, bins, skew_amount, num_samples, x_range):
    """Helper function to plot skewed curve"""
    x = np.linspace(x_range[0], x_range[1], 100)
    # Create skewed distribution
    pdf = skewnorm.pdf(x, skew_amount, loc=np.mean(x), scale=(x_range[1]-x_range[0])/4)
    # Scale to match histogram counts
    pdf = pdf * num_samples/len(bins) * (bins[1]-bins[0]) * 5
    ax.plot(x, pdf, color='black', linewidth=2)

# --- Version 1: Fair Die (Right-skewed) ---
die_outcomes = np.random.randint(1, 7, num_samples)
#counts, bins, _ = axes[0, 0].hist(die_outcomes, bins=6, alpha=alpha, color=colors[0], 
 #               edgecolor='black', align='mid', rwidth=0.8)
axes[0, 0].set_title("Fair Die Rolls")
axes[0, 0].set_xlabel("Outcome of Die Roll")
axes[0, 0].set_ylabel("Frequency")
axes[0, 0].set_xticks(range(1, 7))
plot_skewed_curve(axes[0, 0], bins, 5, num_samples, (0.5, 6.5))  # Positive skew for right-tailed

# --- Version 2: Number Generator (Left-skewed) ---
generated_numbers = np.random.randint(0, 5, num_samples)
#counts, bins, _ = axes[0, 1].hist(generated_numbers, bins=5, alpha=alpha, color=colors[1], 
 #               edgecolor='black', align='mid', rwidth=0.8)
axes[0, 1].set_title("Random Number Generator (0-4)")
axes[0, 1].set_xlabel("Generated Number")
axes[0, 1].set_ylabel("Count")
axes[0, 1].set_xticks(range(0, 5))
plot_skewed_curve(axes[0, 1], bins, -5, num_samples, (-0.5, 4.5))  # Negative skew for left-tailed

# --- Version 3: Fair Spinner (Right-skewed) ---
spinner_sections = np.random.randint(10, 18, num_samples)
#counts, bins, _ = axes[1, 0].hist(spinner_sections, bins=8, alpha=alpha, color=colors[2], 
 #               edgecolor='black', align='mid', rwidth=0.8)
axes[1, 0].set_title("Fair Spinner Landings")
axes[1, 0].set_xlabel("Spinner Section")
axes[1, 0].set_ylabel("Number of Landings")
axes[1, 0].set_xticks(range(10, 18))
plot_skewed_curve(axes[1, 0], bins, 5, num_samples, (9.5, 17.5))  # Positive skew for right-tailed

# --- Version 4: Last Digit of Phone Numbers (Left-skewed) ---
phone_digits = np.random.randint(0, 10, num_samples)
#counts, bins, _ = axes[1, 1].hist(phone_digits, bins=10, alpha=alpha, color=colors[3], 
 #               edgecolor='black', align='mid', rwidth=0.8)
axes[1, 1].set_title("Last Digit of Phone Numbers")
axes[1, 1].set_xlabel("Last Digit of Phone Number")
axes[1, 1].set_ylabel("Frequency")
axes[1, 1].set_xticks(range(0, 10))
plot_skewed_curve(axes[1, 1], bins, -5, num_samples, (-0.5, 9.5))  # Negative skew for left-tailed

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("uniform_histograms_with_skewed_curves.png", dpi=300, bbox_inches='tight')
plt.show()