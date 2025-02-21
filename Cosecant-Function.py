import numpy as np
import matplotlib.pyplot as plt

# Define the cosecant function
def cosecant_function(x):
    return 1 / np.sin(x)

# Print the equation for the cosecant function
print("Cosecant Function:")
print("Equation: y = csc(x)")

# Generate x values for the cosecant function
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 500)  # Domain: -2π to 2π

# Avoid asymptotes by excluding points where csc(x) is undefined
x_vals = x_vals[np.abs(x_vals % np.pi) != 0]  # Exclude multiples of π

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x_vals, cosecant_function(x_vals), label='y = csc(x)', color='blue')
plt.title('Cosecant Function: y = csc(x)')
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
