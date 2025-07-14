import numpy as np
import matplotlib.pyplot as plt

# Define the function
def shifted_parabola(x):
    return (x - 1)**2 + 3

# Define x-values for plotting
x_values = np.linspace(-2, 4, 400)
y_values = shifted_parabola(x_values)

# Key points to evaluate
key_x_points = [0, 1, 2, 3]
print("Function: f(x) = (x - 1)^2 + 3")
for x in key_x_points:
    y = shifted_parabola(x)
    print(f"f({x}) = ({x} - 1)^2 + 3 = ({x - 1})^2 + 3 = {y}")

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, label=r"$f(x) = (x - 1)^2 + 3$", color='blue')

# Highlight vertex and other points
for x in key_x_points:
    y = shifted_parabola(x)
    plt.scatter(x, y, color='red')
    plt.text(x, y + 0.2, f'({x}, {y})', fontsize=9, ha='center', color='darkred')

# Formatting
plt.title("Quadratic Function: $f(x) = (x - 1)^2 + 3$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.axvline(0, color='black', linestyle='--', linewidth=0.8)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
