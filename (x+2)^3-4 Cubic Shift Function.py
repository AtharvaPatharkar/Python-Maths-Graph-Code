import numpy as np
import matplotlib.pyplot as plt

# Define the cubic shifted function
def cubic_shift(x):
    return (x + 2)**3 - 4

# Define x-values for plotting
x_values = np.linspace(-5, 2, 400)
y_values = cubic_shift(x_values)

# Key points to evaluate and highlight
key_x_points = [-3, -2, -1, 0, 1]
print("Function: f(x) = (x + 2)^3 - 4")
for x in key_x_points:
    y = cubic_shift(x)
    print(f"f({x}) = ({x} + 2)^3 - 4 = ({x + 2})^3 - 4 = {y}")

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label=r"$f(x) = (x + 2)^3 - 4$", color='purple')

# Highlight key points
for x in key_x_points:
    y = cubic_shift(x)
    plt.scatter(x, y, color='red')
    plt.text(x, y, f'({x}, {y:.2f})', fontsize=9, ha='center', color='darkred')

# Formatting
plt.title("Cubic Shift Function: $f(x) = (x + 2)^3 - 4$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.axvline(0, color='black', linestyle='--', linewidth=0.8)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
