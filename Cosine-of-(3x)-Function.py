import numpy as np
import matplotlib.pyplot as plt

# Function to display x and y values
def display_values(x, y):
    print("x-values and corresponding y-values (y = cos(3x)):")
    for xi, yi in zip(x, y):
        print(f"x = {xi:.2f}, y = {yi:.2f}")

# Create the plot
def create_cosine_3x_plot():
    # Define x values
    x_min = -2 * np.pi
    x_max = 2 * np.pi
    x_step = 0.01
    x = np.arange(x_min, x_max + x_step, x_step)

    # Calculate y = cos(3x)
    y = np.cos(3 * x)

    # Display x and y values
    display_values(x, y)

    # Create the plot
    plt.figure(figsize=(10,6))
    plt.plot(x, y, label=r'$y = \cos(3x)$', color='blue')

    # Scatter plot points for better visualization
    plt.scatter(x, y, color='red', s=5)

    # Label the axes
    plt.xlabel('x')
    plt.ylabel('y')

    # Add title
    plt.title('Cosine Function: y = cos(3x)')

    # Add grid and legend
    plt.grid(True)
    plt.legend()

    # Set axis limits
    plt.xlim(x_min, x_max)
    plt.ylim(-1.5, 1.5)

    # Show the plot
    plt.show()

# Call the function to create and display the plot
create_cosine_3x_plot()
