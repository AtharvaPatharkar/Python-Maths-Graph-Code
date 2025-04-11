import numpy as np
import matplotlib.pyplot as plt

# Define the rectangular function
def rectangular_function(t, a=1, b=3):
    return 1 if a <= t <= b else 0

# Generate time values for the rectangular function
t_vals = np.linspace(0, 5, 1000)  # From 0 to 5 seconds
y_vals = np.array([rectangular_function(t) for t in t_vals])

# Print the equation for the rectangular function
print("Rectangular Function:")
print("Equation: y(t) = 1 if a ≤ t ≤ b, 0 otherwise (a = 1, b = 3)")

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(t_vals, y_vals, label='Rectangular Function', color='blue')
plt.title('Rectangular Function')
plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.ylim(-0.1, 1.1)  # Limit y-axis to show relevant range
plt.xlim(0, 5)

# Display the plot
plt.legend()
plt.show()
