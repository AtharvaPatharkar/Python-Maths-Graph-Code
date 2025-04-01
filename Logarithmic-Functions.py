import numpy as np
import matplotlib.pyplot as plt

# Define logarithmic functions
def natural_logarithm(x):
    return np.log(x)

def common_logarithm(x):
    return np.log10(x)

def binary_logarithm(x):
    return np.log2(x)

# Print the equations
print("Logarithmic Functions:")
print("Natural Logarithm Equation: y = ln(x)")
print("Common Logarithm Equation: y = log10(x)")
print("Binary Logarithm Equation: y = log2(x)")

# Generate x values for logarithms (domain: (0, ∞))
x_vals = np.linspace(0.01, 10, 500)  # Starting just above 0
y_natural_vals = natural_logarithm(x_vals)
y_common_vals = common_logarithm(x_vals)
y_binary_vals = binary_logarithm(x_vals)

# ---- Key points for natural logarithm function ----
natural_key_points = [0.1, 1, 2.718, 10]
print("\nNatural Logarithm Key Points (x, y):")
for point in natural_key_points:
    y_val = natural_logarithm(point)
    print(f"x = {point:.2f}, y = {y_val:.2f}")

# ---- Key points for common logarithm function ----
common_key_points = [0.1, 1, 10]
print("\nCommon Logarithm Key Points (x, y):")
for point in common_key_points:
    y_val = common_logarithm(point)
    print(f"x = {point:.2f}, y = {y_val:.2f}")

# ---- Key points for binary logarithm function ----
binary_key_points = [0.1, 1, 2, 4, 8]
print("\nBinary Logarithm Key Points (x, y):")
for point in binary_key_points:
    y_val = binary_logarithm(point)
    print(f"x = {point:.2f}, y = {y_val:.2f}")

# ---- Plotting the logarithmic functions ----
plt.figure(figsize=(15, 5))

# Plot natural logarithm function
plt.subplot(1, 3, 1)
plt.plot(x_vals, y_natural_vals, label='y = ln(x)', color='b')
for point in natural_key_points:
    plt.plot(point, natural_logarithm(point), 'ro', markersize=8)
plt.title('Natural Logarithm Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Plot common logarithm function
plt.subplot(1, 3, 2)
plt.plot(x_vals, y_common_vals, label='y = log10(x)', color='g')
for point in common_key_points:
    plt.plot(point, common_logarithm(point), 'ro', markersize=8)
plt.title('Common Logarithm Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Plot binary logarithm function
plt.subplot(1, 3, 3)
plt.plot(x_vals, y_binary_vals, label='y = log2(x)', color='orange')
for point in binary_key_points:
    plt.plot(point, binary_logarithm(point), 'ro', markersize=8)
plt.title('Binary Logarithm Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Display the plots
plt.tight_layout()
plt.show()
