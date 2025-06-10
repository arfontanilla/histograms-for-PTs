import numpy as np
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Bimodal Histograms for Problem Templates", fontsize=16)

# Common settings for all histograms
bin_count = 15
alpha = 0.7  # Transparency for histograms

# Custom colors from hex codes
colors = ['#60B2DE', '#03A28D', '#FFB492', '#B6A1F5']

# --- Version 1: Test Scores from Two Classes ---
# Create two distinct groups of scores
scores_class_x = np.random.normal(loc=88, scale=5, size=550)
scores_class_y = np.random.normal(loc=68, scale=6, size=450)
data1 = np.concatenate([scores_class_x, scores_class_y])
data1 = np.clip(data1, 40, 100) # Clip scores to a realistic range

axes[0, 0].hist(data1, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
axes[0, 0].set_title("Test Scores from Two Classes")
axes[0, 0].set_xlabel("Test Score")
axes[0, 0].set_ylabel("Number of Students")

# --- Version 2: Geyser Eruption Durations ---
# Create two types of eruption durations: short and long
short_eruptions = np.random.normal(loc=2.0, scale=0.3, size=400)
long_eruptions = np.random.normal(loc=4.3, scale=0.4, size=600)
data2 = np.concatenate([short_eruptions, long_eruptions])

axes[0, 1].hist(data2, bins=bin_count, alpha=alpha, color=colors[1], edgecolor='black')
axes[0, 1].set_title("Geyser Eruption Durations")
axes[0, 1].set_xlabel("Eruption Duration (Minutes)")
axes[0, 1].set_ylabel("Number of Eruptions")

# --- Version 3: Heights of Mixed Plant Species ---
# Create two groups for two different plant species
heights_species_a = np.random.normal(loc=32, scale=3, size=500)
heights_species_b = np.random.normal(loc=53, scale=4, size=500)
data3 = np.concatenate([heights_species_a, heights_species_b])

axes[1, 0].hist(data3, bins=bin_count, alpha=alpha, color=colors[2], edgecolor='black')
axes[1, 0].set_title("Heights of Mixed Plant Species")
axes[1, 0].set_xlabel("Plant Height (cm)")
axes[1, 0].set_ylabel("Number of Plants")

# --- Version 4: Customer Satisfaction Scores for Two Product Versions ---
# Create two groups for old vs. new product version users
scores_old_version = np.random.normal(loc=4.5, scale=1.0, size=350)
scores_new_version = np.random.normal(loc=8.5, scale=0.8, size=650)
data4 = np.concatenate([scores_old_version, scores_new_version])
data4 = np.clip(data4, 1, 10) # Clip scores to the 1-10 scale

axes[1, 1].hist(data4, bins=10, alpha=alpha, color=colors[3], edgecolor='black') # Using 10 bins for 1-10 scale
axes[1, 1].set_title("Customer Satisfaction Scores")
axes[1, 1].set_xlabel("Customer Satisfaction Score (1-10)")
axes[1, 1].set_ylabel("Number of Customers")

# Adjust layout and save the figure
plt.tight_layout(rect=[0, 0.03, 1, 0.96]) # Adjust rect to make space for suptitle
plt.savefig("bimodal_histograms.png", dpi=300, bbox_inches='tight')
plt.show()