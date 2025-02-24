import numpy as np
import matplotlib.pyplot as plt

# Define the covercosine function
def covercosine_function(x):
    return np.cos(x / 2) ** 2  # y = cos^2(x / 2)

# Print the equation for the covercosine function
print("Covercosine Function:")
print("Equation: y = covercos(x) = cos^2(x / 2)")

# Generate x values for the covercosine function
x_vals = np.linspace(-4 * np.pi, 4 * np.pi, 500)  # Domain: -4π to 4π

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x_vals, covercosine_function(x_vals), label='y = covercos(x)', color='teal')
plt.title('Covercosine Function: y = covercos(x)')
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.ylim(-0.1, 1.1)  # Limit y-axis to show relevant range
plt.xlim(-4 * np.pi, 4 * np.pi)

# Display the plot
plt.legend()
plt.show()
