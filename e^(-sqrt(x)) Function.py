import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return np.exp(-np.sqrt(x))

# Define the x values (from 0 to 10)
x_values = np.linspace(0, 10, 100)
# Calculate the corresponding y values for the function
y_values = f(x_values)

# Print the function values for some selected x values
print("x value  |  f(x) value")
for x, y in zip(x_values[::10], y_values[::10]):  # Displaying every 10th point for readability
    print(f"{x:.2f}  |  {y:.4f}")

# Plot the graph
plt.plot(x_values, y_values, label=r'$f(x) = e^{-\sqrt{x}}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of $f(x) = e^{-\sqrt{x}}$')
plt.grid(True)
plt.legend()
plt.show()

