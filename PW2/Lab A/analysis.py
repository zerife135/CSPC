import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
data = np.loadtxt('freefall.csv', delimiter=',', skiprows=1)
t = data[:, 0]
y = data[:, 1]

# TODO 2: compute velocity v = derivative of y w.r.t. t (np.gradient)
#         and acceleration a = derivative of v w.r.t. t (np.gradient again)
v = np.gradient(y, t)
a = np.gradient(v, t)

print(f"Mean acceleration: {np.mean(a):.2f} m/s²")
print(f"Standard deviation of acceleration: {np.std(a):.2f} m/s²")

# TODO 3: integrate a back up to recover velocity and position
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

max_diff = np.max(np.abs(y_rec - y))
print(f"Max difference between original and recovered position: {max_diff:.4f} m")

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
fig, axes = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# Panel 1: Position
axes[0].plot(t, y, label='Original Position $y$', color='blue')
axes[0].plot(t, y_rec, '--', label='Recovered Position $y_{rec}$', color='orange')
axes[0].set_ylabel('Position (m)')
axes[0].set_title('Motion from Tracking Data')
axes[0].legend()
axes[0].grid(True)

# Panel 2: Velocity
axes[1].plot(t, v, color='green', label='Velocity $v$')
axes[1].set_ylabel('Velocity (m/s)')
axes[1].legend()
axes[1].grid(True)

# Panel 3: Acceleration
axes[2].plot(t, a, color='red', alpha=0.7, label='Acceleration $a$')
axes[2].axhline(-9.81, color='black', linestyle='--', label='True $-9.81\\text{ m/s}^2$')
axes[2].set_xlabel('Time (s)')
axes[2].set_ylabel('Acceleration (m/s²)')
axes[2].legend()
axes[2].grid(True)

plt.tight_layout()
plt.savefig('motion.png', dpi=150)
print("Saved figure as motion.png")