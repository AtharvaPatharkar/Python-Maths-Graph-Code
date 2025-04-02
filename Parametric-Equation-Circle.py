import numpy as np
import matplotlib.pyplot as plt

# Define the parameter t
t = np.linspace(0, 2 * np.pi, 400)

# Radius of the circle
r = 5

# Parametric equations for x and y (circle)
x = r * np.cos(t)
y = r * np.sin(t)

# Plot the parametric curve (circle)
plt.plot(x, y, label='Circle: x = r*cos(t), y = r*sin(t)')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parametric Equation: Circle')

# Add a grid and legend
plt.grid(True)
plt.legend()



# ---- Print Equation and Parametric Points ----
print("Parametric equations for the circle:")
print(f"x(t) = {r} * cos(t)")
print(f"y(t) = {r} * sin(t)")

# Print some specific points for t
print("\nSome specific points (t, x, y):")
for i in range(0, len(t), 100):  # Picking 4 points along the circle
    print(f"t = {t[i]:.2f}, x = {x[i]:.2f}, y = {y[i]:.2f}")

# Show the plot
plt.axis('equal')  # Keep the aspect ratio of the plot equal
plt.show()
