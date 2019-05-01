# Example 1

Build docker image
```shell
docker build -t example_1 .
```

Start docker container
```shell
docker run -ti --name example-1 -v $(pwd):/home/fenics/shared example_1
```


Run code
```shell
cd /home/fenics/shared
python3 simple_ellipsoid.py
```

Exit container
```shell
exit
```

Restart container
```shell
docker start example-1
```

Execute shell in container and start working
```shell
docker exec -ti -u fenics example-1 /bin/bash -l
```
