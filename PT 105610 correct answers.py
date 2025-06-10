import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Bimodal Histograms with Correct Smooth Curves", fontsize=16)

# Common settings for all histograms
bin_count = 15
alpha = 0.7  # Transparency for histograms

# Custom colors from hex codes
colors = ['#60B2DE', '#03A28D', '#FFB492', '#B6A1F5']

# --- Version 1: Test Scores from Two Classes ---
# Parameters for the two groups
loc1_a, scale1_a, size1_a = 88, 5, 550
loc1_b, scale1_b, size1_b = 68, 6, 450
total_samples1 = size1_a + size1_b

# Create data
scores_class_x = np.random.normal(loc=loc1_a, scale=scale1_a, size=size1_a)
scores_class_y = np.random.normal(loc=loc1_b, scale=scale1_b, size=size1_b)
data1 = np.concatenate([scores_class_x, scores_class_y])
data1 = np.clip(data1, 40, 100)

# Plot histogram and get bin info
n1, bins1, _ = axes[0, 0].hist(data1, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
axes[0, 0].set_title("Test Scores from Two Classes")
axes[0, 0].set_xlabel("Test Score")
axes[0, 0].set_ylabel("Number of Students")

# Generate and plot the correct bimodal curve
x1 = np.linspace(data1.min(), data1.max(), 500)
pdf1_a = norm.pdf(x1, loc=loc1_a, scale=scale1_a) * size1_a / total_samples1
pdf1_b = norm.pdf(x1, loc=loc1_b, scale=scale1_b) * size1_b / total_samples1
combined_pdf1 = pdf1_a + pdf1_b
# Scale PDF to match histogram frequency
bin_width1 = bins1[1] - bins1[0]
scaled_pdf1 = combined_pdf1 * total_samples1 * bin_width1
axes[0, 0].plot(x1, scaled_pdf1, color='black', linewidth=2.5)


# --- Version 2: Geyser Eruption Durations ---
# Parameters for the two groups
loc2_a, scale2_a, size2_a = 2.0, 0.3, 400
loc2_b, scale2_b, size2_b = 4.3, 0.4, 600
total_samples2 = size2_a + size2_b

# Create data
short_eruptions = np.random.normal(loc=loc2_a, scale=scale2_a, size=size2_a)
long_eruptions = np.random.normal(loc=loc2_b, scale=scale2_b, size=size2_b)
data2 = np.concatenate([short_eruptions, long_eruptions])

# Plot histogram and get bin info
n2, bins2, _ = axes[0, 1].hist(data2, bins=bin_count, alpha=alpha, color=colors[1], edgecolor='black')
axes[0, 1].set_title("Geyser Eruption Durations")
axes[0, 1].set_xlabel("Eruption Duration (Minutes)")
axes[0, 1].set_ylabel("Number of Eruptions")

# Generate and plot the correct bimodal curve
x2 = np.linspace(data2.min(), data2.max(), 500)
pdf2_a = norm.pdf(x2, loc=loc2_a, scale=scale2_a) * size2_a / total_samples2
pdf2_b = norm.pdf(x2, loc=loc2_b, scale=scale2_b) * size2_b / total_samples2
combined_pdf2 = pdf2_a + pdf2_b
# Scale PDF to match histogram frequency
bin_width2 = bins2[1] - bins2[0]
scaled_pdf2 = combined_pdf2 * total_samples2 * bin_width2
axes[0, 1].plot(x2, scaled_pdf2, color='black', linewidth=2.5)


# --- Version 3: Heights of Mixed Plant Species ---
# Parameters for the two groups
loc3_a, scale3_a, size3_a = 32, 3, 500
loc3_b, scale3_b, size3_b = 53, 4, 500
total_samples3 = size3_a + size3_b

# Create data
heights_species_a = np.random.normal(loc=loc3_a, scale=scale3_a, size=size3_a)
heights_species_b = np.random.normal(loc=loc3_b, scale=scale3_b, size=size3_b)
data3 = np.concatenate([heights_species_a, heights_species_b])

# Plot histogram and get bin info
n3, bins3, _ = axes[1, 0].hist(data3, bins=bin_count, alpha=alpha, color=colors[2], edgecolor='black')
axes[1, 0].set_title("Heights of Mixed Plant Species")
axes[1, 0].set_xlabel("Plant Height (cm)")
axes[1, 0].set_ylabel("Number of Plants")

# Generate and plot the correct bimodal curve
x3 = np.linspace(data3.min(), data3.max(), 500)
pdf3_a = norm.pdf(x3, loc=loc3_a, scale=scale3_a) * size3_a / total_samples3
pdf3_b = norm.pdf(x3, loc=loc3_b, scale=scale3_b) * size3_b / total_samples3
combined_pdf3 = pdf3_a + pdf3_b
# Scale PDF to match histogram frequency
bin_width3 = bins3[1] - bins3[0]
scaled_pdf3 = combined_pdf3 * total_samples3 * bin_width3
axes[1, 0].plot(x3, scaled_pdf3, color='black', linewidth=2.5)


# --- Version 4: Customer Satisfaction Scores for Two Product Versions ---
# Parameters for the two groups
loc4_a, scale4_a, size4_a = 4.5, 1.0, 350
loc4_b, scale4_b, size4_b = 8.5, 0.8, 650
total_samples4 = size4_a + size4_b

# Create data
scores_old_version = np.random.normal(loc=loc4_a, scale=scale4_a, size=size4_a)
scores_new_version = np.random.normal(loc=loc4_b, scale=scale4_b, size=size4_b)
data4 = np.concatenate([scores_old_version, scores_new_version])
data4 = np.clip(data4, 1, 10)

# Plot histogram and get bin info
n4, bins4, _ = axes[1, 1].hist(data4, bins=10, alpha=alpha, color=colors[3], edgecolor='black')
axes[1, 1].set_title("Customer Satisfaction Scores")
axes[1, 1].set_xlabel("Customer Satisfaction Score (1-10)")
axes[1, 1].set_ylabel("Number of Customers")

# Generate and plot the correct bimodal curve
x4 = np.linspace(data4.min(), data4.max(), 500)
pdf4_a = norm.pdf(x4, loc=loc4_a, scale=scale4_a) * size4_a / total_samples4
pdf4_b = norm.pdf(x4, loc=loc4_b, scale=scale4_b) * size4_b / total_samples4
combined_pdf4 = pdf4_a + pdf4_b
# Scale PDF to match histogram frequency
bin_width4 = bins4[1] - bins4[0]
scaled_pdf4 = combined_pdf4 * total_samples4 * bin_width4
axes[1, 1].plot(x4, scaled_pdf4, color='black', linewidth=2.5)


# Adjust layout and save the figure
plt.tight_layout(rect=[0, 0.03, 1, 0.96]) # Adjust rect to make space for suptitle
plt.savefig("bimodal_histograms_with_curves.png", dpi=300, bbox_inches='tight')
plt.show()