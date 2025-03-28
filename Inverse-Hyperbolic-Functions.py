import numpy as np
import matplotlib.pyplot as plt

# Define inverse hyperbolic functions
def inverse_hyperbolic_sine(x):
    return np.arcsinh(x)

def inverse_hyperbolic_cosine(x):
    return np.arccosh(x)

# Print the equations
print("Inverse Hyperbolic Functions:")
print("Inverse Hyperbolic Sine Equation: y = sinh^(-1)(x)")
print("Inverse Hyperbolic Cosine Equation: y = cosh^(-1)(x)")

# Generate x values for inverse hyperbolic sine
x_sinh_vals = np.linspace(-3, 3, 500)
y_sinh_vals = inverse_hyperbolic_sine(x_sinh_vals)

# Generate x values for inverse hyperbolic cosine (x must be >= 1)
x_cosh_vals = np.linspace(1, 5, 500)
y_cosh_vals = inverse_hyperbolic_cosine(x_cosh_vals)

# ---- Key points for inverse hyperbolic sine function ----
sinh_key_points = [-2, -1, 0, 1, 2]
print("\nInverse Hyperbolic Sine Key Points (x, y):")
for point in sinh_key_points:
    y_val = inverse_hyperbolic_sine(point)
    print(f"x = {point:.2f}, y = {y_val:.2f}")

# ---- Key points for inverse hyperbolic cosine function ----
cosh_key_points = [1, 2, 3, 4, 5]
print("\nInverse Hyperbolic Cosine Key Points (x, y):")
for point in cosh_key_points:
    y_val = inverse_hyperbolic_cosine(point)
    print(f"x = {point:.2f}, y = {y_val:.2f}")

# ---- Plotting the inverse hyperbolic functions ----
plt.figure(figsize=(10, 5))

# Plot inverse hyperbolic sine function
plt.subplot(1, 2, 1)
plt.plot(x_sinh_vals, y_sinh_vals, label='y = sinh^(-1)(x)', color='b')
for point in sinh_key_points:
    plt.plot(point, inverse_hyperbolic_sine(point), 'ro', label=f'({point:.2f}, {inverse_hyperbolic_sine(point):.2f})', markersize=8)
plt.title('Inverse Hyperbolic Sine Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Plot inverse hyperbolic cosine function
plt.subplot(1, 2, 2)
plt.plot(x_cosh_vals, y_cosh_vals, label='y = cosh^(-1)(x)', color='g')
for point in cosh_key_points:
    plt.plot(point, inverse_hyperbolic_cosine(point), 'ro', label=f'({point:.2f}, {inverse_hyperbolic_cosine(point):.2f})', markersize=8)
plt.title('Inverse Hyperbolic Cosine Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Display the plots
plt.tight_layout()
plt.show()
