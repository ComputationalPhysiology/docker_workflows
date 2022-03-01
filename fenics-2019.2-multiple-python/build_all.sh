# Base image
docker build -t finsberg/dev-base -f Dockerfile-base .
docker push finsberg/dev-base
# Python 3.10
docker build -t finsberg/py310-base -f Dockerfile-base-py310 .
docker push finsberg/py310-base
docker build -t finsberg/fenics-py310 -f Dockerfile-fenics-py310 .
docker push finsberg/fenics-py310
# Python 3.9
docker build -t finsberg/py39-base -f Dockerfile-base-py39 .
docker push finsberg/py39-base
docker build -t finsberg/fenics-py39 -f Dockerfile-fenics-py39 .
docker push finsberg/fenics-py39
# Python 3.8
docker build -t finsberg/py38-base -f Dockerfile-base-py38 .
docker push finsberg/py38-base
docker build -t finsberg/fenics-py38 -f Dockerfile-fenics-py38 .
docker push finsberg/fenics-py38
# Python 3.7
docker build -t finsberg/py37-base -f Dockerfile-base-py37 .
docker push finsberg/py37-base
docker build -t finsberg/fenics-py37 -f Dockerfile-fenics-py37 .
docker push finsberg/fenics-py37