import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the system of differential equations
def harmonic_oscillator(x, y):
    y1, y2 = y
    dydx = [y2, -y1]  # dy1/dx = y2, dy2/dx = -y1
    return dydx

# Print the system of differential equations
print("System of Differential Equations:")
print("dy1/dx = y2")
print("dy2/dx = -y1")

# Initial conditions: y1(0) = 1, y2(0) = 0
y0 = [1, 0]

# Solve the system over the range x = [0, 10]
x_span = (0, 10)
solution = solve_ivp(harmonic_oscillator, x_span, y0, t_eval=np.linspace(0, 10, 100))

# Extract x values and the solutions for y1 and y2
x_vals = solution.t
y1_vals = solution.y[0]
y2_vals = solution.y[1]

# ---- Print the solution values ----
print("\nSolution of the system of differential equations:")
for i in range(0, len(x_vals), 10):
    print(f"x = {x_vals[i]:.2f}, y1 (displacement) = {y1_vals[i]:.4f}, y2 (velocity) = {y2_vals[i]:.4f}")

# Plot the solutions
plt.plot(x_vals, y1_vals, label='y1 (displacement)')
plt.plot(x_vals, y2_vals, label='y2 (velocity)', linestyle='--')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of Harmonic Oscillator')

# Add a grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
