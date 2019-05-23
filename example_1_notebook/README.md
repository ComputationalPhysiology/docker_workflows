# Jupyter notebook, FEniCS 2017.2, pulse
This is a Jupyter notebook version of Example 1. A docker image is 
created with FEniCS 2017.2 and pulse, and then a jupyter notebook
server is run inside the docker container and accessed from the host. 


## Build docker image
```shell
docker build -t example_1 .
```

## Start docker container
```shell
docker run --name example-1-notebook -v $(pwd):/home/fenics/shared -d -p 127.0.0.1:8888:8888 example_1 'jupyter-notebook --ip=0.0.0.0'
```


## Go to http://localhost:8888/, and get token from log
```shell
docker logs example-1-notebook
```

## Stop container
```shell
docker stop example-1-notebook
```

## Restart container
```shell
docker start example-1-notebook
```
