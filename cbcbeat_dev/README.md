# Docker image for developing cbcbeat

Clone cbcbeat
```
hg clone ssh://hg@bitbucket.org/meg/cbcbeat
cd cbcbeat && hg pull && hg update stable-2017.2.0
cd ..
```

Build docker image
```shell
docker build -t cbcbeat_dev .
```

Start docker container
```shell
docker run -ti --name beat_dev -e "TERM=xterm-256color" -w /home/fenics/shared -v $(pwd):/home/fenics/shared beat_dev
```

Run a simple demo
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
