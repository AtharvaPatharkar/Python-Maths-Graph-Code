import numpy as np
import matplotlib.pyplot as plt

# Define the arccosine and arcsine functions
def arccosine_function(x):
    return np.arccos(x)

def arcsine_function(x):
    return np.arcsin(x)

# Set up x values (valid for both arccos and arcsin: [-1, 1])
x = np.linspace(-1, 1, 100)

# Set initial function to arccosine
current_function = arccosine_function
y = current_function(x)

# Create the plot
fig, ax = plt.subplots(figsize=(8, 5))

# Plot the initial graph (arccosine function)
line, = ax.plot(x, y, label='f(x) = arccos(x)', color='blue')
ax.set_title('Click on the graph to switch between arccos(x) and arcsin(x)')
ax.set_xlabel('x')
ax.set_ylabel('f(x) (in radians)')
ax.axhline(0, color='black', linewidth=0.5)  # Draw x-axis
ax.axvline(0, color='black', linewidth=0.5)  # Draw y-axis
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Function to toggle between arccosine and arcsine
def on_click(event):
    global current_function, line
    if current_function == arccosine_function:
        current_function = arcsine_function
        line.set_ydata(current_function(x))  # Update y-data to arcsin(x)
        line.set_label('f(x) = arcsin(x)')
    else:
        current_function = arccosine_function
        line.set_ydata(current_function(x))  # Update y-data to arccos(x)
        line.set_label('f(x) = arccos(x)')
    
    ax.legend()  # Update legend
    plt.draw()  # Redraw the plot

# Connect the click event
fig.canvas.mpl_connect('button_press_event', on_click)

# Show the plot
plt.show()
