import numpy as np
import matplotlib.pyplot as plt

# Function to simulate Dirac Delta using a Gaussian function
def dirac_delta_approx(x, sigma=0.1):
    return np.exp(-x**2 / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))

# Create the plot
def create_dirac_delta_plot():
    # Define x values
    x_min = -1
    x_max = 1
    x_step = 0.01
    x = np.arange(x_min, x_max + x_step, x_step)

    # Define sigma for Gaussian approximation
    sigma = 0.05  # Small sigma for sharp peak

    # Calculate the Gaussian approximation
    y = dirac_delta_approx(x, sigma)

    # Create the plot
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=r'$\delta(x)$ Approximation', color='blue')

    # Add title and labels
    plt.title('Approximation of the Dirac Delta Function')
    plt.xlabel('x')
    plt.ylabel('y')

    # Set y-limit to simulate the spike at x=0
    plt.ylim(0, 10)

    # Add grid and legend
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.show()

# Call the function to create and display the plot
create_dirac_delta_plot()
