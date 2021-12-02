# syntax=docker/dockerfile:1
FROM dispel4py/docker.openmpi

COPY script.py script.py
COPY collect_hosts collect_hosts
COPY run_mpi run_mpi
RUN chmod +x run_mpi
RUN chmod +x collect_hosts
RUN pip install numpy