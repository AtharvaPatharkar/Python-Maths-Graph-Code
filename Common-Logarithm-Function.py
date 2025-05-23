import numpy as np
import matplotlib.pyplot as plt

# Function to display x and y values
def display_values(x, y):
    print("x-values and corresponding y-values (y = log10(x)):")
    for i in range(len(x)):
        print(f"x = {x[i]:.2f}, y = {y[i]:.2f}")

# Create the plot
def create_common_log_plot():
    # Define x values, positive only (cannot log(0) or negative numbers!)
    x_min = 0.1
    x_max = 10
    x_step = 0.1
    x = np.arange(x_min, x_max, x_step)

    # Calculate y = log10(x)
    y = np.log10(x)

    # Display the x and y values
    display_values(x, y)

    # Create the plot
    plt.plot(x, y, label=r'$y = \log_{10}(x)$', color='orange')

    # Plot every point as a marker
    plt.scatter(x, y, color='red', s=10)

    # Label the axes
    plt.xlabel('x')
    plt.ylabel('y')

    # Add a title
    plt.title('Common Logarithm Function')

    # Add a grid
    plt.grid(True)
    plt.legend()

    # Set limits
    plt.xlim(x_min, x_max)
    plt.ylim(-1, 1.5)

    # Show the plot
    plt.show()

# Call the function to create and display the plot
create_common_log_plot()
