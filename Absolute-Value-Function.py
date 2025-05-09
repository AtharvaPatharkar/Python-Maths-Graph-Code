import numpy as np
import matplotlib.pyplot as plt

# Define the absolute value function
def absolute_value_function(x):
    return np.abs(x)

# Set up x values
x = np.linspace(-10, 10, 21)  # 21 points from -10 to 10

# Get corresponding y values
y = absolute_value_function(x)

# Print function name and equation
print("Function: Absolute Value Function")
print("Equation: f(x) = |x|")

# Print sample (x, f(x)) points
print("Sample points:")
for xi, yi in zip(x, y):
    print(f"f({xi}) = {yi}")

# Plotting the graph
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='f(x) = |x|', color='orange', marker='o')
plt.title('Absolute Value Function: f(x) = |x|')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.5)  # Draw x-axis
plt.axvline(0, color='black', linewidth=0.5)  # Draw y-axis
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
