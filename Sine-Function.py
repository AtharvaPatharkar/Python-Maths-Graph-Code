import numpy as np
import matplotlib.pyplot as plt

# Define the sine function
def sine_function(x):
    return np.sin(x)

# Print the equation for the sine function
print("Sine Function:")
print("Equation: y = sin(x)")

# Generate x values for the sine function
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 500)  # Domain: -2π to 2π

# Create the plot
plt.figure(figsize=(8, 4))
plt.plot(x_vals, sine_function(x_vals), label='y = sin(x)', color='b')
plt.title('Sine Function: y = sin(x)')
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.xlim(-2 * np.pi, 2 * np.pi)
plt.ylim(-1.5, 1.5)

# Display the plot
plt.show()
