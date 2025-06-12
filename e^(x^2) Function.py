import numpy as np
import matplotlib.pyplot as plt

# Function to plot y = e^(x^2)
def create_exponential_square_plot():
    # Define x values
    x_min = -2
    x_max = 2
    x_step = 0.01
    x = np.arange(x_min, x_max + x_step, x_step)

    # Calculate y = e^(x^2)
    y = np.exp(x**2)

    # Create the plot
    plt.figure(figsize=(8,6))
    plt.plot(x, y, label=r'$y = e^{x^2}$', color='red')

    # Add title and labels
    plt.title('Exponential Function: y = e^{x^2}')
    plt.xlabel('x')
    plt.ylabel('y')

    # Add grid and legend
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.show()

# Call the function to create and display the plot
create_exponential_square_plot()
