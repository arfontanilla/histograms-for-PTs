import numpy as np
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Uniform Distribution Histograms", fontsize=16)

# Common settings for all histograms
num_samples = 1000
alpha = 0.7  # Transparency for histograms

# Custom colors from hex codes
colors = ['#F7B24B', '#FF9B6F', '#FC7E8D', '#A68DF2']

# --- Version 1: Fair Die ---
die_outcomes = np.random.randint(1, 7, num_samples)
axes[0, 0].hist(die_outcomes, bins=6, alpha=alpha, color=colors[0], 
                edgecolor='black', align='mid', rwidth=0.8)
axes[0, 0].set_title("Fair Die Rolls")
axes[0, 0].set_xlabel("Outcome of Die Roll")
axes[0, 0].set_ylabel("Frequency")
axes[0, 0].set_xticks(range(1, 7))

# --- Version 2: Number Generator ---
generated_numbers = np.random.randint(0, 5, num_samples)
axes[0, 1].hist(generated_numbers, bins=5, alpha=alpha, color=colors[1], 
                edgecolor='black', align='mid', rwidth=0.8)
axes[0, 1].set_title("Random Number Generator (0-4)")
axes[0, 1].set_xlabel("Generated Number")
axes[0, 1].set_ylabel("Count")
axes[0, 1].set_xticks(range(0, 5))

# --- Version 3: Fair Spinner ---
spinner_sections = np.random.randint(10, 18, num_samples)
axes[1, 0].hist(spinner_sections, bins=8, alpha=alpha, color=colors[2], 
                edgecolor='black', align='mid', rwidth=0.8)
axes[1, 0].set_title("Fair Spinner Landings")
axes[1, 0].set_xlabel("Spinner Section")
axes[1, 0].set_ylabel("Number of Landings")
axes[1, 0].set_xticks(range(10, 18))

# --- Version 4: Last Digit of Phone Numbers ---
phone_digits = np.random.randint(0, 10, num_samples)
axes[1, 1].hist(phone_digits, bins=10, alpha=alpha, color=colors[3], 
                edgecolor='black', align='mid', rwidth=0.8)
axes[1, 1].set_title("Last Digit of Phone Numbers")
axes[1, 1].set_xlabel("Last Digit of Phone Number")
axes[1, 1].set_ylabel("Frequency")
axes[1, 1].set_xticks(range(0, 10))

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("uniform_histograms.png", dpi=300, bbox_inches='tight')
plt.show()