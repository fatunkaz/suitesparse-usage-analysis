# SuiteSparse Usage Analysis

[![CI](https://github.com/fatunkaz/suitesparse-usage-analysis/actions/workflows/ci.yml/badge.svg)](https://github.com/fatunkaz/suitesparse-usage-analysis/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Experimental code and data for the internship report
"Identification and Analysis of SuiteSparse Usage Scenarios in Application Packages".

The repository contains three independent experiments demonstrating how
[SuiteSparse](https://github.com/DrTimothyAldenDavis/SuiteSparse) sparse matrix
solvers (KLU, CHOLMOD, UMFPACK, SPQR) are used in real-world scientific packages:
SUNDIALS, Ceres Solver, and SciPy.

**Author:** Pakhomov Georgiy Aleksandrovich  
**University:** Saint Petersburg State University  
**Year:** 2026

## Repository Structure

```
suitesparse-usage-analysis/
├── ceres/               # Ceres Solver experiments (CHOLMOD, SPQR)
│   ├── results.txt      # Pre-computed experiment results
    ├── outputs.txt      # Output of experimental programs
│   └── README.md        # Build instructions and run commands
├── sundials/            # SUNDIALS experiments (KLU)
│   ├── results.txt      # Pre-computed experiment results
    ├── outputs.txt      # Output of experimental programs
│   └── README.md        # Build instructions and run commands
└── scipy/               # SciPy experiments (UMFPACK, CHOLMOD)
    ├── bench_scipy.py   # Scenarios 1 & 2: UMFPACK vs SuperLU
    ├── bench_scipy3.py  # Scenario 3: CHOLMOD vs UMFPACK vs dense
    ├── results.txt      # Pre-computed experiment results
    ├── outputs.txt      # Output of experimental programs
    └── README.md        # Installation and run instructions
```

## Environment

- OS: Debian GNU/Linux (WSL2, x86-64)
- GCC 14.2.0
- SuiteSparse 7.10.1
- SUNDIALS 7.6.0
- Ceres Solver 2.3.0
- SciPy 1.15.3, scikit-umfpack 0.4.2, scikit-sparse 0.5.0

## Required dependencies

To correctly perform these experiments, the following dependencies are required:

```bash
sudo apt-get install -y gcc g++ cmake make wget
sudo apt-get install -y libopenblas-dev
sudo apt-get install -y liblapack-dev
sudo apt-get install -y libsuitesparse-dev
```

## See Also

Each subdirectory contains its own README with detailed build
instructions, dependencies and run commands, as well as a
results.txt file with pre-computed experiment outputs.
