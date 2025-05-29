import numpy as np
import matplotlib.pyplot as plt

# Function to display x and y values
def display_values(x, y):
    print("x-values and corresponding y-values (y = e^(sin(x))):")
    for i in range(len(x)):
        print(f"x = {x[i]:.2f}, y = {y[i]:.2f}")

# Create the plot
def create_composite_exp_sin_x_plot():
    # Define x values
    x_min = -10
    x_max = 10
    x_step = 0.1
    x = np.arange(x_min, x_max, x_step)

    # Calculate y = e^(sin(x))
    y = np.exp(np.sin(x))

    # Display x and y values
    display_values(x, y)

    # Create the plot
    plt.plot(x, y, label=r'$y = e^{\sin(x)}$', color='green')

    # Optionally, plot every point as a red marker
    plt.scatter(x, y, color='red', s=10)

    # Label the axes
    plt.xlabel('x')
    plt.ylabel('y')

    # Add a title
    plt.title('Composite Function: y = e^(sin(x))')

    # Add a grid
    plt.grid(True)
    plt.legend()

    # Set limits for clarity
    plt.xlim(x_min, x_max)
    plt.ylim(0, np.exp(1)+0.5)  # e^1 ≈ 2.718, so set y-axis slightly higher

    # Show the plot
    plt.show()

# Call the function to create and display the plot
create_composite_exp_sin_x_plot()
