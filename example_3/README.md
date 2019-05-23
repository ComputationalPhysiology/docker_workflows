# FENiCS 2017.2 with dolfin-adjoint and cbcbeat
This example is a good choice if do not want to change or develop cbcbeat, but
simply want to use it in your own code. It may be useful to clone the 
cbcbeat separately on the host system to use as a reference and to use
the demo scripts as starting points for your own work. 

## Build docker image
```shell
docker build -t example_3 .
```

## Start docker container
```shell
docker run -ti --name example-3 -e "TERM=xterm-256color" -w /home/fenics/shared -v $(pwd):/home/fenics/shared example_3
```

## Get cell model
```shell
wget https://models.physiomeproject.org/workspace/tentusscher_noble_noble_panfilov_2004/@@rawfile/941ec8e54e46e6fe82765c17f1d47582169baac2/tentusscher_noble_noble_panfilov_2004_a.cellml
```

## Codegeneration
```shell
cellml2gotran tentusscher_noble_noble_panfilov_2004_a.cellml
gotran2py  tentusscher_2004_mcell.ode --output cell_model_python
gotran2beat  tentusscher_2004_mcell.ode --output cell_model_cbcbeat
```

## Exit container
```
exit
```

## Restart container
```
docker start example-3
```

Execute shell in container and start working
```
docker exec -ti -u fenics example-3 /bin/bash -l
```

Start notebook container
```shell
docker run --name example-3-notebook -w /home/fenics/shared -v $(pwd):/home/fenics/shared -d -p 127.0.0.1:8888:8888 example_3 'jupyter-notebook --ip=0.0.0.0'
```
