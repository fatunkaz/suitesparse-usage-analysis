import numpy as np
import scipy.sparse as sps
from scipy.optimize import linprog
import time

np.random.seed(42)

print("=" * 70)
print("Сценарий 3: CHOLMOD в linprog (метод внутренней точки)")
print("=" * 70)

for n in [100, 500, 1000, 2000]:
    m = n // 2
    A_eq = sps.random(m, n, density=0.05, format='csc')
    x0 = np.abs(np.random.randn(n)) + 0.1
    b_eq = A_eq @ x0
    c = np.random.randn(n)

    t0 = time.perf_counter()
    res_ip = linprog(c, A_eq=A_eq, b_eq=b_eq,
                     method='interior-point',
                     options={'sparse': True, 'cholesky': True})
    t_ip = time.perf_counter() - t0

    t0 = time.perf_counter()
    res_highs = linprog(c, A_eq=A_eq, b_eq=b_eq, method='highs')
    t_highs = time.perf_counter() - t0

    print(f"n={n:5d}, m={m:4d} | interior-point: {t_ip:.4f}s "
          f"(iters={res_ip.nit}) | HiGHS: {t_highs:.4f}s | "
          f"status_ip: {res_ip.status}")