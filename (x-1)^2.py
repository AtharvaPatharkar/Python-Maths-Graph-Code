import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = sqrt(x - 1)
def sqrt_shifted(x):
    return np.sqrt(x - 1)

# Key x-values to evaluate and highlight
key_x_points = [1, 2, 5, 10, 17]
print("Function: f(x) = âˆš(x - 1)")
for x in key_x_points:
    y = sqrt_shifted(x)
    print(f"f({x}) = âˆš({x} - 1) = âˆš{x - 1} = {y:.2f}")

# Generate x values starting from 1 to 20
x_values = np.linspace(1, 20, 500)
y_values = sqrt_shifted(x_values)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values, label=r"$f(x) = \sqrt{x - 1}$", color='teal')

# Highlight key points
for x in key_x_points:
    y = sqrt_shifted(x)
    plt.scatter(x, y, color='red')
    plt.text(x, y, f' ({x}, {y:.2f})', fontsize=9, color='darkred')

# Formatting the graph
plt.title("Square Root Shifted Function: $f(x) = \\sqrt{x - 1}$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.legend()

plt.tight_layout()
plt.show()
