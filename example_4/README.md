# Example 4 - cbcbeat from branch fix_markerwise

Build docker image
```shell
docker build -t example_4 .
```

Start docker container
```shell
docker run -ti --name example-4 -e "TERM=xterm-256color" -w /home/fenics/shared -v $(pwd):/home/fenics/shared example_4
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
docker start example-4
```

Execute shell in container and start working
```
docker exec -ti -u fenics example-4 /bin/bash -l
```
