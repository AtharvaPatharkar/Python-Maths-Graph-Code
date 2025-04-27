import numpy as np
import matplotlib.pyplot as plt

# Define the versine function
def versine_function(x):
    return 1 - np.cos(x)  # y = 1 - cos(x)

# Print the equation for the versine function
print("Versine Function:")
print("Equation: y = vers(x) = 1 - cos(x)")

# Generate x values for the versine function
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 500)  # Domain: -2π to 2π

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x_vals, versine_function(x_vals), label='y = vers(x)', color='orange')
plt.title('Versine Function: y = vers(x)')
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.ylim(-1, 2)  # Limit y-axis to show relevant range
plt.xlim(-2 * np.pi, 2 * np.pi)

# Display the plot
plt.legend()
plt.show()
