import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Histograms with Incorrectly Fitted Bimodal Curves", fontsize=16)

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

# Generate and plot the incorrect bimodal curve (peaks shifted left, heights inverted)
loc1_a_bad, scale1_a_bad, size1_a_bad = 82, 5, 450 # Shifted peak, swapped size
loc1_b_bad, scale1_b_bad, size1_b_bad = 62, 6, 550 # Shifted peak, swapped size
total_samples1 = size1_a_bad + size1_b_bad
x1 = np.linspace(data1.min(), data1.max(), 500)
pdf1_a = norm.pdf(x1, loc=loc1_a_bad, scale=scale1_a_bad) * size1_a_bad / total_samples1
pdf1_b = norm.pdf(x1, loc=loc1_b_bad, scale=scale1_b_bad) * size1_b_bad / total_samples1
combined_pdf1 = pdf1_a + pdf1_b
bin_width1 = bins1[1] - bins1[0]
scaled_pdf1 = combined_pdf1 * len(data1) * bin_width1
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

# Generate and plot the incorrect bimodal curve (peaks closer together, widths are wrong)
loc2_a_bad, scale2_a_bad, size2_a_bad = 2.5, 0.6, 400 # Shifted peak, wider
loc2_b_bad, scale2_b_bad, size2_b_bad = 4.0, 0.2, 600 # Shifted peak, narrower
total_samples2 = size2_a_bad + size2_b_bad
x2 = np.linspace(data2.min(), data2.max(), 500)
pdf2_a = norm.pdf(x2, loc=loc2_a_bad, scale=scale2_a_bad) * size2_a_bad / total_samples2
pdf2_b = norm.pdf(x2, loc=loc2_b_bad, scale=scale2_b_bad) * size2_b_bad / total_samples2
combined_pdf2 = pdf2_a + pdf2_b
bin_width2 = bins2[1] - bins2[0]
scaled_pdf2 = combined_pdf2 * len(data2) * bin_width2
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

# Generate and plot the incorrect bimodal curve (peaks shifted right)
loc3_a_bad, scale3_a_bad, size3_a_bad = 40, 3, 500 # Shifted significantly right
loc3_b_bad, scale3_b_bad, size3_b_bad = 60, 4, 500 # Shifted significantly right
total_samples3 = size3_a_bad + size3_b_bad
x3 = np.linspace(data3.min(), data3.max(), 500)
pdf3_a = norm.pdf(x3, loc=loc3_a_bad, scale=scale3_a_bad) * size3_a_bad / total_samples3
pdf3_b = norm.pdf(x3, loc=loc3_b_bad, scale=scale3_b_bad) * size3_b_bad / total_samples3
combined_pdf3 = pdf3_a + pdf3_b
bin_width3 = bins3[1] - bins3[0]
scaled_pdf3 = combined_pdf3 * len(data3) * bin_width3
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

# Generate and plot the incorrect bimodal curve (relative heights are swapped)
loc4_a_bad, scale4_a_bad, size4_a_bad = 4.5, 1.0, 650 # Swapped size
loc4_b_bad, scale4_b_bad, size4_b_bad = 8.5, 0.8, 350 # Swapped size
total_samples4 = size4_a_bad + size4_b_bad
x4 = np.linspace(data4.min(), data4.max(), 500)
pdf4_a = norm.pdf(x4, loc=loc4_a_bad, scale=scale4_a_bad) * size4_a_bad / total_samples4
pdf4_b = norm.pdf(x4, loc=loc4_b_bad, scale=scale4_b_bad) * size4_b_bad / total_samples4
combined_pdf4 = pdf4_a + pdf4_b
bin_width4 = bins4[1] - bins4[0]
scaled_pdf4 = combined_pdf4 * len(data4) * bin_width4
axes[1, 1].plot(x4, scaled_pdf4, color='black', linewidth=2.5)


# Adjust layout and save the figure
plt.tight_layout(rect=[0, 0.03, 1, 0.96]) # Adjust rect to make space for suptitle
plt.savefig("bimodal_histograms_incorrectly_fitted.png", dpi=300, bbox_inches='tight')
plt.show()