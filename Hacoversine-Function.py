import numpy as np
import matplotlib.pyplot as plt

# Define the hacoversine function
def hacoversine_function(x):
    return (1 + np.cos(x)) / 2  # y = (1 + cos(x)) / 2

# Print the equation for the hacoversine function
print("Hacoversine Function:")
print("Equation: y = hacovers(x) = (1 + cos(x)) / 2")

# Generate x values for the hacoversine function
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 500)  # Domain: -2π to 2π

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x_vals, hacoversine_function(x_vals), label='y = hacovers(x)', color='green')
plt.title('Hacoversine Function: y = hacovers(x)')
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
