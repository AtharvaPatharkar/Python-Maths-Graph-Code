import numpy as np
import matplotlib.pyplot as plt

# Define power functions
def power_function(x, n):
    return x ** n

# Print the equations
n_values = [2, 3, -1, 0.5]  # Example powers: x^2, x^3, x^(-1), x^(1/2)
print("Power Functions:")
for n in n_values:
    print(f"Power Function Equation: y = x^{n}")

# Generate x values for power functions (domain: (-10, 10), excluding zero for negative powers)
x_vals_positive = np.linspace(0.01, 10, 500)  # Positive x values for all powers
x_vals_negative = np.linspace(-10, 10, 500)  # Negative x values for odd powers

# Create plots
plt.figure(figsize=(15, 5))

# Plot for n = 2 (x^2)
plt.subplot(1, 4, 1)
plt.plot(x_vals_positive, power_function(x_vals_positive, 2), label='y = x^2', color='b')
plt.title('Power Function: y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Plot for n = 3 (x^3)
plt.subplot(1, 4, 2)
plt.plot(x_vals_positive, power_function(x_vals_positive, 3), label='y = x^3', color='g')
plt.title('Power Function: y = x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Plot for n = -1 (x^(-1))
plt.subplot(1, 4, 3)
plt.plot(x_vals_positive, power_function(x_vals_positive, -1), label='y = x^(-1)', color='orange')
plt.title('Power Function: y = x^(-1)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Plot for n = 1/2 (x^(1/2))
plt.subplot(1, 4, 4)
plt.plot(x_vals_positive, power_function(x_vals_positive, 0.5), label='y = x^(1/2)', color='purple')
plt.title('Power Function: y = x^(1/2)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Display the plots
plt.tight_layout()
plt.show()
