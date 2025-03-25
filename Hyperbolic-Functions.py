import numpy as np
import matplotlib.pyplot as plt

# Define hyperbolic functions
def hyperbolic_sine(x):
    return np.sinh(x)

def hyperbolic_cosine(x):
    return np.cosh(x)

# Print the equations
print("Hyperbolic Functions:")
print("Hyperbolic Sine Equation: y = sinh(x)")
print("Hyperbolic Cosine Equation: y = cosh(x)")

# Generate x values
x_vals = np.linspace(-2, 2, 500)
y_sinh_vals = hyperbolic_sine(x_vals)
y_cosh_vals = hyperbolic_cosine(x_vals)

# ---- Key points for hyperbolic sine function ----
sinh_key_points = [-2, -1, 0, 1, 2]
print("\nHyperbolic Sine Key Points (x, y):")
for point in sinh_key_points:
    y_val = hyperbolic_sine(point)
    print(f"x = {point}, y = {y_val:.2f}")

# ---- Key points for hyperbolic cosine function ----
cosh_key_points = [-2, -1, 0, 1, 2]
print("\nHyperbolic Cosine Key Points (x, y):")
for point in cosh_key_points:
    y_val = hyperbolic_cosine(point)
    print(f"x = {point}, y = {y_val:.2f}")

# ---- Plotting the hyperbolic functions ----
plt.figure(figsize=(10, 5))

# Plot hyperbolic sine function
plt.subplot(1, 2, 1)
plt.plot(x_vals, y_sinh_vals, label='y = sinh(x)', color='b')
for point in sinh_key_points:
    plt.plot(point, hyperbolic_sine(point), 'ro', label=f'({point}, {hyperbolic_sine(point):.2f})', markersize=8)
plt.title('Hyperbolic Sine Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Plot hyperbolic cosine function
plt.subplot(1, 2, 2)
plt.plot(x_vals, y_cosh_vals, label='y = cosh(x)', color='g')
for point in cosh_key_points:
    plt.plot(point, hyperbolic_cosine(point), 'ro', label=f'({point}, {hyperbolic_cosine(point):.2f})', markersize=8)
plt.title('Hyperbolic Cosine Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Display the plots
plt.tight_layout()
plt.show()
