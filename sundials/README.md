# SUNDIALS experiments

## Environment
- OS: Debian GNU/Linux (WSL2, x86-64)
- GCC 14.2.0, SUNDIALS 7.6.0, SuiteSparse 7.10.1

## Build
```bash
cd ~/sundials_build
cmake ~/sundials \
  -DENABLE_KLU=ON \
  -DKLU_INCLUDE_DIR=/usr/include/suitesparse \
  -DKLU_LIBRARY_DIR=/usr/lib/x86_64-linux-gnu \
  -DEXAMPLES_ENABLE_C=ON
make -j4
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
./idaRoberts_klu
```
DAE version of Robertson kinetics solved with IDA integrator.

## Results
Pre-computed results are available in `results.txt`.
