from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
n_processes = comm.size
if rank == 0:
    print("Enter number of intervals: ")
    n = int(input())
else:
    n = None
n = comm.bcast(n, root=0)
h = 1.0 / n
sum = 0
for i in range(rank+1, n+1, n_processes):
    x = h * i
    sum += (4 / (1 + x*x))
pi = np.array(h * sum,'d')
result = np.array(0.0,'d')
comm.Reduce(pi, result, op=MPI.SUM, root=0)
if rank == 0:
    print("Pi: {0}".format(result))
