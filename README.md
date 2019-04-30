# Docker workflows

In this repository we will explain how you can develop your code using
docker as an isolated environment. The motivation behind this is due
to difficulties to develop code based on
[FEniCS](https://fenicsproject.org), which has good support in docker
but which is non-trivial to install on you local machine. Since many
libraries and third-party package depends on specific versions of
python there is a need for good and efficient workflows that
circumvent these issues.

## Prerequisites

You need [docker](https://docs.docker.com).

## Workflows

In the following we will give two examples of possible workflows


### Example 1

In this example we will be using FEniCS version 2017.2 together with
[pulse](https://github.com/ComputationalPhysiology/pulse) which is a
package for solving problems in cardiac mechanics. You will find all
the relevant source files in the folder called [example_1](example_1).

We want to use this
to develop a solver to simulate passive inflation and active
contraction of an idealized ventricle. For simplicity, our goal is to
run demo in the pulse repository called [simple
ellipsoid](https://computationalphysiology.github.io/pulse/html/demos/simple_ellipsoid.html).


#### Step 1: Creating the Dockerfile
A Dockerfile is file that contains all the instructions for building a
docker image. There is a lot to say about this file, so the interested
reader can read more about it in the [official
documentation](https://docs.docker.com/engine/reference/builder/).
Our Dockerfile is show below

```Dockerfile
# example_1/Dockerfile
FROM quay.io/fenicsproject/stable:2017.2.0

RUN git clone https://github.com/finsberg/pulse.git pulse && \
    cd pulse && \
    pip3 install -r requirements.txt && \
    pip3 install .
```

There are basically two instructions. The first one specifies that we
want to use fenics version 2017.2.0, and the seconds one clones the
pulse repository and installs it and its dependencies using pip.


#### Step 2: Building the image

Now that we have the Dockerfile we can build a new image that we will
call `example_1`. 

```shell
docker build -t example_1 .
```

This will take a while the first time because you need to download the
fenics image. Once it is done you can list the available images by
typing 

```
$ docker images
docker images
REPOSITORY                     TAG                 IMAGE ID            CREATED             SIZE
example_1                      latest              a16f0d62da1f        9 minutes ago       2.5GB
```

#### Step 3: Spinning up a container

Next we need to create a container, which is a running instance of an
image. We also want to be able to share a folder on our computer with
the container, so that it is easy to share files between the container
and you machine. To start the container do

```shell
docker run -ti --name example-1 -v $(pwd):/home/fenics/shared example_1
```

Here we have given a name `example-1` to the container and we have
mounted the current working directory `pwd` into the path
`/home/fenics/shared` inside the container. 

When you enter the container, and go to `/home/fenics/shared` you will
find the files in the same directory as you where in when you ran the
`docker run` command. Note that you can edit the files on you computer
as you would have if you where working in the same directory.

#### Step 4: Do some work

Try to run the demo in `/home/fenics/shared/`.

```shell
cd /home/fenics/shared
python3 simple_ellipsoid.py
```

When it is done you will see a figure called `simple_ellipsoid.png`
appear in the folder


#### Step 5: Done for the day

When you are done working you can type

```
exit
```

inside the container. This will bring you back to your local machine.
You can now see that you have a container that has been exited by
typing `docker ps -a`

```
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                     PORTS               NAMES
be0a9e4afb63        example_1           "/sbin/my_init --qui…"   10 minutes ago      Exited (0) 8 minutes ago                       example-1
```


#### Step 6: Back to work

When you are ready to work inside the container again, you need to
start it

```
docker start example-1
```

and the you need to execute a new process so that we can enter the
container again. We will start a `bash` shell and we will there run
the following command

```
docker exec -ti -u fenics example-1 /bin/bash -l
```
The `-l` is needed because we want this process to act as a login
shell. We also want to use the `user` fenics and therefore provide the
`-u fenics` argument. If `user` is not provided you will be logged in
as root which is generally not good practice.

Now go back to Step 4 and repeat.


#### Step 7: Clean up

You will notice that these images and container takes up a lot of
space so it is generally a good idea to delete images and containers
that are not used any more.

To delete a container do 
```
docker rm CONTAINER_ID
```
where `CONTAINER_ID` can be found in the first column when you type
`docker -ps -a`. If you want to delete all container you can do 

```
docker rm $(docker ps -aq)
```

To delete an image you do
```
docker rmi IMAGE_ID
```
where `CONTAINER_ID` can be found in the first column when you type
`docker images -a`. If you want to delete all container you can do 

```
docker rmi $(docker images -aq)
```


### Example 2

In this example will install and run an example using
[`pulse-adjoint`](https://github.com/ComputationalPhysiology/pulse_adjoint)
which is a framework for doing data assimilation of cardiac mechanics
and is based on pulse from Example 1. Check out the code in
[example_2](example_2) and follow the same steps as in Example 1.
Note that in this example we will be using a base image with
[dolfin-adjoint](http://www.dolfin-adjoint.org/en/latest/). Furthermore,
since python2 is default we need to also update dolfin-adjoint so that
we use python3 instead.


#### Example 3

In this example we will be using
[CBCBeat](https://bitbucket.org/meg/cbcbeat). Source code for this
will come later.


## Resources

The FEniCS community has made a very nice resource on how to use
docker as a part of your workflow, and this repository is based on the
article about [suggested
workflows](https://fenics.readthedocs.io/projects/containers/en/latest/work_flows.html).


## License
MIT
