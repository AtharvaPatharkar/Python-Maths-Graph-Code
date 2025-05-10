import numpy as np
import matplotlib.pyplot as plt

# Define the absolute value piecewise function
def absolute_value_piecewise(x):
    return np.where(x >= 0, x, -x)

# Set up x values
x = np.linspace(-10, 10, 21)  # 21 points from -10 to 10

# Get corresponding y values
y = absolute_value_piecewise(x)

# Print function name and equation
print("Function: Absolute Value Piecewise Function")
print("Equation: f(x) = x if x >= 0, -x if x < 0")

# Print sample (x, f(x)) points
print("Sample points:")
for xi, yi in zip(x, y):
    print(f"f({xi}) = {yi}")

# Plotting the graph
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='f(x) = piecewise(|x|)', color='red', marker='o')
plt.title('Absolute Value Piecewise Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.5)  # Draw x-axis
plt.axvline(0, color='black', linewidth=0.5)  # Draw y-axis
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
