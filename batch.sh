#! /bin/bash

# An example Slurm batch file

#SBATCH -p debugq
#SBATCH -t 5:00
#SBATCH -N 2

echo "batch.sh running on $(hostname)"

module load mpich

# Because we need the environment set up by the "module load", we can't do this
# as a one-liner.  Instead, we need to use another script, run-singularity.sh
#module load singularity
#mpirun -n 20 singularity run myproject.sif python3 /demo/sampler.py --mpi

mpirun -n 80 ./run-singularity.sh

echo "All done!"
