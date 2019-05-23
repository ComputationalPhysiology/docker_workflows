# cbcbeat from branch voltage_bcs
This example uses a branch of cbcbeat that supports extracellular
voltage boundary conditions. This is a development version that
is slower and not as well tested as the main branch of cbcbeat. 


## Build docker image
```shell
docker build -t example_4 .
```

## Start docker container
```shell
docker run -ti --name example-4 -e "TERM=xterm-256color" -w /home/fenics/shared -v $(pwd):/home/fenics/shared example_4
```

## Run a simple demo
```
cd ../cbcbeat/demo/monodomain
python3 demo_monodomain.py
```

## Exit container
```
exit
```

## Restart container
```
docker start example-4
```

## Execute shell in container and start working
```
docker exec -ti -u fenics example-4 /bin/bash -l
```
