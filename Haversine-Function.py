import numpy as np
import matplotlib.pyplot as plt

# Define the haversine function
def haversine_function(x):
    return (1 - np.cos(x)) / 2  # y = (1 - cos(x)) / 2

# Print the equation for the haversine function
print("Haversine Function:")
print("Equation: y = havers(x) = (1 - cos(x)) / 2")

# Generate x values for the haversine function
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 500)  # Domain: -2π to 2π

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x_vals, haversine_function(x_vals), label='y = havers(x)', color='red')
plt.title('Haversine Function: y = havers(x)')
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.ylim(-0.1, 1.1)  # Limit y-axis to show relevant range
plt.xlim(-2 * np.pi, 2 * np.pi)

# Display the plot
plt.legend()
plt.show()
