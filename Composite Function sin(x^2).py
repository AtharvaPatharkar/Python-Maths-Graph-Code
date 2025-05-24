import numpy as np
import matplotlib.pyplot as plt

# Function to display x and y values
def display_values(x, y):
    print("x-values and corresponding y-values (y = sin(x²)):")
    for xi, yi in zip(x, y):
        print(f"x = {xi:.2f}, y = {yi:.2f}")

# Create the plot
def create_composite_sin_x2_plot():
    # Define x values
    x_min = -5
    x_max = 5
    x_step = 0.01
    x = np.arange(x_min, x_max + x_step, x_step)  # Include x_max

    # Calculate y = sin(x^2)
    y = np.sin(x**2)

    # Display x and y values
    display_values(x, y)

    # Create the plot
    plt.figure(figsize=(10,6))
    plt.plot(x, y, label=r'$y = \sin(x^2)$', color='purple')

    # Plot points as markers (optional)
    plt.scatter(x, y, color='red', s=5)

    # Label the axes
    plt.xlabel('x')
    plt.ylabel('y')

    # Add a title
    plt.title('Composite Function: y = sin(x²)')

    # Add grid and legend
    plt.grid(True)
    plt.legend()

    # Set axis limits
    plt.xlim(x_min, x_max)
    plt.ylim(-1.5, 1.5)

    # Show the plot
    plt.show()

# Call the function to create and display the plot
create_composite_sin_x2_plot()
