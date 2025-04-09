import numpy as np
import matplotlib.pyplot as plt

# Define the coefficients of the quintic equation: y = ax^5 + bx^4 + cx^3 + dx^2 + ex + f
a = 1
b = -10
c = 35
d = -50
e = 24
f = 0

# Define the quintic function
def quintic_function(x):
    return a * x**5 + b * x**4 + c * x**3 + d * x**2 + e * x + f

# Print the quintic equation
print(f"Quintic Equation: y = {a}x^5 + {b}x^4 + {c}x^3 + {d}x^2 + {e}x + {f}")

# Generate x values (you can change the range of x as needed)
x_vals = np.linspace(-5, 5, 500)

# Compute corresponding y values
y_vals = quintic_function(x_vals)

# ---- Finding critical points (local minima and maxima) ----
# First derivative: dy/dx = 5ax^4 + 4bx^3 + 3cx^2 + 2dx + e
first_derivative_coeffs = [5*a, 4*b, 3*c, 2*d, e]
critical_points = np.roots(first_derivative_coeffs)

# Print critical points (local minima or maxima)
print("\nCritical Points (Local Minima/Maxima):")
for point in critical_points:
    if np.isreal(point):  # Only consider real critical points
        point = point.real
        y_critical = quintic_function(point)
        print(f"x = {point:.2f}, y = {y_critical:.2f}")

# ---- Finding roots ----
# The roots of the quintic equation are where y = 0
roots = np.roots([a, b, c, d, e, f])
print("\nRoots:")
for root in roots:
    if np.isreal(root):  # Only consider real roots
        print(f"x = {root.real:.2f}, y = 0")

# ---- Plot the quintic function ----
plt.plot(x_vals, y_vals, label=f'y = {a}x^5 + {b}x^4 + {c}x^3 + {d}x^2 + {e}x + {f}', color='b')

# Mark critical points (local minima/maxima)
for point in critical_points:
    if np.isreal(point):  # Only consider real critical points
        point = point.real
        plt.plot(point, quintic_function(point), 'ro', label=f'Critical Point ({point:.2f}, {quintic_function(point):.2f})', markersize=8)

# Mark the roots
for root in roots:
    if np.isreal(root):  # Only consider real roots
        plt.plot(root.real, 0, 'go', label=f'Root ({root.real:.2f}, 0)', markersize=8)

# Add labels and title
plt.title('Quintic Function Plot')
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
