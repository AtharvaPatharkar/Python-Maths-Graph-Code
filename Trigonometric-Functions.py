import numpy as np
import matplotlib.pyplot as plt

# Define trigonometric functions
def sine_function(x):
    return np.sin(x)

def cosine_function(x):
    return np.cos(x)

# Print the equations
print("Trigonometric Functions:")
print("Sine Equation: y = sin(x)")
print("Cosine Equation: y = cos(x)")

# Generate x values
x_vals = np.linspace(0, 2 * np.pi, 500)
y_sin_vals = sine_function(x_vals)
y_cos_vals = cosine_function(x_vals)

# ---- Key points for sine function ----
sine_key_points = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
print("\nSine Key Points (x, y):")
for point in sine_key_points:
    y_val = sine_function(point)
    print(f"x = {point:.2f}, y = {y_val:.2f}")

# ---- Key points for cosine function ----
cosine_key_points = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
print("\nCosine Key Points (x, y):")
for point in cosine_key_points:
    y_val = cosine_function(point)
    print(f"x = {point:.2f}, y = {y_val:.2f}")

# ---- Plotting the trigonometric functions ----
plt.figure(figsize=(10, 5))

# Plot sine function
plt.subplot(1, 2, 1)
plt.plot(x_vals, y_sin_vals, label='y = sin(x)', color='b')
for point in sine_key_points:
    plt.plot(point, sine_function(point), 'ro', label=f'({point:.2f}, {sine_function(point):.2f})', markersize=8)
plt.title('Sine Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xticks(np.arange(0, 2 * np.pi + 0.5, np.pi/2), 
           ['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])
plt.grid(True)
plt.legend()

# Plot cosine function
plt.subplot(1, 2, 2)
plt.plot(x_vals, y_cos_vals, label='y = cos(x)', color='g')
for point in cosine_key_points:
    plt.plot(point, cosine_function(point), 'ro', label=f'({point:.2f}, {cosine_function(point):.2f})', markersize=8)
plt.title('Cosine Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xticks(np.arange(0, 2 * np.pi + 0.5, np.pi/2), 
           ['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])
plt.grid(True)
plt.legend()

# Display the plots
plt.tight_layout()
plt.show()
