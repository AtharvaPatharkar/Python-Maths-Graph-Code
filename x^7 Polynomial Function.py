import numpy as np
import matplotlib.pyplot as plt

# Define the polynomial function
def polynomial(x):
    return x**7

# Define x-values for plotting
x_values = np.linspace(-2, 2, 400)
y_values = polynomial(x_values)

# Key points to evaluate and highlight
key_x_points = [-2, -1, 0, 1, 2]
print("Function: f(x) = x^7")
for x in key_x_points:
    y = polynomial(x)
    print(f"f({x}) = {x}^7 = {y}")

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label=r"$f(x) = x^7$", color='green')

# Highlight key points
for x in key_x_points:
    y = polynomial(x)
    plt.scatter(x, y, color='red')
    plt.text(x, y + 0.5, f'({x}, {y:.2f})', fontsize=9, ha='center', color='darkred')

# Formatting
plt.title("Polynomial Function: $f(x) = x^7$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.axvline(0, color='black', linestyle='--', linewidth=0.8)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
