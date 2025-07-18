import numpy as np
import matplotlib.pyplot as plt

# Define the function sin(x) + sin(2x)
def sine_sum(x):
    return np.sin(x) + np.sin(2*x)

# Generate x values from -2π to 2π for plotting
x_values = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Calculate the y values for the function sin(x) + sin(2x)
y_values = sine_sum(x_values)

# Plotting the function sin(x) + sin(2x)
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, label=r"$f(x) = \sin(x) + \sin(2x)$", color='b')

# Add title and labels
plt.title("Function: $f(x) = \\sin(x) + \\sin(2x)$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)

# Show legend
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()
