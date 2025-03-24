import numpy as np
import matplotlib.pyplot as plt

# Define the Heaviside step function
def heaviside_step_function(x):
    return np.where(x < 0, 0, 1)

# Generate x values for the Heaviside function
x_vals = np.linspace(-5, 5, 1000)  # From -5 to 5
y_vals = heaviside_step_function(x_vals)

# Print the equation for the import numpy as np
import matplotlib.pyplot as plt

# Define the Heaviside step function
def heaviside_step_function(x):
    return np.where(x < 0, 0, 1)

# Generate x values for the Heaviside function
x_vals = np.linspace(-5, 5, 1000)  # From -5 to 5
y_vals = heaviside_step_function(x_vals)

# Print the equation for the Heaviside step function
print("Heaviside Step Function:")
print("H(x) = 0 if x < 0, H(x) = 1 if x ≥ 0")

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x_vals, y_vals, label='H(x)', color='blue')
plt.title('Heaviside Step Function')
plt.xlabel('x')
plt.ylabel('H(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.ylim(-0.1, 1.1)  # Limit y-axis to show relevant range
plt.xlim(-5, 5)

# Display the plot
plt.legend()
plt.show()
print("Heaviside Step Function:")
print("H(x) = 0 if x < 0, H(x) = 1 if x ≥ 0")

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x_vals, y_vals, label='H(x)', color='blue')
plt.title('Heaviside Step Function')
plt.xlabel('x')
plt.ylabel('H(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.ylim(-0.1, 1.1)  # Limit y-axis to show relevant range
plt.xlim(-5, 5)

# Display the plot
plt.legend()
plt.show()
