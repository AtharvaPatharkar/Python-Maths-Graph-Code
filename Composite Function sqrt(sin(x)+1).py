import numpy as np
import matplotlib.pyplot as plt

# Function to display x and y values
def display_values(x, y):
    print("x-values and corresponding y-values (y = sqrt(sin(x) + 1)):")
    for xi, yi in zip(x, y):
        print(f"x = {xi:.2f}, y = {yi:.2f}")

# Create the plot
def create_composite_sqrt_sin_x_plot():
    # Define x values
    x_min = -2 * np.pi
    x_max = 2 * np.pi
    x_step = 0.01
    x = np.arange(x_min, x_max + x_step, x_step)  # Include x_max

    # Calculate y = sqrt(sin(x) + 1)
    y = np.sqrt(np.sin(x) + 1)

    # Display x and y values
    display_values(x, y)

    # Create the plot
    plt.figure(figsize=(10,6))
    plt.plot(x, y, label=r'$y = \sqrt{\sin(x) + 1}$', color='darkgreen')

    # Plot points as small markers
    plt.scatter(x, y, color='red', s=5)

    # Label the axes
    plt.xlabel('x')
    plt.ylabel('y')

    # Add title
    plt.title('Composite Function: y = sqrt(sin(x) + 1)')

    # Add grid and legend
    plt.grid(True)
    plt.legend()

    # Set axis limits
    plt.xlim(x_min, x_max)
    plt.ylim(0, np.sqrt(2) + 0.5)  # sqrt(2) ~ 1.414

    # Show the plot
    plt.show()

# Call the function to create and display the plot
create_composite_sqrt_sin_x_plot()
