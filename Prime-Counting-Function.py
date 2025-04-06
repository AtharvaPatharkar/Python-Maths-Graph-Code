import numpy as np
import matplotlib.pyplot as plt
from sympy import primepi  # Using sympy for the prime-counting function

# Generate a range of values for n
n_values = np.arange(1, 101)  # From 1 to 100
pi_values = [primepi(n) for n in n_values]

# Print the prime-counting function values
print("Prime-Counting Function Values:")
for n, pi in zip(n_values, pi_values):
    print(f"π({n}) = {pi}")

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(n_values, pi_values, marker='o', label='π(n)', color='blue')
plt.title('Prime-Counting Function: π(n)')
plt.xlabel('n')
plt.ylabel('π(n)')
plt.xticks(n_values)
plt.grid(True)

# Display the plot
plt.legend()
plt.show()
