import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Constants for the exact equation
theta_e = 0.1  # Einstein angle in radians (large for visibility)

def exact_lens_eq(theta, beta, theta_e):
    return theta - beta - (theta_e**2 / np.tan(theta))

def solve_part_b():
    # Source positions normalized by theta_e
    beta_ratios = np.linspace(0.01, 5, 200)
    beta_vals = beta_ratios * theta_e
    
    exact_sols = []
    approx_sols = []
    
    for b in beta_vals:
        # Analytical approximation: theta = (beta + sqrt(beta^2 + 4*theta_e^2)) / 2
        theta_approx = (b + np.sqrt(b**2 + 4*theta_e**2)) / 2
        approx_sols.append(theta_approx)
        
        # Numerical solution for the exact trigonometric equation
        sol = fsolve(exact_lens_eq, theta_approx, args=(b, theta_e))
        exact_sols.append(sol[0])
        
    error = np.abs((np.array(exact_sols) - np.array(approx_sols)) / np.array(exact_sols)) * 100
    
    # Plotting
    plt.figure(figsize=(8, 5))
    plt.plot(beta_ratios, error, color='crimson', lw=2)
    plt.axhline(y=1.0, color='black', ls='--', label='1% Error Threshold')
    plt.xlabel(r'$\beta / \theta_E$')
    plt.ylabel('Percentage Error (%)')
    plt.title('Error in Small-Angle Approximation')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

solve_part_b()
