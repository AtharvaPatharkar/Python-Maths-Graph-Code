import numpy as np
import matplotlib.pyplot as plt

# Define inverse circular functions
def inverse_sine(x):
    return np.arcsin(x)

def inverse_cosine(x):
    return np.arccos(x)

# Print the equations
print("Inverse Circular Functions:")
print("Inverse Sine Equation: y = sin^(-1)(x)")
print("Inverse Cosine Equation: y = cos^(-1)(x)")

# Generate x values for inverse sine (domain: [-1, 1])
x_sin_vals = np.linspace(-1, 1, 500)
y_sin_vals = inverse_sine(x_sin_vals)

# Generate x values for inverse cosine (domain: [-1, 1])
x_cos_vals = np.linspace(-1, 1, 500)
y_cos_vals = inverse_cosine(x_cos_vals)

# ---- Key points for inverse sine function ----
sin_key_points = [-1, 0, 1]
print("\nInverse Sine Key Points (x, y):")
for point in sin_key_points:
    y_val = inverse_sine(point)
    print(f"x = {point:.2f}, y = {y_val:.2f}")

# ---- Key points for inverse cosine function ----
cos_key_points = [-1, 0, 1]
print("\nInverse Cosine Key Points (x, y):")
for point in cos_key_points:
    y_val = inverse_cosine(point)
    print(f"x = {point:.2f}, y = {y_val:.2f}")

# ---- Plotting the inverse circular functions ----
plt.figure(figsize=(10, 5))

# Plot inverse sine function
plt.subplot(1, 2, 1)
plt.plot(x_sin_vals, y_sin_vals, label='y = sin^(-1)(x)', color='b')
for point in sin_key_points:
    plt.plot(point, inverse_sine(point), 'ro', label=f'({point:.2f}, {inverse_sine(point):.2f})', markersize=8)
plt.title('Inverse Sine Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Plot inverse cosine function
plt.subplot(1, 2, 2)
plt.plot(x_cos_vals, y_cos_vals, label='y = cos^(-1)(x)', color='g')
for point in cos_key_points:
    plt.plot(point, inverse_cosine(point), 'ro', label=f'({point:.2f}, {inverse_cosine(point):.2f})', markersize=8)
plt.title('Inverse Cosine Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Display the plots
plt.tight_layout()
plt.show()
