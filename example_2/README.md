# Example 1

Build docker image
```shell
docker build -t example_2 .
```

Start docker container
```shell
docker run -ti --name example-2 -v $(pwd):/home/fenics/shared example_2
```


Run code
```shell
cd /home/fenics/shared
python3 demo.py
```

Exit container
```
exit
```

Restart container
```
docker start example-2
```

Execute shell in container and start working
```
docker exec -ti -u fenics example-2 /bin/bash -l
```
