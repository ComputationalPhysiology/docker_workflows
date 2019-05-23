# FEniCS 2017.2 with dolfin-adjoint and pulse-adjoint
This example installs dolfin-adjoint and the pulse-adjoint code for parameter
estimatation and patient specific heart mechanics modeling. 


## Build docker image
```shell
docker build -t example_2 .
```

## Start docker container
```shell
docker run -ti --name example-2 -v $(pwd):/home/fenics/shared example_2
```


## Run code
```shell
cd /home/fenics/shared
python3 demo.py
```

## Exit container
```
exit
```

## Restart container
```
docker start example-2
```

## Execute shell in container and start working
```
docker exec -ti -u fenics example-2 /bin/bash -l
```
