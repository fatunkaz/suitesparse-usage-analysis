import numpy as np
import scipy.sparse as sps
from scipy.optimize import linprog
import time
import warnings
warnings.filterwarnings('ignore')

np.random.seed(42)

print("=" * 70)
print("Сценарий 3: CHOLMOD через linprog interior-point, sparse=True")
print("=" * 70)

for n in [100, 500, 1000, 2000]:
    m = n // 2
    A_eq = sps.random(m, n, density=0.05, format='csc')
    x0 = np.abs(np.random.randn(n)) + 0.1
    b_eq = A_eq @ x0
    c = np.random.randn(n)

    # С CHOLMOD (sparse=True, cholesky=True)
    t0 = time.perf_counter()
    res = linprog(c, A_eq=A_eq, b_eq=b_eq,
                  method='interior-point',
                  options={'sparse': True,
                           'cholesky': True,
                           'disp': False})
    t_cholmod = time.perf_counter() - t0

    # Без CHOLMOD (sparse=True, cholesky=False — через UMFPACK)
    t0 = time.perf_counter()
    res2 = linprog(c, A_eq=A_eq, b_eq=b_eq,
                   method='interior-point',
                   options={'sparse': True,
                            'cholesky': False,
                            'disp': False})
    t_umfpack = time.perf_counter() - t0

    # Без разреженности (dense Cholesky)
    t0 = time.perf_counter()
    res3 = linprog(c, A_eq=A_eq.toarray(), b_eq=b_eq,
                   method='interior-point',
                   options={'sparse': False,
                            'cholesky': True,
                            'disp': False})
    t_dense = time.perf_counter() - t0

    print(f"n={n:5d}, m={m:4d} | "
          f"sparse+cholesky: {t_cholmod:.4f}s (iters={res.nit}) | "
          f"sparse+umfpack: {t_umfpack:.4f}s (iters={res2.nit}) | "
          f"dense: {t_dense:.4f}s (iters={res3.nit})")
