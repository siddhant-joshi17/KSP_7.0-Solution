import numpy as np
import matplotlib.pyplot as plt

# Using a normalized Einstein Angle for simplicity
theta_e = 1.0 

def get_lensed_images(y_source, te):
    """Calculates the vertical positions of the two images for a source at (0, y)."""
    # Using the analytical solution: theta = (beta +/- sqrt(beta^2 + 4*theta_e^2)) / 2
    # Here beta is the magnitude of the source position y_source
    beta = abs(y_source)
    
    if beta == 0:
        return None # Special case for perfect alignment
    
    t_plus = (beta + np.sqrt(beta**2 + 4*te**2)) / 2
    t_minus = (beta - np.sqrt(beta**2 + 4*te**2)) / 2
    
    # Preserve the sign relative to the source position
    sign = 1 if y_source >= 0 else -1
    return [sign * t_plus, sign * t_minus]

# Sequence of y values approaching 0
y_values = [1.5, 0.8, 0.4, 0.1, 0.0]

fig, axes = plt.subplots(1, 5, figsize=(20, 4))

for i, y in enumerate(y_values):
    ax = axes[i]
    
    # 1. Plot Lens at origin
    ax.scatter(0, 0, color='black', s=50, label='Lens' if i==0 else "")
    
    # 2. Plot Source (blue)
    ax.scatter(0, y, color='blue', s=40, label='Source' if i==0 else "")
    
    # 3. Plot Images (red/yellow)
    img_positions = get_lensed_images(y, theta_e)
    
    if img_positions is None:
        # Perfect alignment: Plot the Einstein Ring
        ring = plt.Circle((0, 0), theta_e, color='gold', fill=False, lw=2, label='Einstein Ring')
        ax.add_patch(ring)
    else:
        # Standard case: Plot two discrete points
        ax.scatter([0, 0], img_positions, color='red', s=30, label='Images' if i==0 else "")
    
    # Formatting
    ax.set_title(f"Source at y = {y}")
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    if i == 0:
        ax.legend(loc='upper right', fontsize='small')

plt.tight_layout()
plt.show()
