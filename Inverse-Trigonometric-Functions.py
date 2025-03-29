import numpy as np
import matplotlib.pyplot as plt

# Define the inverse trigonometric functions
def arcsin_function(x):
    return np.arcsin(x)

def arccos_function(x):
    return np.arccos(x)

def arctan_function(x):
    return np.arctan(x)

# Generate x values for the functions
x_arcsin = np.linspace(-1, 1, 400)  # Domain for arcsin
x_arccos = np.linspace(-1, 1, 400)  # Domain for arccos
x_arctan = np.linspace(-10, 10, 400)  # Domain for arctan

# Create the plots
plt.figure(figsize=(15, 10))

# Arcsine
plt.subplot(3, 1, 1)
plt.plot(x_arcsin, arcsin_function(x_arcsin), label='y = arcsin(x)', color='blue')
plt.title('Arcsine Function: y = arcsin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.xlim(-1.1, 1.1)

# Arccosine
plt.subplot(3, 1, 2)
plt.plot(x_arccos, arccos_function(x_arccos), label='y = arccos(x)', color='green')
plt.title('Arccosine Function: y = arccos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.ylim(-1.5, 2)
plt.xlim(-1.1, 1.1)

# Arctangent
plt.subplot(3, 1, 3)
plt.plot(x_arctan, arctan_function(x_arctan), label='y = arctan(x)', color='red')
plt.title('Arctangent Function: y = arctan(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.xlim(-10, 10)

# Display the plots
plt.tight_layout()
plt.show()

# Print the equations
print("Inverse Trigonometric Functions:")
print("1. y = arcsin(x) for x in [-1, 1]")
print("2. y = arccos(x) for x in [-1, 1]")
print("3. y = arctan(x) for all x")
