#! /bin/bash
module load singularity
module load mpich
singularity run myproject-mpi.sif python3 /myproject/sampler.py --mpi
