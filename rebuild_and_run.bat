CALL docker rmi docker-mpi
CALL docker build --tag docker-mpi .
CALL docker-compose up -d --scale mpi_head=1 --scale  mpi_node=3
CALL ssh -i ssh/id_rsa.mpi -p 60037 tutorial@localhost