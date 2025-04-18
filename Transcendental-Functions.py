import numpy as np
import matplotlib.pyplot as plt

# Define the exponential and logarithmic functions
def exponential_function(x):
    return np.exp(x)

def logarithmic_function(x):
    return np.log(x)

# Print the equations
print("Transcendental Functions:")
print("Exponential Equation: y = e^x")
print("Logarithmic Equation: y = ln(x)")

# Generate x values for the exponential function
x_exp_vals = np.linspace(-2, 2, 500)
y_exp_vals = exponential_function(x_exp_vals)

# Generate x values for the logarithmic function (only positive x values)
x_log_vals = np.linspace(0.01, 10, 500)
y_log_vals = logarithmic_function(x_log_vals)

# ---- Key points for exponential function ----
exp_key_points = [-2, 0, 1, 2]
print("\nExponential Function Key Points (x, y):")
for point in exp_key_points:
    y_val = exponential_function(point)
    print(f"x = {point}, y = {y_val:.2f}")

# ---- Key points for logarithmic function ----
log_key_points = [1, np.e, 10]
print("\nLogarithmic Function Key Points (x, y):")
for point in log_key_points:
    y_val = logarithmic_function(point)
    print(f"x = {point}, y = {y_val:.2f}")

# ---- Plotting the exponential function ----
plt.figure(figsize=(10, 5))

# Plot exponential function
plt.subplot(1, 2, 1)
plt.plot(x_exp_vals, y_exp_vals, label='y = e^x', color='b')
for point in exp_key_points:
    plt.plot(point, exponential_function(point), 'ro', label=f'({point}, {exponential_function(point):.2f})', markersize=8)
plt.title('Exponential Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Plot logarithmic function
plt.subplot(1, 2, 2)
plt.plot(x_log_vals, y_log_vals, label='y = ln(x)', color='g')
for point in log_key_points:
    plt.plot(point, logarithmic_function(point), 'ro', label=f'({point}, {logarithmic_function(point):.2f})', markersize=8)
plt.title('Logarithmic Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Display the plots
plt.tight_layout()
plt.show()
