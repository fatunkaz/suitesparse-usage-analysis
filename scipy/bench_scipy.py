import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import time

from scipy.sparse.linalg import use_solver, spsolve, factorized

np.random.seed(42)

def make_sparse_spd(n, density=0.01):
    """Создать разреженную СПД матрицу размера n x n"""
    A = sp.random(n, n, density=density, format='csc', dtype=np.float64)
    A = A @ A.T + sp.eye(n, format='csc') * n
    return A.tocsc()

def make_sparse_nonsym(n, density=0.01):
    """Создать разреженную несимметричную матрицу размера n x n"""
    A = sp.random(n, n, density=density, format='csc', dtype=np.float64)
    A = A + sp.eye(n, format='csc') * n
    return A.tocsc()

sizes = [500, 1000, 2000, 5000]

print("=" * 70)
print("Сценарий 1 и 2: spsolve и factorized (UMFPACK vs SuperLU)")
print("=" * 70)

for n in sizes:
    A = make_sparse_nonsym(n)
    b = np.random.randn(n)

    # UMFPACK через spsolve
    use_solver(useUmfpack=True)
    t0 = time.perf_counter()
    x1 = spsolve(A, b)
    t_umfpack = time.perf_counter() - t0

    # SuperLU через spsolve
    use_solver(useUmfpack=False)
    t0 = time.perf_counter()
    x2 = spsolve(A, b)
    t_superlu = time.perf_counter() - t0

    # factorized (UMFPACK) - многократное решение
    use_solver(useUmfpack=True)
    t0 = time.perf_counter()
    solve = factorized(A)
    x3 = solve(b)
    x4 = solve(b)
    x5 = solve(b)
    t_factorized = time.perf_counter() - t0

    err1 = np.linalg.norm(A @ x1 - b) / np.linalg.norm(b)
    err2 = np.linalg.norm(A @ x2 - b) / np.linalg.norm(b)

    print(f"n={n:5d} | UMFPACK: {t_umfpack:.4f}s | SuperLU: {t_superlu:.4f}s | "
          f"factorized(3x): {t_factorized:.4f}s | err_umf={err1:.2e} | err_slu={err2:.2e}")

