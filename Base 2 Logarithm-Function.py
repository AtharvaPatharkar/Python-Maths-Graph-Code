import numpy as np
import matplotlib.pyplot as plt

# Function to display the function values at all points
def display_values(x, y):
    print("x-values and corresponding y-values (y = log2(x)):")
    for i in range(len(x)):
        print(f"x = {x[i]:.2f}, y = {y[i]:.2f}")

# Create the plot
def create_plot():
    # Define the range for x-axis (only positive numbers for log)
    x_min = 0.1  # can't be zero or negative!
    x_max = 10
    x_step = 0.1
    x = np.arange(x_min, x_max, x_step)

    # Calculate the corresponding y values for the base-2 logarithm function
    y = np.log2(x)

    # Display the values of x and y
    display_values(x, y)

    # Create the plot
    plt.plot(x, y, label=r'$y = \log_2(x)$', color='green')

    # Plot every point as a marker
    plt.scatter(x, y, color='red', marker='o')

    # Label the axes
    plt.xlabel('x')
    plt.ylabel('y')

    # Add a title to the graph
    plt.title('Base 2 Logarithm Function')

    # Display a grid
    plt.grid(True)

    # Add a legend
    plt.legend()

    # Set the limits for the graph
    plt.xlim(x_min, x_max)
    plt.ylim(-4, 4)  # Adjusted for better view

    # Show the plot
    plt.show()

# Call the function to create and display the plot
create_plot()
