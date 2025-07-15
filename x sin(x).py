import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = x * sin(x)
def x_sin_x(x):
    return x * np.sin(x)

# Key x-values to evaluate and highlight
key_x_points = [-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]
print("Function: f(x) = x × sin(x)")
for x in key_x_points:
    y = x_sin_x(x)
    print(f"f({x:.2f}) = {x:.2f} × sin({x:.2f}) = {x:.2f} × {np.sin(x):.2f} = {y:.2f}")

# Generate x values for the graph
x_values = np.linspace(-3*np.pi, 3*np.pi, 1000)
y_values = x_sin_x(x_values)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values, label=r"$f(x) = x \cdot \sin(x)$", color='teal')

# Highlight key points
for x in key_x_points:
    y = x_sin_x(x)
    plt.scatter(x, y, color='red')
    plt.text(x, y, f' ({x:.2f}, {y:.2f})', fontsize=9, color='darkred')

# Formatting
plt.title("Function: $f(x) = x \\cdot \\sin(x)$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.axvline(0, color='black', linestyle='--', linewidth=0.8)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
