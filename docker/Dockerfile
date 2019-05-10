FROM ubuntu:18.04
RUN apt -y update && apt install -y --no-install-recommends \
        python3 python3-pip python3-setuptools python3-wheel git
RUN pip3 install numpy==1.15 emcee
RUN mkdir /myproject
WORKDIR /myproject
RUN git clone https://github.com/dstndstn/docker-demo.git
COPY my-data-file.txt /myproject
CMD ["python3", "docker-demo/amazing.py", "my-data-file.txt"]
