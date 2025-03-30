import numpy as np
import matplotlib.pyplot as plt

# Define two vectors
v1 = np.array([1, 2])
v2 = np.array([3, 1])

# Define coefficients for the linear combination
a1 = 2  # Coefficient for v1
a2 = 3  # Coefficient for v2

# Calculate the linear combination
linear_combination = a1 * v1 + a2 * v2

# Print the linear combination equation
print("Linear Combination:")
print(f"L = {a1} * v1 + {a2} * v2")
print(f"L = {a1} * {v1} + {a2} * {v2} = {linear_combination}")

# Prepare the plot
origin = np.array([[0, 0], [0, 0]])  # origin for the vectors
plt.quiver(*origin, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v1')
plt.quiver(*origin, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='red', label='v2')
plt.quiver(*origin, linear_combination[0], linear_combination[1], angles='xy', scale_units='xy', scale=1, color='green', label='L (Linear Combination)')

# Set limits and labels
plt.xlim(-1, 6)
plt.ylim(-1, 6)
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.title('Linear Combination of Vectors')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()
