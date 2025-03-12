import numpy as np
import matplotlib.pyplot as plt

# Define the floor function
def floor_function(x):
    return np.floor(x)

# Generate x values for the floor function
x_vals = np.linspace(-5, 5, 1000)  # From -5 to 5
y_vals = floor_function(x_vals)

# Print the equation for the floor function
print("Floor Function:")
print("Equation: y = ⌊x⌋")

# Create the plot
plt.figure(figsize=(10, 5))
plt.step(x_vals, y_vals, label='Floor Function', color='green', where='post')
plt.title('Floor Function: y = ⌊x⌋')
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
