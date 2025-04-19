import numpy as np
import matplotlib.pyplot as plt

# Define the triangle wave function
def triangle_wave(t, A=1, T=2):
    return (2 * A / T) * (t % T) if (t % T) < T / 2 else (2 * A * (1 - (t % T) / T))

# Generate time values for the triangle wave
t_vals = np.linspace(0, 10, 1000)  # From 0 to 10 seconds
y_vals = np.array([triangle_wave(t) for t in t_vals])

# Print the equation for the triangle wave
print("Triangle Wave Function:")
print("Equation: y(t) = { (4A/T) * t, 0 ≤ t < T/2; (-4A/T) * t + 4A, T/2 ≤ t < T }")

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(t_vals, y_vals, label='Triangle Wave', color='orange')
plt.title('Triangle Wave Function')
plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.ylim(-1.5, 1.5)  # Limit y-axis to show relevant range
plt.xlim(0, 10)

# Display the plot
plt.legend()
plt.show()
