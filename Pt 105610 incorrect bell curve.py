import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Histograms with Incorrect Unimodal Symmetric Curves", fontsize=16)

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

# Plot histogram and get bin info
n1, bins1, _ = axes[0, 0].hist(data1, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
axes[0, 0].set_title("Test Scores from Two Classes")
axes[0, 0].set_xlabel("Test Score")
axes[0, 0].set_ylabel("Number of Students")

# Generate and plot the incorrect unimodal curve
mu1, sigma1 = np.mean(data1), np.std(data1)
x1 = np.linspace(data1.min(), data1.max(), 500)
pdf1 = norm.pdf(x1, loc=mu1, scale=sigma1)
# Scale PDF to match histogram frequency
bin_width1 = bins1[1] - bins1[0]
scaled_pdf1 = pdf1 * len(data1) * bin_width1
axes[0, 0].plot(x1, scaled_pdf1, color='black', linewidth=2.5)


# --- Version 2: Geyser Eruption Durations ---
# Create two types of eruption durations: short and long
short_eruptions = np.random.normal(loc=2.0, scale=0.3, size=400)
long_eruptions = np.random.normal(loc=4.3, scale=0.4, size=600)
data2 = np.concatenate([short_eruptions, long_eruptions])

# Plot histogram and get bin info
n2, bins2, _ = axes[0, 1].hist(data2, bins=bin_count, alpha=alpha, color=colors[1], edgecolor='black')
axes[0, 1].set_title("Geyser Eruption Durations")
axes[0, 1].set_xlabel("Eruption Duration (Minutes)")
axes[0, 1].set_ylabel("Number of Eruptions")

# Generate and plot the incorrect unimodal curve
mu2, sigma2 = np.mean(data2), np.std(data2)
x2 = np.linspace(data2.min(), data2.max(), 500)
pdf2 = norm.pdf(x2, loc=mu2, scale=sigma2)
# Scale PDF to match histogram frequency
bin_width2 = bins2[1] - bins2[0]
scaled_pdf2 = pdf2 * len(data2) * bin_width2
axes[0, 1].plot(x2, scaled_pdf2, color='black', linewidth=2.5)


# --- Version 3: Heights of Mixed Plant Species ---
# Create two groups for two different plant species
heights_species_a = np.random.normal(loc=32, scale=3, size=500)
heights_species_b = np.random.normal(loc=53, scale=4, size=500)
data3 = np.concatenate([heights_species_a, heights_species_b])

# Plot histogram and get bin info
n3, bins3, _ = axes[1, 0].hist(data3, bins=bin_count, alpha=alpha, color=colors[2], edgecolor='black')
axes[1, 0].set_title("Heights of Mixed Plant Species")
axes[1, 0].set_xlabel("Plant Height (cm)")
axes[1, 0].set_ylabel("Number of Plants")

# Generate and plot the incorrect unimodal curve
mu3, sigma3 = np.mean(data3), np.std(data3)
x3 = np.linspace(data3.min(), data3.max(), 500)
pdf3 = norm.pdf(x3, loc=mu3, scale=sigma3)
# Scale PDF to match histogram frequency
bin_width3 = bins3[1] - bins3[0]
scaled_pdf3 = pdf3 * len(data3) * bin_width3
axes[1, 0].plot(x3, scaled_pdf3, color='black', linewidth=2.5)


# --- Version 4: Customer Satisfaction Scores for Two Product Versions ---
# Create two groups for old vs. new product version users
scores_old_version = np.random.normal(loc=4.5, scale=1.0, size=350)
scores_new_version = np.random.normal(loc=8.5, scale=0.8, size=650)
data4 = np.concatenate([scores_old_version, scores_new_version])
data4 = np.clip(data4, 1, 10) # Clip scores to the 1-10 scale

# Plot histogram and get bin info
n4, bins4, _ = axes[1, 1].hist(data4, bins=10, alpha=alpha, color=colors[3], edgecolor='black')
axes[1, 1].set_title("Customer Satisfaction Scores")
axes[1, 1].set_xlabel("Customer Satisfaction Score (1-10)")
axes[1, 1].set_ylabel("Number of Customers")

# Generate and plot the incorrect unimodal curve
mu4, sigma4 = np.mean(data4), np.std(data4)
x4 = np.linspace(data4.min(), data4.max(), 500)
pdf4 = norm.pdf(x4, loc=mu4, scale=sigma4)
# Scale PDF to match histogram frequency
bin_width4 = bins4[1] - bins4[0]
scaled_pdf4 = pdf4 * len(data4) * bin_width4
axes[1, 1].plot(x4, scaled_pdf4, color='black', linewidth=2.5)


# Adjust layout and save the figure
plt.tight_layout(rect=[0, 0.03, 1, 0.96]) # Adjust rect to make space for suptitle
plt.savefig("bimodal_histograms_incorrect_unimodal.png", dpi=300, bbox_inches='tight')
plt.show()