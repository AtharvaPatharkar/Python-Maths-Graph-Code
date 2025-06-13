import numpy as np
import matplotlib.pyplot as plt

# Function to plot Ellipse (Cartesian Equation)
def create_ellipse_plot():
    # Define the semi-major axis (a) and semi-minor axis (b)
    a = 5  # Semi-major axis
    b = 3  # Semi-minor axis

    # Parametric angle values
    theta = np.linspace(0, 2 * np.pi, 1000)

    # Parametric equations for x and y
    x = a * np.cos(theta)
    y = b * np.sin(theta)

    # Create the plot
    plt.figure(figsize=(8,6))
    plt.plot(x, y, label=f'Ellipse: $x^2/{a**2} + y^2/{b**2} = 1$', color='purple')

    # Add title and labels
    plt.title('Ellipse: Cartesian Equation')
    plt.xlabel('x')
    plt.ylabel('y')

    # Set axis limits to create a proper aspect ratio
    plt.xlim(-a-1, a+1)
    plt.ylim(-b-1, b+1)

    # Set aspect ratio to equal for accurate ellipse appearance
    plt.gca().set_aspect('equal', adjustable='box')

    # Add grid and legend
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.show()

# Call the function to create and display the plot
create_ellipse_plot()
