import numpy as np
import matplotlib.pyplot as plt

# Define the polynomial coefficients (example: f(x) = 2x^3 - 5x^2 + 3x - 4)
coefficients = [2, -5, 3, -4]

# Create a polynomial function using numpy
polynomial = np.poly1d(coefficients)

# Generate x values
x = np.linspace(-10, 10, 400)

# Calculate y values using the polynomial function
y = polynomial(x)

# Plot the polynomial
plt.plot(x, y, label=f'Polynomial: {polynomial}')

# Mark specific points in color
points_x = [-5, 0, 5]  # Example points to highlight
points_y = polynomial(points_x)

# Plot the points with different colors
plt.scatter(points_x, points_y, color=['red', 'green', 'blue'], s=100, zorder=5)

# Annotate the points
for i, (px, py) in enumerate(zip(points_x, points_y)):
    plt.text(px, py, f'({px}, {py:.2f})', fontsize=10, ha='right')

# Add labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of Polynomial Equation')

# Add the polynomial equation as text on the graph
equation_str = "f(x) = " + " + ".join([f"{coef}x^{i}" if i > 0 else f"{coef}" for i, coef in enumerate(coefficients[::-1])])
plt.text(-9, 100, equation_str, fontsize=12, color='purple')

# Add a grid and legend
plt.grid(True)
plt.legend()



# ---- Printing Equation and Points ----

# Print the polynomial equation
print("Polynomial equation:")
print(equation_str)

# Print the specific points and their values
print("\nHighlighted points and their values:")
for px, py in zip(points_x, points_y):
    print(f"Point ({px}, {py:.2f})")

# Show the plot
plt.show()
