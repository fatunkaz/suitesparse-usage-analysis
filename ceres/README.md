# Ceres Solver experiments

## Environment
- OS: Debian GNU/Linux (WSL2, x86-64)
- GCC 14.2.0, Ceres Solver 2.3.0, SuiteSparse 7.10.1, Eigen 3.4.0

## Installation 

```bash
sudo apt-get install -y libeigen3-dev
sudo apt-get install -y libgoogle-glog-dev
sudo apt-get install -y libflags-dev
sudo apt-get install -y libabsl-dev
git clone https://github.com/ceres-solver/ceres-solver.git
```

## Build
```bash
mkdir ~/ceres_build && cd ~/ceres_build
cmake ~/ceres-solver \
    -DCMAKE_BUILD_TYPE=Release \
    -DSUITESPARSE=ON \
    -DBUILD_EXAMPLES=ON \
    -DBUILD_TESTING=OFF
make -j$(nproc)
```

## Dataset
BAL (Bundle Adjustment in the Large) — ladybug scene:
- File: data/problem-49-7776-pre.txt
- Cameras: 49, 3D points: 7776, observations: 31843, parameters: 23769

## Experiments

### SPARSE_NORMAL_CHOLESKY vs SPARSE_SCHUR (AMD ordering, 20 iterations)
```bash
cd ~/ceres_build/bin

# SPARSE_NORMAL_CHOLESKY + AMD
./bundle_adjuster \
  --input ~/suitesparse-usage-analysis/ceres/data/problem-49-7776-pre.txt \
  --linear_solver sparse_normal_cholesky \
  --ordering_type amd \
  --num_iterations 20

# SPARSE_SCHUR + AMD
./bundle_adjuster \
  --input ~/suitesparse-usage-analysis/ceres/data/problem-49-7776-pre.txt \
  --linear_solver sparse_schur \
  --ordering_type amd \
  --num_iterations 20
```

## Results
Pre-computed results are available in `results.txt`.
