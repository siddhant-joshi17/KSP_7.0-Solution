import matplotlib.pyplot as plt
import numpy as np

def solve_optics(x0, y0):
    f = 1.0
    
    # 1. Analytical Calculation
    if x0 == -f:
        print("Image is at infinity (Parallel rays)")
        x_img, y_img = None, None
    else:
        x_img = (x0 * f) / (x0 + f)
        y_img = y0 * (x_img / x0)
        print(f"Image Position: ({x_img:.2f}, {y_img:.2f})")

    # 2. Plotting
    plt.figure(figsize=(10, 5))
    
    # Draw Lens
    plt.plot([0, 0], [-1.5, 1.5], 'k-', lw=3, label="Thin Lens")
    # Draw Principal Axis
    plt.axhline(0, color='black', lw=1, ls='--')
    # Plot Focal Points
    plt.plot([-f, f], [0, 0], 'ro', label="Foci")

    # Draw Incident Ray (Horizontal)
    plt.annotate('', xy=(0, y0), xytext=(x0, y0),
                 arrowprops=dict(arrowstyle='->', color='blue'))
    
    # Draw Refracted Ray
    if abs(y0) <= 1.5:
        # Define a point further along the path to draw the line
        x_far = 3.0 
        y_far = -y0 * (x_far - 1)
        plt.plot([0, x_far], [y0, y_far], 'r--', label="Refracted Ray")

    # Plot Source
    plt.plot(x0, y0, 'go', label="Source")
    if x_img is not None:
        plt.plot(x_img, y_img, 'mo', label="Image")

    plt.xlim(-3, 3)
    plt.ylim(-2, 2)
    plt.legend()
    plt.grid(True)
    plt.show()

# Example: Source at (-2, 0.5)
solve_optics(-2.0, 0.5)
