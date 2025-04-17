import numpy as np
import matplotlib.pyplot as plt

# Define the tangent function
def tangent_function(x):
    return np.tan(x)

# Print the equation for the tangent function
print("Tangent Function:")
print("Equation: y = tan(x)")

# Generate x values for the tangent function
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 500)  # Domain: -2π to 2π

# Avoid asymptotes by excluding points where tan(x) is undefined
x_vals = x_vals[np.abs(x_vals) % (np.pi / 2) != 0]

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x_vals, tangent_function(x_vals), label='y = tan(x)', color='orange')
plt.title('Tangent Function: y = tan(x)')
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.ylim(-10, 10)  # Limit y-axis to avoid large values
plt.xlim(-2 * np.pi, 2 * np.pi)

# Display the plot
plt.legend()
plt.show()
