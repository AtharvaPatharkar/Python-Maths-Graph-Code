import numpy as np
import matplotlib.pyplot as plt

# Function to display x and ceiling(x) values
def display_values(x, y):
    print("x-values and corresponding ceiling(x) values:")
    for i in range(len(x)):
        print(f"x = {x[i]:.2f}, ceil(x) = {y[i]}")

# Create the plot
def create_ceiling_plot():
    # Define the range for x-axis
    x_min = -5
    x_max = 5
    x_step = 0.1
    x = np.arange(x_min, x_max, x_step)

    # Calculate the ceiling of x
    y = np.ceil(x)

    # Display the values
    display_values(x, y)

    # Create the plot
    plt.step(x, y, where='post', label=r'$y = \lceil x \rceil$', color='blue')

    # Plot every point as a marker
    plt.scatter(x, y, color='red', s=10)

    # Label the axes
    plt.xlabel('x')
    plt.ylabel('y')

    # Add a title to the graph
    plt.title('Ceiling Function')

    # Display a grid
    plt.grid(True)

    # Add a legend
    plt.legend()

    # Set the limits for better viewing
    plt.xlim(x_min, x_max)
    plt.ylim(x_min, x_max + 1)

    # Show the plot
    plt.show()

# Call the function to create and display the plot
create_ceiling_plot()
