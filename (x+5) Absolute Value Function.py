import numpy as np
import matplotlib.pyplot as plt

# Define the absolute value function
def absolute_value(x):
    return np.abs(x + 5)

# Define x-values for plotting
x_values = np.linspace(-10, 0, 400)
y_values = absolute_value(x_values)

# Key points to evaluate and highlight
key_x_points = [-5, -8, -3, 0]
print("Function: f(x) = |x + 5|")
for x in key_x_points:
    y = absolute_value(x)
    print(f"f({x}) = |{x} + 5| = |{x + 5}| = {y}")

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label=r"$f(x) = |x + 5|$", color='green')

# Highlight key points
for x in key_x_points:
    y = absolute_value(x)
    plt.scatter(x, y, color='red')
    plt.text(x, y + 0.2, f'({x}, {y})', fontsize=9, ha='center', color='darkred')

# Formatting
plt.title("Absolute Value Function: $f(x) = |x + 5|$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.axvline(0, color='black', linestyle='--', linewidth=0.8)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
