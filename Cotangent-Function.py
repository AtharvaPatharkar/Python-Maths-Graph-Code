import numpy as np
import matplotlib.pyplot as plt

# Define the cotangent function
def cotangent_function(x):
    return 1 / np.tan(x)

# Print the equation for the cotangent function
print("Cotangent Function:")
print("Equation: y = cot(x)")

# Generate x values for the cotangent function
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 500)  # Domain: -2Ï€ to 2Ï€

# Avoid asymptotes by excluding points where cot(x) is undefined
x_vals = x_vals[np.abs(x_vals) % np.pi != 0]  # Exclude multiples of Ï€

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x_vals, cotangent_function(x_vals), label='y = cot(x)', color='purple')
plt.title('Cotangent Function: y = cot(x)')
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
