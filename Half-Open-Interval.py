import numpy as np
import matplotlib.pyplot as plt

# Define the half-open intervals
a, b = 2, 5  # For interval [2, 5)
c, d = 2, 5  # For interval (2, 5]

# Generate x values for plotting
x_vals = np.linspace(1.5, 6, 1000)  # Range from 1.5 to 6

# Create the plot
plt.figure(figsize=(10, 5))

# Plot the half-open interval [a, b)
plt.fill_between(x_vals, 0, 1, where=(x_vals >= a) & (x_vals < b), color='blue', alpha=0.5, label='[2, 5)')

# Plot the half-open interval (c, d]
plt.fill_between(x_vals, 0, 1, where=(x_vals > c) & (x_vals <= d), color='orange', alpha=0.5, label='(2, 5]')

# Mark the endpoints
plt.scatter([a, b], [1, 1], color='blue', zorder=5)
plt.scatter([c, d], [1, 1], color='orange', zorder=5)

# Annotate the endpoints
plt.text(a, 1.02, '2', fontsize=12, ha='center')
plt.text(b, 1.02, '5', fontsize=12, ha='center', color='blue')
plt.text(c, 1.02, '2', fontsize=12, ha='center', color='orange')
plt.text(d, 1.02, '5', fontsize=12, ha='center', color='orange')

# Set limits and labels
plt.xlim(1.5, 6)
plt.ylim(0, 1.5)
plt.axhline(0, color='black', linewidth=0.5)
plt.title('Half-Open Intervals')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()

# Show the plot
plt.show()

# Print the interval equations
print("Half-Open Intervals:")
print("[2, 5) includes 2 but not 5.")
print("(2, 5] includes 5 but not 2.")
