import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm, norm

# Set a random seed for reproducibility
np.random.seed(42)

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Negatively Skewed Histograms with Centered Normal Distribution Curves", fontsize=16)

# Common settings for all histograms
num_samples = 1000
bin_count = 15
alpha = 0.7  # Transparency for histograms
skewness = -5  # Negative skewness parameter
curve_color = 'black'
curve_linewidth = 2

# Custom colors from hex codes
colors = ['#838EF0', '#19C9D6', '#FAC88C', '#E69BA6']

# --- Version 1: Scores on an Easy Test ---
a1, loc1, scale1 = skewness, 90, 5  
data1 = skewnorm.rvs(a1, loc=loc1, scale=scale1, size=num_samples)
data1 = np.clip(data1, 60, 100)
counts1, bins1, _ = axes[0, 0].hist(data1, bins=bin_count, alpha=alpha, color=colors[0], edgecolor='black')
# Centered normal curve
x1 = np.linspace(60, 100, 1000)
mid_point1 = (60 + 100) / 2
pdf1_incorrect = norm.pdf(x1, loc=mid_point1, scale=10)  # Centered exactly in middle
axes[0, 0].plot(x1, pdf1_incorrect*np.max(counts1)/np.max(pdf1_incorrect), 
                color=curve_color, linewidth=curve_linewidth)
axes[0, 0].set_title("Scores on an Easy Test")
axes[0, 0].set_xlabel("Test Scores")
axes[0, 0].set_ylabel("Number of Students")

# --- Version 2: Age of Retirement ---
a2, loc2, scale2 = skewness, 65, 5  
data2 = skewnorm.rvs(a2, loc=loc2, scale=scale2, size=num_samples)
data2 = np.clip(data2, 50, 80)
counts2, bins2, _ = axes[0, 1].hist(data2, bins=bin_count, alpha=alpha, color=colors[1], edgecolor='black')
# Centered normal curve
x2 = np.linspace(50, 80, 1000)
mid_point2 = (50 + 80) / 2
pdf2_incorrect = norm.pdf(x2, loc=mid_point2, scale=7)  # Centered exactly in middle
axes[0, 1].plot(x2, pdf2_incorrect*np.max(counts2)/np.max(pdf2_incorrect), 
                color=curve_color, linewidth=curve_linewidth)
axes[0, 1].set_title("Age of Retirement")
axes[0, 1].set_xlabel("Age (Years)")
axes[0, 1].set_ylabel("Number of Professionals")

# --- Version 3: Lifespan of a Durable Product ---
a3, loc3, scale3 = skewness, 12, 2  
data3 = skewnorm.rvs(a3, loc=loc3, scale=scale3, size=num_samples)
data3 = np.clip(data3, 5, 20)
counts3, bins3, _ = axes[1, 0].hist(data3, bins=bin_count, alpha=alpha, color=colors[2], edgecolor='black')
# Centered normal curve
x3 = np.linspace(5, 20, 1000)
mid_point3 = (5 + 20) / 2
pdf3_incorrect = norm.pdf(x3, loc=mid_point3, scale=3)  # Centered exactly in middle
axes[1, 0].plot(x3, pdf3_incorrect*np.max(counts3)/np.max(pdf3_incorrect), 
                color=curve_color, linewidth=curve_linewidth)
axes[1, 0].set_title("Lifespan of a Durable Product")
axes[1, 0].set_xlabel("Lifespan (Years)")
axes[1, 0].set_ylabel("Number of Products")

# --- Version 4: Player Scores in a Video Game ---
a4, loc4, scale4 = skewness, 9000, 1000  
data4 = skewnorm.rvs(a4, loc=loc4, scale=scale4, size=num_samples)
data4 = np.clip(data4, 6000, 11000)
counts4, bins4, _ = axes[1, 1].hist(data4, bins=bin_count, alpha=alpha, color=colors[3], edgecolor='black')
# Centered normal curve
x4 = np.linspace(6000, 11000, 1000)
mid_point4 = (6000 + 11000) / 2
pdf4_incorrect = norm.pdf(x4, loc=mid_point4, scale=1200)  # Centered exactly in middle
axes[1, 1].plot(x4, pdf4_incorrect*np.max(counts4)/np.max(pdf4_incorrect), 
                color=curve_color, linewidth=curve_linewidth)
axes[1, 1].set_title("Player Scores in a Video Game")
axes[1, 1].set_xlabel("Player Score (Points)")
axes[1, 1].set_ylabel("Number of Players")

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("negatively_skewed_histograms_with_centered_normal_curves.png", dpi=300, bbox_inches='tight')
plt.show()