# Docker image for developing cbcbeat

This workflow is useful if you want to change the cbcbeat code itself. The example illustrates 
how you can clone cbcbeat on your host system, share it into the docker image, and install it
there. In this way you can edit cbcbeat files on your host, and then simply reinstall 
inside the docker image to see the changes in effect. 

## Clone cbcbeat
```
hg clone ssh://hg@bitbucket.org/meg/cbcbeat
cd cbcbeat && hg pull && hg update stable-2017.2.0
cd ..
```

## Build docker image
```shell
docker build -t cbcbeat_dev .
```

## Start docker container
```shell
docker run -ti --name beat_dev -e "TERM=xterm-256color" -w /home/fenics/shared -v $(pwd):/home/fenics/shared beat_dev
```

## Run a simple demo
```
cd ../cbcbeat/demo/monodomain
python3 demo_monodomain.py
```

Exit container
```
exit
```

Restart container
```
docker start beat_dev
```

Execute shell in container and start working
```
docker exec -ti -u fenics beat_dev /bin/bash -l
```
