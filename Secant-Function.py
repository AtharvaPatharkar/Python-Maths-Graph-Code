import numpy as np
import matplotlib.pyplot as plt

# Define the secant function
def secant_function(x):
    return 1 / np.cos(x)

# Print the equation for the secant function
print("Secant Function:")
print("Equation: y = sec(x)")

# Generate x values for the secant function
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 500)  # Domain: -2π to 2π

# Avoid asymptotes by excluding points where sec(x) is undefined
x_vals = x_vals[np.abs(x_vals % np.pi) != np.pi / 2]  # Exclude odd multiples of π/2

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x_vals, secant_function(x_vals), label='y = sec(x)', color='orange')
plt.title('Secant Function: y = sec(x)')
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
