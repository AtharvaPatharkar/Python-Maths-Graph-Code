import numpy as np
import matplotlib.pyplot as plt

# Define the excosecant function
def excosecant_function(x):
    return 1 / np.sin(x) - 1  # y = csc(x) - 1

# Print the equation for the excosecant function
print("Excosecant Function:")
print("Equation: y = excsc(x) = csc(x) - 1")

# Generate x values for the excosecant function
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 500)  # Domain: -2π to 2π

# Avoid asymptotes by excluding points where csc(x) is undefined
x_vals = x_vals[np.abs(x_vals % np.pi) != 0]  # Exclude multiples of π

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x_vals, excosecant_function(x_vals), label='y = excsc(x)', color='green')
plt.title('Excosecant Function: y = excsc(x)')
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
