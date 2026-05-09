import numpy as np
import matplotlib.pyplot as plt

# Using constants from Part (c) or defining standard scale
theta_e = 1.0  # Normalized Einstein Angle

def get_lensed_points(beta_x, beta_y, te):
    """Calculates the two image points for a given source point."""
    beta_mag = np.sqrt(beta_x**2 + beta_y**2)
    if beta_mag == 0:
        return [] # Alignment at origin creates a ring
    
    # Image magnitudes from quadratic solution
    t_plus = (beta_mag + np.sqrt(beta_mag**2 + 4*te**2)) / 2
    t_minus = (beta_mag - np.sqrt(beta_mag**2 + 4*te**2)) / 2
    
    # Vector components for the two images
    img1 = (t_plus * beta_x / beta_mag, t_plus * beta_y / beta_mag)
    img2 = (t_minus * beta_x / beta_mag, t_minus * beta_y / beta_mag)
    return [img1, img2]

def simulate_extended_source(x0, y0, R, num_points=250):
    # 1. Sample points within the circle
    r = R * np.sqrt(np.random.rand(num_points))
    phi = 2 * np.pi * np.random.rand(num_points)
    
    src_x = x0 + r * np.cos(phi)
    src_y = y0 + r * np.sin(phi)
    
    img_x, img_y = [], []
    
    # 2. Calculate lensed images for each point
    for i in range(num_points):
        images = get_lensed_points(src_x[i], src_y[i], theta_e)
        for im in images:
            img_x.append(im[0])
            img_y.append(im[1])
            
    # 3. Plotting
    plt.figure(figsize=(8, 8))
    
    # Original Source
    plt.scatter(src_x, src_y, s=3.5, color='blue', label='Original Source Points', alpha=0.6)
    
    # Lensed Images
    plt.scatter(img_x, img_y, s=3.5, color='red', label='Lensed Image Points', alpha=0.6)
    
    # Lens at origin
    plt.scatter(0, 0, color='black', marker='x', label='Lens (Origin)')
    
    # Einstein Ring for reference
    circle = plt.Circle((0, 0), theta_e, color='gray', fill=False, linestyle='--', alpha=0.3)
    plt.gca().add_patch(circle)
    
    plt.axhline(0, color='black', lw=0.5, alpha=0.2)
    plt.axvline(0, color='black', lw=0.5, alpha=0.2)
    plt.title(f"Lensing of Extended Source at ({x0}, {y0})")
    plt.xlabel(r"$\theta_x / \theta_E$")
    plt.ylabel(r"$\theta_y / \theta_E$")
    plt.legend()
    plt.axis('equal')
    plt.grid(True, alpha=0.2)
    plt.show()

# Example: Source slightly offset from the lens to see distortion
simulate_extended_source(x0=1.2, y0=0.5, R=0.3)
