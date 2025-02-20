import numpy as np
import matplotlib.pyplot as plt

# Define the ceiling function
def ceiling_function(x):
    return np.ceil(x)

# Generate x values for plotting
x_vals = np.linspace(-5, 5, 1000)  # From -5 to 5
y_vals = ceiling_function(x_vals)

# Print the equation for the ceiling function
print("Ceiling Function:")
print("Equation: y = ⌈x⌉")

# Create the plot
plt.figure(figsize=(10, 5))
plt.step(x_vals, y_vals, label='Ceiling Function', color='blue', where='post')
plt.title('Ceiling Function: y = ⌈x⌉')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.ylim(-6, 6)  # Limit y-axis to show relevant range
plt.xlim(-5, 5)

# Display the plot
plt.legend()
plt.show()
