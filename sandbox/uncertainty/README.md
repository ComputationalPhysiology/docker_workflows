# Docker image for UQ analysis and Bayesian inversion

Clone cbcbeat
```
git clone git@github.com:ComputationalPhysiology/uq_mechanics.git
```

Build docker image
```shell
docker build -t uq_mcmc .
```

Start docker container
```shell
docker run -ti --name mcmc -e "TERM=xterm-256color" -w /home/fenics/shared -v $(pwd):/home/fenics/shared uq_mcmc
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
