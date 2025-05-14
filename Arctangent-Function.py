import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def arccosine_function(x):
    return np.arccos(x)

def arcsine_function(x):
    return np.arcsin(x)

def arctangent_function(x):
    return np.arctan(x)

# Set up x values (valid for all three functions: [-1, 1] for arccos, arcsin, and larger for arctan)
x = np.linspace(-10, 10, 500)

# Initial function is arccosine
current_function = arccosine_function
y = current_function(x)

# Create the plot
fig, ax = plt.subplots(figsize=(8, 5))

# Plot the initial graph (arccosine function)
line, = ax.plot(x, y, label='f(x) = arccos(x)', color='blue')
ax.set_title('Click to switch between functions and scroll to zoom')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axhline(0, color='black', linewidth=0.5)  # Draw x-axis
ax.axvline(0, color='black', linewidth=0.5)  # Draw y-axis
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Zoom factor (initial)
zoom_factor = 1

# Function to toggle between arccosine, arcsine, and arctangent
def on_click(event):
    global current_function, line
    if current_function == arccosine_function:
        current_function = arcsine_function
        line.set_ydata(current_function(x))  # Update y-data to arcsin(x)
        line.set_label('f(x) = arcsin(x)')
    elif current_function == arcsine_function:
        current_function = arctangent_function
        line.set_ydata(current_function(x))  # Update y-data to arctan(x)
        line.set_label('f(x) = arctan(x)')
    else:
        current_function = arccosine_function
        line.set_ydata(current_function(x))  # Update y-data to arccos(x)
        line.set_label('f(x) = arccos(x)')
    
    ax.legend()  # Update legend
    plt.draw()  # Redraw the plot

# Function to zoom in/out based on mouse scroll
def on_scroll(event):
    global zoom_factor

    # Zoom in
    if event.button == 'up':
        zoom_factor *= 1.1  # Zoom in by 10%
    # Zoom out
    elif event.button == 'down':
        zoom_factor /= 1.1  # Zoom out by 10%

    # Update axis limits based on zoom factor
    ax.set_xlim(-zoom_factor * 10, zoom_factor * 10)  # Limit x-axis
    ax.set_ylim(-zoom_factor * 2, zoom_factor * 2)  # Limit y-axis
    plt.draw()  # Redraw the plot

# Connect the click and scroll events
fig.canvas.mpl_connect('button_press_event', on_click)
fig.canvas.mpl_connect('scroll_event', on_scroll)

# Show the plot
plt.show()
