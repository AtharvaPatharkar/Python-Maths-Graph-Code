import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

x = np.linspace(-50, 10, 1000)
y = gamma(x)

plt.plot(x, y)
plt.ylim(-50, 50)  # Limit the y-axis for better visibility
plt.grid(True)
plt.show()
