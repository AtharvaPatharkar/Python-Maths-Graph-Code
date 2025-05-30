import numpy as np
import matplotlib.pyplot as plt

# Function to display x and y values
def display_values(x, y):
    print("x-values and corresponding y-values (y = constant):")
    for xi, yi in zip(x, y):
        print(f"x = {xi:.2f}, y = {yi:.2f}")

# Create the plot
def create_constant_function_plot():
    # Define the constant
    c = 3  # You can change this to any number

    # Define x values
    x_min = -10
    x_max = 10
    x_step = 0.5
    x = np.arange(x_min, x_max + x_step, x_step)  # Include x_max

    # Calculate y = c
    y = np.full_like(x, c)

    # Display x and y values
    display_values(x, y)

    # Create the plot
    plt.figure(figsize=(8,5))
    plt.plot(x, y, label=f'$y = {c}$', color='orange')

    # Plot points as markers
    plt.scatter(x, y, color='red', s=30)

    # Label the axes
    plt.xlabel('x')
    plt.ylabel('y')

    # Add title
    plt.title('Constant Function: y = c')

    # Add grid and legend
    plt.grid(True)
    plt.legend()

    # Set axis limits
    plt.xlim(x_min, x_max)
    plt.ylim(c - 2, c + 2)  # A little room above and below

    # Show the plot
    plt.show()

# Call the function to create and display the plot
create_constant_function_plot()
