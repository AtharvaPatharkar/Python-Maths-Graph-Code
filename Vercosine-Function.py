import numpy as np
import matplotlib.pyplot as plt

# Define the vercosine function
def vercosine_function(x):
    return 1 - np.sin(x)  # y = 1 - sin(x)

# Print the equation for the vercosine function
print("Vercosine Function:")
print("Equation: y = vercos(x) = 1 - sin(x)")

# Generate x values for the vercosine function
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 500)  # Domain: -2π to 2π

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x_vals, vercosine_function(x_vals), label='y = vercos(x)', color='purple')
plt.title('Vercosine Function: y = vercos(x)')
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
