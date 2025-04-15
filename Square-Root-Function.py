import numpy as np
import matplotlib.pyplot as plt

# Define the square root function
def sqrt_function(x):
    return np.sqrt(x)

# Print the square root equation
print("Square Root Equation: y = sqrt(x)")

# Generate x values (we'll use only positive x values since sqrt(x) is defined for x >= 0)
x_vals = np.linspace(0, 25, 500)

# Compute corresponding y values
y_vals = sqrt_function(x_vals)

# ---- Finding key points ----
# At x = 0, y = sqrt(0) = 0
# Let's also consider a few other key points for the square root function
key_points = [0, 1, 4, 9, 16, 25]

# Print key points
print("\nKey Points (x, y):")
for point in key_points:
    y_val = sqrt_function(point)
    print(f"x = {point}, y = {y_val:.2f}")

# ---- Plot the square root function ----
plt.plot(x_vals, y_vals, label='y = sqrt(x)', color='b')

# Mark key points on the graph
for point in key_points:
    plt.plot(point, sqrt_function(point), 'ro', label=f'({point}, {sqrt_function(point):.2f})', markersize=8)

# Add labels and title
plt.title('Square Root Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Add a legend
plt.legend()

# Show a grid
plt.grid(True)

# Display the plot
plt.show()
