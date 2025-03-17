import numpy as np
import matplotlib.pyplot as plt

# Define the Gudermannian function
def gudermannian_function(x):
    return np.arctan(np.sin(x))

# Print the equation for the Gudermannian function
print("Gudermannian Function:")
print("Equation: y = gd(x) = arctan(sin(x))")

# Generate x values for the Gudermannian function
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 500)  # Domain: -2π to 2π

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x_vals, gudermannian_function(x_vals), label='y = gd(x)', color='purple')
plt.title('Gudermannian Function: y = gd(x)')
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.ylim(-1.5, 1.5)  # Limit y-axis to show relevant range
plt.xlim(-2 * np.pi, 2 * np.pi)

# Display the plot
plt.legend()
plt.show()
