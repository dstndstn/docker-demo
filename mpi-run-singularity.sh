#! /bin/bash
module load singularity
module load mpich
singularity run myproject.sif python3 /myproject/sampler.py --mpi
