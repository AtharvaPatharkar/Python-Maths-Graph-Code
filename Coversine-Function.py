import numpy as np
import matplotlib.pyplot as plt

# Define the coversine function
def coversine_function(x):
    return np.sin(x / 2) ** 2  # y = sin^2(x / 2)

# Print the equation for the coversine function
print("Coversine Function:")
print("Equation: y = covers(x) = sin^2(x / 2)")

# Generate x values for the coversine function
x_vals = np.linspace(-4 * np.pi, 4 * np.pi, 500)  # Domain: -4Ï€ to 4Ï€

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x_vals, coversine_function(x_vals), label='y = covers(x)', color='blue')
plt.title('Coversine Function: y = covers(x)')
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.ylim(-0.1, 1.1)  # Limit y-axis to show relevant range
plt.xlim(-4 * np.pi, 4 * np.pi)

# Display the plot
plt.legend()
plt.show()
