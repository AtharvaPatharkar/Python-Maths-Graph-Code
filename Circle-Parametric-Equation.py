import numpy as np
import matplotlib.pyplot as plt

# Function to display theta, x, and y values
def display_values(theta, x, y):
    print("theta (degrees), x, and y values (Circle Parametric):")
    for i in range(len(theta)):
        print(f"theta = {np.degrees(theta[i]):.1f}°, x = {x[i]:.2f}, y = {y[i]:.2f}")

# Create the plot
def create_parametric_circle():
    # Define theta values from 0 to 2*pi
    theta = np.linspace(0, 2 * np.pi, 360)

    # Define radius
    r = 3  # radius of the circle

    # Calculate x and y using parametric equations
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Display the theta, x, and y values
    display_values(theta, x, y)

    # Create the plot
    plt.figure(figsize=(6,6))
    plt.plot(x, y, label=r'$x = r\cos(\theta),\quad y = r\sin(\theta)$', color='purple')

    # Plot every point as a marker
    plt.scatter(x, y, color='red', s=10)

    # Label the axes
    plt.xlabel('x')
    plt.ylabel('y')

    # Add a title
    plt.title('Circle (Parametric Equations)')

    # Add a grid
    plt.grid(True)
    plt.legend()

    # Set equal aspect ratio
    plt.axis('equal')  # so the circle doesn't look like an ellipse

    # Set limits for better view
    plt.xlim(-r-1, r+1)
    plt.ylim(-r-1, r+1)

    # Show the plot
    plt.show()

# Call the function to create and display the circle
create_parametric_circle()
