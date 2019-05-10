#! /bin/bash

# An example Slurm batch file that uses Singularity with MPI.

#SBATCH -p debugq
#SBATCH -t 5:00
#SBATCH -N 2

echo "mpi-batch.sh running on $(hostname)"

# We use MPICH to match what is in the container.
module load mpich

# Because we need the environment set up by the "module load", we have to use
# another little script, mpi-run-singularity.sh .  We'll run 40 cores x 2 nodes =
# 80 copies.
mpirun -n 80 ./mpi-run-singularity.sh

echo "All done!"
