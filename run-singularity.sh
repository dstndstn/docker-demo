#! /bin/bash

module load singularity
module load mpich
singularity run myproject.sif python3 /demo/sampler.py --mpi
