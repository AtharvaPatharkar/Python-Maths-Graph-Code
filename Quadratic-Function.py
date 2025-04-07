import numpy as np
import matplotlib.pyplot as plt

# Define the coefficients of the quadratic equation: y = ax^2 + bx + c
a = 1
b = -3
c = 2

# Define the quadratic function
def quadratic_function(x):
    return a * x**2 + b * x + c

# Print the quadratic equation
print(f"Quadratic Equation: y = {a}x^2 + {b}x + {c}")

# Generate x values (you can change the range of x as needed)
x_vals = np.linspace(-10, 10, 400)

# Compute corresponding y values
y_vals = quadratic_function(x_vals)

# ---- Print important points ----
# Calculate the vertex
vertex_x = -b / (2 * a)
vertex_y = quadratic_function(vertex_x)
print(f"\nVertex: ({vertex_x:.2f}, {vertex_y:.2f})")

# Calculate the discriminant to find roots
discriminant = b**2 - 4*a*c
if discriminant >= 0:
    root1 = (-b + np.sqrt(discriminant)) / (2*a)
    root2 = (-b - np.sqrt(discriminant)) / (2*a)
    print(f"Root 1: ({root1:.2f}, 0)")
    print(f"Root 2: ({root2:.2f}, 0)")
else:
    print("No real roots")

# ---- Plot the quadratic function ----
plt.plot(x_vals, y_vals, label=f'y = {a}x^2 + {b}x + {c}', color='b')

# Mark the vertex
plt.plot(vertex_x, vertex_y, 'ro', label=f'Vertex ({vertex_x:.2f}, {vertex_y:.2f})', markersize=8)

# Mark the roots if they exist
if discriminant >= 0:
    plt.plot(root1, 0, 'go', label=f'Root 1 ({root1:.2f}, 0)', markersize=8)
    plt.plot(root2, 0, 'go', label=f'Root 2 ({root2:.2f}, 0)', markersize=8)

# Add labels and title
plt.title('Quadratic Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Add a legend
plt.legend()

# Show a grid
plt.grid(True)

# Display the plot
plt.show()
