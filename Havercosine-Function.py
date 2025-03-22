import numpy as np
import matplotlib.pyplot as plt

# Define the havercosine function
def havercosine_function(x):
    return (1 + np.cos(x)) / 2  # y = (1 + cos(x)) / 2

# Print the equation for the havercosine function
print("Havercosine Function:")
print("Equation: y = havercos(x) = (1 + cos(x)) / 2")

# Generate x values for the havercosine function
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 500)  # Domain: -2π to 2π

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x_vals, havercosine_function(x_vals), label='y = havercos(x)', color='blue')
plt.title('Havercosine Function: y = havercos(x)')
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
