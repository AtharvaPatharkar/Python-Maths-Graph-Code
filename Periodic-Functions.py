import numpy as np
import matplotlib.pyplot as plt

# Define periodic functions
def sine_function(x):
    return np.sin(x)

def cosine_function(x):
    return np.cos(x)

# Print the equations for sine and cosine functions
print("Periodic Functions:")
print("1. Sine Function: y = sin(x)")
print("2. Cosine Function: y = cos(x)")

# Generate x values for periodic functions
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 500)  # Domain: -2π to 2π

# Create plots
plt.figure(figsize=(12, 6))

# Plot for sine function
plt.subplot(1, 2, 1)
plt.plot(x_vals, sine_function(x_vals), label='y = sin(x)', color='b')
plt.title('Sine Function: y = sin(x)')
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Plot for cosine function
plt.subplot(1, 2, 2)
plt.plot(x_vals, cosine_function(x_vals), label='y = cos(x)', color='g')
plt.title('Cosine Function: y = cos(x)')
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Display the plots
plt.tight_layout()
plt.show()
