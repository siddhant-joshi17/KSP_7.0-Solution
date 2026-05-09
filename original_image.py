import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def reconstruct_source(csv_path):
    # 1. Load the lensed points
    # Assuming columns are 'theta_x' and 'theta_y' in units of theta_E
    try:
        data = pd.read_csv(csv_path)
        theta_x = data['theta_x'].values
        theta_y = data['theta_y'].values
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return

    # 2. Apply Inverse Transformation
    # Since coordinates are already normalized (theta/theta_E), we use theta_E = 1
    theta_sq = theta_x**2 + theta_y**2
    
    # beta = theta * (1 - 1/theta^2)
    beta_x = theta_x * (1 - 1/theta_sq)
    beta_y = theta_y * (1 - 1/theta_sq)

    # 3. Plotting
    plt.figure(figsize=(12, 5))

    # Plot Lensed Image (Observed)
    plt.subplot(1, 2, 1)
    plt.scatter(theta_x, theta_y, s=3.5, color='red', alpha=0.5)
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.title("Lensed Image (From CSV)")
    plt.xlabel(r"$\theta_x / \theta_E$")
    plt.ylabel(r"$\theta_y / \theta_E$")
    plt.axis('equal')

    # Plot Reconstructed Source (Actual)
    plt.subplot(1, 2, 2)
    plt.scatter(beta_x, beta_y, s=3.5, color='blue', alpha=0.5)
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.title("Reconstructed Original Source")
    plt.xlabel(r"$\beta_x / \theta_E$")
    plt.ylabel(r"$\beta_y / \theta_E$")
    plt.axis('equal')

    plt.tight_layout()
    plt.show()

# To run this, ensure 'lensed_points.csv' is in your directory
# reconstruct_source('lensed_points.csv')
