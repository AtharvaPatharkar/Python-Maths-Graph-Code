import numpy as np
import matplotlib.pyplot as plt

# Define parameters for the square wave
A = 1      # Amplitude
T = 2      # Period
t = np.linspace(0, 10, 1000)  # Time vector

# Create the square wave using numpy's sign function
square_wave = A * np.sign(np.sin(2 * np.pi * (t / T)))

# Print the equation for the square wave
print("Square Wave Function:")
print(f"f(t) = A * sign(sin(2πt/T)) where A = {A} and T = {T}")

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(t, square_wave, label='Square Wave', color='blue')
plt.title('Square Wave')
plt.xlabel('Time (t)')
plt.ylabel('f(t)')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.ylim(-1.5, 1.5)  # Limit y-axis to show relevant range
plt.xlim(0, 10)

# Display the plot
plt.legend()
plt.show()
