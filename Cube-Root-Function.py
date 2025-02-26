import numpy as np
import matplotlib.pyplot as plt

# Define the cube root function
def cube_root_function(x):
    return np.cbrt(x)

# Print the cube root equation
print("Cube Root Equation: y = cbrt(x)")

# Generate x values (we'll use both positive and negative x values as cube root is defined for all real numbers)
x_vals = np.linspace(-25, 25, 500)

# Compute corresponding y values
y_vals = cube_root_function(x_vals)

# ---- Finding key points ----
# Cube root of a few key values: x = -8, -1, 0, 1, 8
key_points = [-8, -1, 0, 1, 8]

# Print key points
print("\nKey Points (x, y):")
for point in key_points:
    y_val = cube_root_function(point)
    print(f"x = {point}, y = {y_val:.2f}")

# ---- Plot the cube root function ----
plt.plot(x_vals, y_vals, label='y = cbrt(x)', color='b')

# Mark key points on the graph
for point in key_points:
    plt.plot(point, cube_root_function(point), 'ro', label=f'({point}, {cube_root_function(point):.2f})', markersize=8)

# Add labels and title
plt.title('Cube Root Function Plot')
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
