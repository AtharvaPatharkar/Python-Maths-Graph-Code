import numpy as np
import matplotlib.pyplot as plt

# Define the indicator function for the set A = [0, 1]
def indicator_function(x):
    return 1 if 0 <= x <= 1 else 0

# Create an array of x values
x_vals = np.linspace(-0.5, 1.5, 500)
y_vals = np.array([indicator_function(x) for x in x_vals])

# Print the equation for the indicator function
print("Indicator Function:")
print("Equation: I_A(x) = 1 if x ∈ A, 0 otherwise (A = [0, 1])")

# Create the plot
plt.figure(figsize=(10, 5))
plt.step(x_vals, y_vals, label='I_A(x)', color='blue', where='post')
plt.title('Indicator Function for the Set A = [0, 1]')
plt.xlabel('x')
plt.ylabel('I_A(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.ylim(-0.1, 1.1)
plt.xlim(-0.5, 1.5)

# Display the plot
plt.legend()
plt.show()
