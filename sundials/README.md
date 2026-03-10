# SUNDIALS experiments

## Environment
- OS: Debian GNU/Linux (WSL2, x86-64)
- GCC 14.2.0, SUNDIALS 7.6.0, SuiteSparse 7.10.1

## Installation

```bash
wget ://github.com/LLNL/sundials/releases/download/v7.6.0/sundials-7.6.0.tar.gz
tar -xzf sundials-7.6.0.tar.gz
mv sundials-7.6.0 sundials 
```

## Build
```bash
mkdir ~/sundials_build && cd ~/sundials_build
cmake ~/sundials \
    -DCMAKE_BUILD_TYPE=Release \
    -DENABLE_KLU=ON \
    -DKLU_INCLUDE_DIR=/usr/include/suitesparse \
    -DKLU_LIBRARY_DIR=/usr/lib/x86_64-linux-gnu \
    -DBUILD_EXAMPLES=ON
make -j$(nproc)
```

## Experiments

### Scenario 1 & 2: Robertson kinetics — scalability (CVODE + KLU)
```bash
cd ~/sundials_build/examples/cvode/serial

for N in 1 10 100 500 1000 5000; do
    echo -n "N_g=$N: "
    time ./cvRoberts_block_klu $N
done
```
Block-diagonal ODE system (Robertson kinetics), BDF method,
rtol=1e-4, interval [0, 4e10]. Matrix size: 3*N x 3*N, nnz: 9*N.

### Scenario 3: DAE problem (IDA + KLU)
```bash
cd ~/sundials_build/examples/ida/serial
echo -n "idaRoberts: "
time ./idaRoberts_klu 2>&1 | tail -10
```
DAE version of Robertson kinetics solved with IDA integrator.

## Results
Pre-computed results are available in `results.txt`.
