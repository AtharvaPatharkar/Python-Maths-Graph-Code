import numpy as np
import matplotlib.pyplot as plt

# Function to display x and y values
def display_values(x, y):
    print("x-values and corresponding y-values (y = mx + b):")
    for xi, yi in zip(x, y):
        print(f"x = {xi:.2f}, y = {yi:.2f}")

# Create the plot
def create_decreasing_linear_plot():
    # Define slope and intercept
    m = -2  # Negative slope for decreasing line
    b = 5   # y-intercept

    # Define x values
    x_min = -5
    x_max = 5
    x_step = 0.5
    x = np.arange(x_min, x_max + x_step, x_step)

    # Calculate y = m*x + b
    y = m * x + b

    # Display x and y values
    display_values(x, y)

    # Create the plot
    plt.figure(figsize=(8,5))
    plt.plot(x, y, label=f'$y = {m}x + {b}$', color='brown')

    # Plot points as markers
    plt.scatter(x, y, color='red', s=30)

    # Label the axes
    plt.xlabel('x')
    plt.ylabel('y')

    # Add title
    plt.title('Decreasing Linear Function: y = mx + b')

    # Add grid and legend
    plt.grid(True)
    plt.legend()

    # Set axis limits
    plt.xlim(x_min, x_max)
    plt.ylim(min(y)-2, max(y)+2)

    # Show the plot
    plt.show()

# Call the function to create and display the plot
create_decreasing_linear_plot()
