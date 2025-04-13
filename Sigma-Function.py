import numpy as np
import matplotlib.pyplot as plt

# Define the sigma function
def sigma_function(n):
    return sum(d for d in range(1, n + 1) if n % d == 0)

# Generate a range of values for n
n_values = np.arange(1, 21)  # From 1 to 20
sigma_values = [sigma_function(n) for n in n_values]

# Print the sigma values
print("Sigma Function Values:")
for n, sigma in zip(n_values, sigma_values):
    print(f"σ({n}) = {sigma}")

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(n_values, sigma_values, marker='o', label='σ(n)', color='blue')
plt.title('Sigma Function: σ(n)')
plt.xlabel('n')
plt.ylabel('σ(n)')
plt.xticks(n_values)
plt.grid(True)

# Display the plot
plt.legend()
plt.show()
