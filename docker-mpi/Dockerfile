# This is an example Dockerfile that uses MPI to parallelize across
# multiple cores on multiple nodes.

FROM ubuntu:18.04

RUN apt -y update && apt install -y apt-utils && \
    DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends \
        python3 python3-pip python3-setuptools python3-wheel git

RUN pip3 install numpy==1.15 emcee matplotlib

# We need to match MPI versions inside the container and on Symmetry.
# Symmetry runs an older Ubuntu version (16.04), so I couldn't find an OpenMPI
# version that matched (1.10.7 on Symmetry vs 2.1.1 in Ubuntu 18.04), so I tried
# MPICH and it seems to work.

RUN apt install -y mpich libmpich-dev gcc libc-dev python3-dev rsh-client
RUN pip3 install mpi4py

# Can also use the Ubuntu-supplied mpi4py library...
#RUN apt install -y python3-mpi4py openmpi-bin rsh-client

RUN mkdir /myproject
WORKDIR /myproject

# If you're doing a big production run or generating results for a paper,
# you probably want to use a tagged version of your code:
#RUN git clone --branch v1.7 https://github.com/dstndstn/demo.git .

RUN git clone https://github.com/dstndstn/docker-demo.git . && echo 2

#CMD ["python3", "/demo/sampler.py"]
