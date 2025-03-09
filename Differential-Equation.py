import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the differential equation dy/dx = f(x, y)
def differential_eq(x, y):
    return y - x**2 + 1  # dy/dx = y - x^2 + 1

# Print the differential equation
print("Differential Equation: dy/dx = y - x^2 + 1")

# Define the range of x (the independent variable) and the initial condition for y
x_span = (0, 5)  # Solving from x=0 to x=5
y0 = [0.5]  # Initial condition: y(0) = 0.5

# Solve the differential equation using solve_ivp
solution = solve_ivp(differential_eq, x_span, y0, t_eval=np.linspace(0, 5, 100))

# Extract x and y values from the solution
x_vals = solution.t
y_vals = solution.y[0]

# ---- Print the solution values ----
print("\nSolution of the differential equation:")
for i in range(0, len(x_vals), 10):  # Print points at regular intervals
    print(f"x = {x_vals[i]:.2f}, y = {y_vals[i]:.4f}")

# Plot the solution
plt.plot(x_vals, y_vals, label='Solution to dy/dx = y - x^2 + 1')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of Differential Equation')

# Add a grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
