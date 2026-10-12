"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x)
def k_imbalance(x):
    return ((2 * x)**2) / ((a - x) * (b - x)) - K

# TODO 2 (method 1): use scipy.optimize.newton
x_newton = newton(k_imbalance, x0=0.5)

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
def objective(x):
    return k_imbalance(x)**2

res_slsqp = minimize(objective, x0=[0.5], method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res_slsqp.x[0]

print(f"Newton x: {x_newton:.4f}")
print(f"SLSQP x:  {x_slsqp:.4f}")

# TODO 4: report equilibrium amounts and plot
h2_eq = a - x_newton
i2_eq = b - x_newton
hi_eq = 2 * x_newton

print(f"Equilibrium Amounts -> H2: {h2_eq:.4f} mol, I2: {i2_eq:.4f} mol, HI: {hi_eq:.4f} mol")

x_vals = np.linspace(0, 0.95, 200)
h2_vals = a - x_vals
i2_vals = b - x_vals
hi_vals = 2 * x_vals

plt.figure(figsize=(8, 5))
plt.plot(x_vals, h2_vals, label='$H_2$', color='blue')
plt.plot(x_vals, i2_vals, label='$I_2$', color='green')
plt.plot(x_vals, hi_vals, label='$HI$', color='orange')
plt.axvline(x_newton, color='red', linestyle='--', label=f'Equilibrium Point ($x \\approx {x_newton:.2f}$)')

plt.xlabel('Reaction Extent ($x$)')
plt.ylabel('Amount (mol)')
plt.title('Chemical Equilibrium Composition ($K = 15.6$)')
plt.legend()
plt.grid(True)

plt.savefig('equilibrium.png', dpi=150)
print("Saved figure as equilibrium.png")