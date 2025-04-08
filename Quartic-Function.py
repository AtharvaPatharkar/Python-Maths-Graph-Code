import numpy as np
import matplotlib.pyplot as plt

# Define the coefficients of the quartic equation: y = ax^4 + bx^3 + cx^2 + dx + e
a = 1
b = -8
c = 18
d = -12
e = -3

# Define the quartic function
def quartic_function(x):
    return a * x**4 + b * x**3 + c * x**2 + d * x + e

# Print the quartic equation
print(f"Quartic Equation: y = {a}x^4 + {b}x^3 + {c}x^2 + {d}x + {e}")

# Generate x values (you can change the range of x as needed)
x_vals = np.linspace(-10, 10, 500)

# Compute corresponding y values
y_vals = quartic_function(x_vals)

# ---- Finding critical points (local minima and maxima) ----
# First derivative: dy/dx = 4ax^3 + 3bx^2 + 2cx + d
first_derivative_coeffs = [4*a, 3*b, 2*c, d]
critical_points = np.roots(first_derivative_coeffs)

# Print critical points (local minima or maxima)
print("\nCritical Points (Local Minima/Maxima):")
for point in critical_points:
    if np.isreal(point):  # Only consider real critical points
        point = point.real
        y_critical = quartic_function(point)
        print(f"x = {point:.2f}, y = {y_critical:.2f}")

# ---- Finding roots ----
# The roots of the quartic equation are where y = 0
roots = np.roots([a, b, c, d, e])
print("\nRoots:")
for root in roots:
    if np.isreal(root):  # Only consider real roots
        print(f"x = {root.real:.2f}, y = 0")

# ---- Plot the quartic function ----
plt.plot(x_vals, y_vals, label=f'y = {a}x^4 + {b}x^3 + {c}x^2 + {d}x + {e}', color='b')

# Mark critical points (local minima/maxima)
for point in critical_points:
    if np.isreal(point):  # Only consider real critical points
        point = point.real
        plt.plot(point, quartic_function(point), 'ro', label=f'Critical Point ({point:.2f}, {quartic_function(point):.2f})', markersize=8)

# Mark the roots
for root in roots:
    if np.isreal(root):  # Only consider real roots
        plt.plot(root.real, 0, 'go', label=f'Root ({root.real:.2f}, 0)', markersize=8)

# Add labels and title
plt.title('Quartic Function Plot')
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
