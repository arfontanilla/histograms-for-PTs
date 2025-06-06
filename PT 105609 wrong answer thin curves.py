import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Histograms with Incorrectly Thin Curves", fontsize=16)

# Common settings for all histograms
num_samples = 1000
bin_count = 15
alpha = 0.7  # Transparency for histograms
skewness = -5  # Negative skewness parameter

# Custom colors from hex codes
colors = ['#838EF0', '#19C9D6', '#FAC88C', '#E69BA6']

# --- Version 1: Scores on an Easy Test ---
# Parameters for negatively skewed test scores (peaking around 90)
a1, loc1, scale1 = skewness, 90, 5
data1 = skewnorm.rvs(a1, loc=loc1, scale=scale1, size=num_samples)
data1 = np.clip(data1, 60, 100)  # Clip scores between 60 and 100

# Plot histogram and get bin information
n1, bins1, _ = axes[0, 0].hist(data1, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
axes[0, 0].set_title("Scores on an Easy Test")
axes[0, 0].set_xlabel("Test Scores")
axes[0, 0].set_ylabel("Number of Students")

# Generate and plot the incorrect, overly thin curve
incorrect_scale1 = 1.5  # Much smaller scale to make the curve thin
x1 = np.linspace(data1.min(), data1.max(), 500)
pdf1 = skewnorm.pdf(x1, a=a1, loc=loc1, scale=incorrect_scale1)
# Scale PDF to match the frequency y-axis
bin_width1 = bins1[1] - bins1[0]
scaled_pdf1 = pdf1 * num_samples * bin_width1
axes[0, 0].plot(x1, scaled_pdf1, color='black', linewidth=2.5)


# --- Version 2: Age of Retirement ---
# Parameters for retirement ages (peaking around 65)
a2, loc2, scale2 = skewness, 65, 5
data2 = skewnorm.rvs(a2, loc=loc2, scale=scale2, size=num_samples)
data2 = np.clip(data2, 50, 80)  # Clip ages between 50 and 80

# Plot histogram and get bin information
n2, bins2, _ = axes[0, 1].hist(data2, bins=bin_count, alpha=alpha, color=colors[1], edgecolor='black')
axes[0, 1].set_title("Age of Retirement")
axes[0, 1].set_xlabel("Age (Years)")
axes[0, 1].set_ylabel("Number of Professionals")

# Generate and plot the incorrect, overly thin curve
incorrect_scale2 = 1.5 # Much smaller scale
x2 = np.linspace(data2.min(), data2.max(), 500)
pdf2 = skewnorm.pdf(x2, a=a2, loc=loc2, scale=incorrect_scale2)
# Scale PDF to match the frequency y-axis
bin_width2 = bins2[1] - bins2[0]
scaled_pdf2 = pdf2 * num_samples * bin_width2
axes[0, 1].plot(x2, scaled_pdf2, color='black', linewidth=2.5)


# --- Version 3: Lifespan of a Durable Product ---
# Parameters for product lifespans (peaking around 12 years)
a3, loc3, scale3 = skewness, 12, 2
data3 = skewnorm.rvs(a3, loc=loc3, scale=scale3, size=num_samples)
data3 = np.clip(data3, 5, 20)  # Clip lifespans between 5 and 20 years

# Plot histogram and get bin information
n3, bins3, _ = axes[1, 0].hist(data3, bins=bin_count, alpha=alpha, color=colors[2], edgecolor='black')
axes[1, 0].set_title("Lifespan of a Durable Product")
axes[1, 0].set_xlabel("Lifespan (Years)")
axes[1, 0].set_ylabel("Number of Products")

# Generate and plot the incorrect, overly thin curve
incorrect_scale3 = 0.5 # Much smaller scale
x3 = np.linspace(data3.min(), data3.max(), 500)
pdf3 = skewnorm.pdf(x3, a=a3, loc=loc3, scale=incorrect_scale3)
# Scale PDF to match the frequency y-axis
bin_width3 = bins3[1] - bins3[0]
scaled_pdf3 = pdf3 * num_samples * bin_width3
axes[1, 0].plot(x3, scaled_pdf3, color='black', linewidth=2.5)


# --- Version 4: Player Scores in a Video Game ---
# Parameters for video game scores (peaking around 9000)
a4, loc4, scale4 = skewness, 9000, 1000
data4 = skewnorm.rvs(a4, loc=loc4, scale=scale4, size=num_samples)
data4 = np.clip(data4, 6000, 11000)  # Clip scores between 6000 and 11000

# Plot histogram and get bin information
n4, bins4, _ = axes[1, 1].hist(data4, bins=bin_count, alpha=alpha, color=colors[3], edgecolor='black')
axes[1, 1].set_title("Player Scores in a Video Game")
axes[1, 1].set_xlabel("Player Score (Points)")
axes[1, 1].set_ylabel("Number of Players")

# Generate and plot the incorrect, overly thin curve
incorrect_scale4 = 300 # Much smaller scale
x4 = np.linspace(data4.min(), data4.max(), 500)
pdf4 = skewnorm.pdf(x4, a=a4, loc=loc4, scale=incorrect_scale4)
# Scale PDF to match the frequency y-axis
bin_width4 = bins4[1] - bins4[0]
scaled_pdf4 = pdf4 * num_samples * bin_width4
axes[1, 1].plot(x4, scaled_pdf4, color='black', linewidth=2.5)


# Adjust layout and save the figure
plt.tight_layout(rect=[0, 0.03, 1, 0.96]) # Adjust rect to make space for suptitle
plt.savefig("histograms_with_incorrect_curves.png", dpi=300, bbox_inches='tight')
plt.show()