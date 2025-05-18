import numpy as np
import matplotlib.pyplot as plt

# Function to display r and theta values
def display_values(theta, r):
    print("theta (degrees) and corresponding r values (r = 1 - cos(theta)):")
    for i in range(len(theta)):
        print(f"theta = {np.degrees(theta[i]):.1f}°, r = {r[i]:.2f}")

# Create the plot
def create_cardioid():
    # Define theta values from 0 to 2*pi (full circle)
    theta = np.linspace(0, 2 * np.pi, 360)

    # Calculate r for each theta
    r = 1 - np.cos(theta)

    # Display the theta and r values
    display_values(theta, r)

    # Create a polar plot
    plt.figure(figsize=(6,6))
    ax = plt.subplot(111, polar=True)
    ax.plot(theta, r, label=r'$r = 1 - \cos(\theta)$', color='magenta')

    # Add a title
    plt.title('Cardioid (Polar Plot)', va='bottom')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()

# Call the function to create and display the cardioid
create_cardioid()
