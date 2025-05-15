import numpy as np
import matplotlib.pyplot as plt

# Function to display the function values at all points
def display_values(x, y):
    print("x-values and corresponding y-values (y = 2^x):")
    for i in range(len(x)):
        print(f"x = {x[i]:.2f}, y = {y[i]:.2f}")

# Create the plot
def create_plot():
    # Define the range for x-axis and create x values
    x_min = -2
    x_max = 2
    x_step = 0.1
    x = np.arange(x_min, x_max, x_step)

    # Calculate the corresponding y values for the base-2 exponential function
    y = 2 ** x

    # Display the values of x and y
    display_values(x, y)

    # Create the plot
    plt.plot(x, y, label=r'$y = 2^x$', color='blue')

    # Plot every point as a marker
    plt.scatter(x, y, color='red', marker='o')

    # Label the axes
    plt.xlabel('x')
    plt.ylabel('y')

    # Add a title to the graph
    plt.title('Base 2 Exponential Function')

    # Display a grid
    plt.grid(True)

    # Add a legend
    plt.legend()

    # Set the limits for the graph (you can adjust these values as needed)
    plt.xlim(x_min, x_max)  # Set the x-axis range
    plt.ylim(0, 10)  # Set the y-axis range (for better view)

    # Show the plot
    plt.show()

# Call the function to create and display the plot
create_plot()
