import numpy as np
import matplotlib.pyplot as plt

# Define the arccosine function
def arccosine_function(x):
    return np.arccos(x)

# Set up x values (only for the valid range [-1, 1])
x = np.linspace(-1, 1, 100)  # 100 points from -1 to 1

# Get corresponding y values
y = arccosine_function(x)

# Print function name and equation
print("Function: Arccosine Function")
print("Equation: f(x) = arccos(x)")

# Print some (x, f(x)) points
print("Sample points:")
for xi, yi in zip(x, y):
    print(f"f({xi}) = {yi}")

# Plotting the graph
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='f(x) = arccos(x)', color='blue')
plt.title('Arccosine Function: f(x) = arccos(x)')
plt.xlabel('x')
plt.ylabel('f(x) (in radians)')
plt.axhline(0, color='black', linewidth=0.5)  # Draw x-axis
plt.axvline(0, color='black', linewidth=0.5)  # Draw y-axis
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
