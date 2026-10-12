"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A: minimise f three ways from x0=0 and print each result:
# (1) Gradient descent by hand
x_gd = 0.0
lr = 0.1
for _ in range(100):
    x_gd = x_gd - lr * df(x_gd)

# (2) scipy.optimize.newton
x_newton = newton(df, x0=0.0, fprime=d2f)

# (3) scipy.optimize.minimize
res_slsqp = minimize(f, x0=0.0, method="SLSQP")

print("=== Part 2A Results (f(x) from x0=0) ===")
print(f"(1) Gradient Descent: {x_gd:.4f}")
print(f"(2) Newton's Method:  {x_newton:.4f}")
print(f"(3) SLSQP Minimizer:  {res_slsqp.x[0]:.4f}\n")


# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.
def run_2b(x0):
    # (1) Gradient Descent
    x_gd = x0
    for _ in range(1000):
        x_gd = x_gd - 0.01 * dg(x_gd)

    # (2) Newton's Method on dg(x)=0
    x_newton = newton(dg, x0=x0, fprime=d2g)
    second_deriv = d2g(x_newton)
    point_type = "minimum" if second_deriv > 0 else "maximum"

    # (3) SLSQP
    res_slsqp = minimize(g, x0=x0, method="SLSQP")

    print(f"=== Part 2B Results (g(x) from x0={x0}) ===")
    print(f"(1) Gradient Descent: {x_gd:.4f}")
    print(f"(2) Newton's Method:  {x_newton:.4f} (d2g = {second_deriv:.2f} -> {point_type})")
    print(f"(3) SLSQP Minimizer:  {res_slsqp.x[0]:.4f}\n")

run_2b(0.0)
run_2b(2.0)