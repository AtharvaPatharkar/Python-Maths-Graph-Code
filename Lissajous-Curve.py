import numpy as np
import matplotlib.pyplot as plt

# Define the parameter t
t = np.linspace(0, 2 * np.pi, 1000)

# Parameters for the Lissajous curve
A = 5
B = 3
a = 3
b = 2
delta = np.pi / 2  # Phase shift

# Parametric equations for Lissajous curve
x = A * np.sin(a * t + delta)
y = B * np.sin(b * t)

# Plot the parametric curve (Lissajous)
plt.plot(x, y, label=f'Lissajous: A*sin({a}t + δ), B*sin({b}t)')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parametric Equation: Lissajous Curve')

# Add a grid and legend
plt.grid(True)
plt.legend()



# ---- Print Equation and Parametric Points ----
print("Parametric equations for the Lissajous curve:")
print(f"x(t) = {A} * sin({a}t + {delta})")
print(f"y(t) = {B} * sin({b}t)")

# Print some specific points for t
print("\nSome specific points (t, x, y):")
for i in range(0, len(t), 250):  # Picking 4 points along the Lissajous curve
    print(f"t = {t[i]:.2f}, x = {x[i]:.2f}, y = {y[i]:.2f}")

# Show the plot
plt.axis('equal')  # Keep the aspect ratio of the plot equal
plt.show()
