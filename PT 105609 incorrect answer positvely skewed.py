import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Negatively Skewed Histograms with Incorrect Positively Skewed Curves", fontsize=16)

# Common settings for all histograms
num_samples = 1000
bin_count = 15
alpha = 0.7  # Transparency for histograms
neg_skewness = -5  # Negative skewness parameter for data
pos_skewness = 5    # Positive skewness parameter for incorrect curves
curve_color = 'black'
curve_linewidth = 2

# Custom colors from hex codes
colors = ['#838EF0', '#19C9D6', '#FAC88C', '#E69BA6']

# --- Version 1: Scores on an Easy Test ---
# Parameters for negatively skewed test scores (peaking around 90)
a1, loc1, scale1 = neg_skewness, 90, 5  
data1 = skewnorm.rvs(a1, loc=loc1, scale=scale1, size=num_samples)
data1 = np.clip(data1, 60, 100)
counts1, bins1, _ = axes[0, 0].hist(data1, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
# Incorrect positive skew curve
x1 = np.linspace(data1.min(), data1.max(), 1000)
pdf1_incorrect = skewnorm.pdf(x1, pos_skewness, loc=70, scale=8)  # Peaking left
axes[0, 0].plot(x1, pdf1_incorrect*np.max(counts1)/np.max(pdf1_incorrect), 
                color=curve_color, linewidth=curve_linewidth)
axes[0, 0].set_title("Scores on an Easy Test")
axes[0, 0].set_xlabel("Test Scores")
axes[0, 0].set_ylabel("Number of Students")

# --- Version 2: Age of Retirement ---
# Parameters for retirement ages (peaking around 65)
a2, loc2, scale2 = neg_skewness, 65, 5  
data2 = skewnorm.rvs(a2, loc=loc2, scale=scale2, size=num_samples)
data2 = np.clip(data2, 50, 80)
counts2, bins2, _ = axes[0, 1].hist(data2, bins=bin_count, alpha=alpha, color=colors[1], edgecolor='black')
# Incorrect positive skew curve
x2 = np.linspace(data2.min(), data2.max(), 1000)
pdf2_incorrect = skewnorm.pdf(x2, pos_skewness, loc=55, scale=6)  # Peaking left
axes[0, 1].plot(x2, pdf2_incorrect*np.max(counts2)/np.max(pdf2_incorrect), 
                color=curve_color, linewidth=curve_linewidth)
axes[0, 1].set_title("Age of Retirement")
axes[0, 1].set_xlabel("Age (Years)")
axes[0, 1].set_ylabel("Number of Professionals")

# --- Version 3: Lifespan of a Durable Product ---
# Parameters for product lifespans (peaking around 12 years)
a3, loc3, scale3 = neg_skewness, 12, 2  
data3 = skewnorm.rvs(a3, loc=loc3, scale=scale3, size=num_samples)
data3 = np.clip(data3, 5, 20)
counts3, bins3, _ = axes[1, 0].hist(data3, bins=bin_count, alpha=alpha, color=colors[2], edgecolor='black')
# Incorrect positive skew curve
x3 = np.linspace(data3.min(), data3.max(), 1000)
pdf3_incorrect = skewnorm.pdf(x3, pos_skewness, loc=8, scale=3)  # Peaking left
axes[1, 0].plot(x3, pdf3_incorrect*np.max(counts3)/np.max(pdf3_incorrect), 
                color=curve_color, linewidth=curve_linewidth)
axes[1, 0].set_title("Lifespan of a Durable Product")
axes[1, 0].set_xlabel("Lifespan (Years)")
axes[1, 0].set_ylabel("Number of Products")

# --- Version 4: Player Scores in a Video Game ---
# Parameters for video game scores (peaking around 9000)
a4, loc4, scale4 = neg_skewness, 9000, 1000  
data4 = skewnorm.rvs(a4, loc=loc4, scale=scale4, size=num_samples)
data4 = np.clip(data4, 6000, 11000)
counts4, bins4, _ = axes[1, 1].hist(data4, bins=bin_count, alpha=alpha, color=colors[3], edgecolor='black')
# Incorrect positive skew curve
x4 = np.linspace(data4.min(), data4.max(), 1000)
pdf4_incorrect = skewnorm.pdf(x4, pos_skewness, loc=7000, scale=1200)  # Peaking left
axes[1, 1].plot(x4, pdf4_incorrect*np.max(counts4)/np.max(pdf4_incorrect), 
                color=curve_color, linewidth=curve_linewidth)
axes[1, 1].set_title("Player Scores in a Video Game")
axes[1, 1].set_xlabel("Player Score (Points)")
axes[1, 1].set_ylabel("Number of Players")

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("negatively_skewed_histograms_with_incorrect_curves.png", dpi=300, bbox_inches='tight')
plt.show()