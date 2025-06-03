import numpy as np
import matplotlib.pyplot as plt

# Function to display x and y values
def display_values(x, y):
    print("x-values and corresponding y-values (y = e^{-a x} cos(bx)):")
    for xi, yi in zip(x, y):
        print(f"x = {xi:.2f}, y = {yi:.2f}")

# Create the plot
def create_damped_oscillation_plot():
    # Parameters
    a = 0.1  # Damping coefficient
    b = 5    # Frequency

    # Define x values
    x_min = 0
    x_max = 20
    x_step = 0.01
    x = np.arange(x_min, x_max + x_step, x_step)

    # Calculate y = e^(-a*x) * cos(b*x)
    y = np.exp(-a * x) * np.cos(b * x)

    # Display x and y values
    display_values(x, y)

    # Create the plot
    plt.figure(figsize=(10,6))
    plt.plot(x, y, label=r'$y = e^{-0.1x} \cos(5x)$', color='teal')

    # Scatter plot points
    plt.scatter(x, y, color='red', s=5)

    # Label the axes
    plt.xlabel('x')
    plt.ylabel('y')

    # Add title
    plt.title('Damped Oscillation: y = e^{-0.1x} cos(5x)')

    # Add grid and legend
    plt.grid(True)
    plt.legend()

    # Set axis limits
    plt.xlim(x_min, x_max)
    plt.ylim(-1.5, 1.5)

    # Show the plot
    plt.show()

# Call the function to create and display the plot
create_damped_oscillation_plot()
