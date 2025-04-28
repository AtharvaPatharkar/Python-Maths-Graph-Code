import numpy as np
import matplotlib.pyplot as plt

# Define the line equation function
def line_equation(x, m, c):
    return m * x + c

# Set the slope (m) and intercept (c)
m = 2    # Example: slope = 2
c = 3    # Example: y-intercept = 3

# Generate x values
x = np.linspace(-10, 10, 400)  # From -10 to 10

# Calculate y values
y = line_equation(x, m, c)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f'y = {m}x + {c}', color='blue')
plt.title('Graph of Line Equation')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis
plt.grid(True)
plt.legend()
plt.show()
