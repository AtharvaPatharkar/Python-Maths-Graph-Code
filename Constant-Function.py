import numpy as np
import matplotlib.pyplot as plt

# Define the constant function
def constant_function(x, c=5):
    return np.full_like(x, c)

# Set up x values
x = np.linspace(-10, 10, 11)  # fewer points to easily print them
c = 5  # constant value

# Get corresponding y values
y = constant_function(x, c)

# Print function name
print("Function: Constant Function")
print(f"Equation: f(x) = {c}")

# Print some (x, f(x)) values
print("Sample points:")
for xi, yi in zip(x, y):
    print(f"f({xi}) = {yi}")

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=f'f(x) = {c}', color='blue', marker='o')
plt.title('Constant Function: f(x) = c')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
