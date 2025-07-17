import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = sqrt(x + 5)
def sqrt_shifted_left(x):
    return np.sqrt(x + 5)

# Key x-values to evaluate and highlight
key_x_points = [-5, -4, 0, 4, 11]
print("Function: f(x) = âˆš(x + 5)")
for x in key_x_points:
    y = sqrt_shifted_left(x)
    print(f"f({x}) = âˆš({x} + 5) = âˆš{x + 5} = {y:.2f}")

# Generate x values from -5 to 20
x_values = np.linspace(-5, 20, 500)
y_values = sqrt_shifted_left(x_values)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values, label=r"$f(x) = \sqrt{x + 5}$", color='blue')

# Highlight key points
for x in key_x_points:
    y = sqrt_shifted_left(x)
    plt.scatter(x, y, color='red')
    plt.text(x, y, f' ({x}, {y:.2f})', fontsize=9, color='darkred')

# Formatting
plt.title("Square Root Shifted Left Function: $f(x) = \\sqrt{x + 5}$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.legend()

plt.tight_layout()
plt.show()
