import numpy as np
import matplotlib.pyplot as plt

# Define the cosine function
def cosine_function(x):
    return np.cos(x)

# Print the equation for the cosine function
print("Cosine Function:")
print("Equation: y = cos(x)")

# Generate x values for the cosine function
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 500)  # Domain: -2Ï€ to 2Ï€

# Create the plot
plt.figure(figsize=(8, 4))
plt.plot(x_vals, cosine_function(x_vals), label='y = cos(x)', color='g')
plt.title('Cosine Function: y = cos(x)')
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.xlim(-2 * np.pi, 2 * np.pi)
plt.ylim(-1.5, 1.5)

# Display the plot
plt.show()
