# FEniCS 2017.2 with pulse heart mechanics
This example installs FEniCS 2017.2 and the pulse heart mechanics solver. 
It is the recommended way to install pulse if you only want to use
it in your own code, and don't need to edit the pulse code itself. The steps 
below illustrate how to first build the docker image, start using
it and create a *container*, and then stopping and restarting the container.

## Build docker image
```shell
docker build -t example_1 .
```

## Start docker container
```shell
docker run -ti --name example-1 -v $(pwd):/home/fenics/shared example_1
```


## Run code
```shell
cd /home/fenics/shared
python3 simple_ellipsoid.py
```

## Exit container
```shell
exit
```

## Restart container
```shell
docker start example-1
```

## Execute shell in container and start working
```shell
docker exec -ti -u fenics example-1 /bin/bash -l
```
