# SciPy experiments

## Environment
- OS: Debian GNU/Linux (WSL2, x86-64)
- Python 3.13, SciPy 1.15.3, SuiteSparse 7.10.1
- scikit-umfpack 0.4.2, scikit-sparse 0.5.0

## Installation
```bash
sudo apt-get install -y swig
pip install scikit-umfpack scikit-sparse --break-system-packages
```

## Scripts

### bench_scipy.py — Scenarios 1 & 2: spsolve and factorized (UMFPACK vs SuperLU)
```bash
python3 bench_scipy.py
```
Compares UMFPACK and SuperLU performance for sparse nonsymmetric matrices
of sizes n=500, 1000, 2000, 5000 with 1% density.

### bench_scipy3.py — Scenario 3: CHOLMOD vs UMFPACK vs dense Cholesky
```bash
python3 bench_scipy3.py
```
Compares sparse+Cholesky (CHOLMOD), sparse+UMFPACK and dense+Cholesky
solvers within the interior-point method for LP problems.
Feasibility is guaranteed: b = A @ x0, x0 >= 0.

## Results
Pre-computed results are available in `results.txt`.
