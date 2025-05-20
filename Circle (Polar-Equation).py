import numpy as np
import matplotlib.pyplot as plt

# Function to display theta and r values
def display_values(theta, r):
    print("theta (degrees) and corresponding r values (Circle):")
    for i in range(len(theta)):
        print(f"theta = {np.degrees(theta[i]):.1f}°, r = {r[i]:.2f}")

# Create the polar plot
def create_circle_plot():
    # Define theta from 0 to 2*pi
    theta = np.linspace(0, 2 * np.pi, 360)

    # Define radius r (constant for a circle)
    r = np.full_like(theta, 3)  # Circle of radius 3

    # Display the theta and r values
    display_values(theta, r)

    # Create a polar plot
    plt.figure(figsize=(6,6))
    ax = plt.subplot(111, polar=True)
    ax.plot(theta, r, label=r'$r = 3$', color='blue')

    # Add a title
    plt.title('Circle (Polar Plot)', va='bottom')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()

# Call the function to create and display the circle
create_circle_plot()
