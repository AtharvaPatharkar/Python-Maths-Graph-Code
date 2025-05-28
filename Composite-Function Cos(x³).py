import numpy as np
import matplotlib.pyplot as plt

# Function to display x and y values
def display_values(x, y):
    print("x-values and corresponding y-values (y = cos(x³)):")
    for i in range(len(x)):
        print(f"x = {x[i]:.2f}, y = {y[i]:.2f}")

# Create the plot
def create_composite_cos_x3_plot():
    # Define x values
    x_min = -2
    x_max = 2
    x_step = 0.01
    x = np.arange(x_min, x_max, x_step)

    # Calculate y = cos(x^3)
    y = np.cos(x**3)

    # Display x and y values
    display_values(x, y)

    # Create the plot
    plt.plot(x, y, label=r'$y = \cos(x^3)$', color='teal')

    # Plot every point as a marker (optional, can be skipped if too crowded)
    plt.scatter(x, y, color='red', s=10)

    # Label the axes
    plt.xlabel('x')
    plt.ylabel('y')

    # Add a title
    plt.title('Composite Function: y = cos(x³)')

    # Add a grid
    plt.grid(True)
    plt.legend()

    # Set limits
    plt.xlim(x_min, x_max)
    plt.ylim(-1.5, 1.5)

    # Show the plot
    plt.show()

# Call the function to create and display the plot
create_composite_cos_x3_plot()
