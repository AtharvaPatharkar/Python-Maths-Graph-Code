import numpy as np
import matplotlib.pyplot as plt

# Define the numerator (P(x)) and denominator (Q(x)) coefficients
# Example: y = (x^2 - 3x + 2) / (x^2 - 4)
numerator_coeffs = [1, -3, 2]  # Coefficients of P(x): x^2 - 3x + 2
denominator_coeffs = [1, 0, -4]  # Coefficients of Q(x): x^2 - 4

# Define the rational function
def rational_function(x):
    P = np.polyval(numerator_coeffs, x)
    Q = np.polyval(denominator_coeffs, x)
    return P / Q

# Print the rational equation
numerator_str = " + ".join([f"{coef}x^{i}" if i != 0 else f"{coef}" 
                            for i, coef in enumerate(numerator_coeffs[::-1])])
denominator_str = " + ".join([f"{coef}x^{i}" if i != 0 else f"{coef}" 
                              for i, coef in enumerate(denominator_coeffs[::-1])])
print(f"Rational Equation: y = ({numerator_str}) / ({denominator_str})")

# Generate x values, avoiding division by zero
x_vals = np.linspace(-10, 10, 500)
y_vals = rational_function(x_vals)

# ---- Finding vertical asymptotes ----
# Vertical asymptotes occur where the denominator is 0
asymptotes = np.roots(denominator_coeffs)

# ---- Finding critical points ----
# First derivative: dy/dx = [P'(x)Q(x) - P(x)Q'(x)] / Q(x)^2
P_prime = np.polyder(numerator_coeffs)  # Derivative of P(x)
Q_prime = np.polyder(denominator_coeffs)  # Derivative of Q(x)
critical_points = np.roots(np.polysub(np.polymul(P_prime, denominator_coeffs), np.polymul(Q_prime, numerator_coeffs)))

# ---- Finding roots ----
# The roots of the rational function occur where the numerator is 0
roots = np.roots(numerator_coeffs)

# Print asymptotes, roots, and critical points
print("\nVertical Asymptotes (where denominator = 0):")
for asymptote in asymptotes:
    print(f"x = {asymptote:.2f}")

print("\nRoots (where numerator = 0):")
for root in roots:
    print(f"x = {root:.2f}, y = 0")

print("\nCritical Points (Local Minima/Maxima):")
for point in critical_points:
    if np.isreal(point):
        point = point.real
        y_critical = rational_function(point)
        print(f"x = {point:.2f}, y = {y_critical:.2f}")

# ---- Plot the rational function ----
plt.plot(x_vals, y_vals, label=f'y = ({numerator_str}) / ({denominator_str})', color='b')

# Mark asymptotes
for asymptote in asymptotes:
    plt.axvline(asymptote, color='r', linestyle='--', label=f'Asymptote x = {asymptote:.2f}')

# Mark roots
for root in roots:
    plt.plot(root, 0, 'go', label=f'Root ({root:.2f}, 0)', markersize=8)

# Mark critical points (local minima/maxima)
for point in critical_points:
    if np.isreal(point):
        point = point.real
        plt.plot(point, rational_function(point), 'ro', label=f'Critical Point ({point:.2f}, {rational_function(point):.2f})', markersize=8)

# Add labels and title
plt.title('Rational Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Add a legend
plt.legend()

# Show a grid
plt.grid(True)

# Display the plot
plt.show()
