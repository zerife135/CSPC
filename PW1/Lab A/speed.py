import time
from decay import simulate, simulate_loop

N0 = 200000
lam = 0.4
t0 = time.perf_counter()
simulate_loop(N0, lam)
t_loop = time.perf_counter() - t0
t0 = time.perf_counter()
simulate(N0, lam)
t_numpy = time.perf_counter() - t0

speedup = t_loop / t_numpy

print(f"Loop time:  {t_loop:.4f} s")
print(f"NumPy time: {t_numpy:.4f} s")
print(f"Speed-up:   {speedup:.1f}x faster")