"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read kinetics.csv (columns time, concentration) into arrays t, C.
#         Set C0 = the first concentration.
data = np.loadtxt('kinetics.csv', delimiter=',', skiprows=1)
t = data[:, 0]
C_measured = data[:, 1]
C0 = C_measured[0]

# TODO 2: write total_error(k) = sum of (measured - C0*exp(-k*t))^2.
#         This is the "how bad" number: small when the model matches the data.
def total_error(k):
    C_pred = C0 * np.exp(-k * t)
    return np.sum((C_measured - C_pred)**2)

# TODO 3: minimise total_error with scipy.optimize.minimize (method "SLSQP",
#         bounds [(0, 5)], start x0=0.5). Print the fitted k.
res = minimize(total_error, x0=[0.5], method="SLSQP", bounds=[(0, 5)])
fitted_k = res.x[0]
print(f"Fitted rate constant k: {fitted_k:.4f}")

# TODO 4: plot the measured data (points) and your fitted curve (line) together.
#         Save as kinetics.png.
plt.figure(figsize=(8, 5))
plt.scatter(t, C_measured, color='red', label='Measured Data', zorder=5)

t_dense = np.linspace(t.min(), t.max(), 200)
C_fit = C0 * np.exp(-fitted_k * t_dense)
plt.plot(t_dense, C_fit, color='blue', label=f'Fitted Curve ($k={fitted_k:.4f}$)')

plt.xlabel('Time')
plt.ylabel('Concentration ($C$)')
plt.title('First-Order Reaction Rate Fitting')
plt.legend()
plt.grid(True)

plt.savefig('kinetics.png', dpi=150)
print("Saved figure as kinetics.png")