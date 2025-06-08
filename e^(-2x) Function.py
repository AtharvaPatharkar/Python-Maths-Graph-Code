import numpy as np
import matplotlib.pyplot as plt

# Function to plot y = e^(-2x)
def create_exponential_decay_plot():
    # Define x values
    x_min = -2
    x_max = 2
    x_step = 0.01
    x = np.arange(x_min, x_max + x_step, x_step)

    # Calculate y = e^(-2x)
    y = np.exp(-2 * x)

    # Create the plot
    plt.figure(figsize=(8,6))
    plt.plot(x, y, label=r'$y = e^{-2x}$', color='blue')

    # Add title and labels
    plt.title('Exponential Decay Function: y = e^{-2x}')
    plt.xlabel('x')
    plt.ylabel('y')

    # Add grid and legend
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.show()

# Call the function to create and display the plot
create_exponential_decay_plot()
