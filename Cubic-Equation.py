import numpy as np
import matplotlib.pyplot as plt

# Define the coefficients of the cubic equation: y = ax^3 + bx^2 + cx + d
a = 1
b = -6
c = 11
d = -6

# Define the cubic function
def cubic_function(x):
    return a * x**3 + b * x**2 + c * x + d

# Print the cubic equation
print(f"Cubic Equation: y = {a}x^3 + {b}x^2 + {c}x + {d}")

# Generate x values (you can change the range of x as needed)
x_vals = np.linspace(-10, 10, 400)

# Compute corresponding y values
y_vals = cubic_function(x_vals)

# ---- Finding local minima and maxima ----
# The critical points occur when the first derivative equals zero: dy/dx = 3ax^2 + 2bx + c = 0
coefficients = [3*a, 2*b, c]
critical_points = np.roots(coefficients)

# Print critical points (local minima or maxima)
print("\nCritical Points (Local Minima/Maxima):")
for point in critical_points:
    y_critical = cubic_function(point)
    print(f"x = {point:.2f}, y = {y_critical:.2f}")

# ---- Finding roots ----
# The roots of the cubic equation are where y = 0
roots = np.roots([a, b, c, d])
print("\nRoots:")
for root in roots:
    print(f"x = {root.real:.2f}, y = 0")

# ---- Plot the cubic function ----
plt.plot(x_vals, y_vals, label=f'y = {a}x^3 + {b}x^2 + {c}x + {d}', color='b')

# Mark critical points (local minima/maxima)
for point in critical_points:
    plt.plot(point, cubic_function(point), 'ro', label=f'Critical Point ({point:.2f}, {cubic_function(point):.2f})', markersize=8)

# Mark the roots
for root in roots:
    plt.plot(root.real, 0, 'go', label=f'Root ({root.real:.2f}, 0)', markersize=8)

# Add labels and title
plt.title('Cubic Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Add a legend
plt.legend()

# Show a grid
plt.grid(True)

# Display the plot
plt.show()
