# Docker workflows

In this repository we will explain how you can create a development
workflow using docker. This is motivated by the fact that developing
code that is based on [FEniCS](https://fenicsproject.org) can be
challenging. Since many libraries and third-party package depends on
specific versions of FEniCS there is a need for good and efficient
workflows that circumvent these issues.

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
`docker run` command. Note that you can edit the files on your computer
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

### Example 1 Notebook
In this example we will be running the same code and using allmost the
same commands as in Example 1. The only difference is that we will be
using [Jupyter notebooks](https://jupyter.org) for development. 
If you are interested in more details you can check out the
[docuementation in the FEniCS container
docs](https://fenics.readthedocs.io/projects/containers/en/latest/jupyter.html).

The source files for this example can be found in
[example_1_notebook](example_1_notebook).

#### Step 1 and 2
The FEniCS docker image allready comes with jupyter installed so we
can use the same image as in example 1


#### Step 3

Sice we want to run a notebook inside the container, and be able to
acess it in the browser on our host computer we need to redirect the
port where we run the notebook inside the container to a port that we
can access at our host. The command we will run is as follows:

```
docker run --name example-1-notebook -v $(pwd):/home/fenics/shared -d -p 127.0.0.1:8888:8888 example_1 'jupyter-notebook --ip=0.0.0.0'
```

This will start the container and run the jupter notebook command
directly. Note that you will not be entering a bash shell like you did
in Example 1. You can inspect the log inside the container by typing

```
docker logs example-1-notebook
```
The output on mine is
```
$ docker logs exmample-1-notebook
[I 09:50:21.939 NotebookApp] Writing notebook server cookie secret to /home/fenics/.local/share/jupyter/runtime/notebook_cookie_secret
[I 09:50:22.435 NotebookApp] Serving notebooks from local directory: /home/fenics
[I 09:50:22.435 NotebookApp] 0 active kernels
[I 09:50:22.435 NotebookApp] The Jupyter Notebook is running at:
[I 09:50:22.435 NotebookApp] http://0.0.0.0:8888/?token=9c20697181852bdee7b5da928662e7c87824c4b71f0e0f13
[I 09:50:22.435 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[W 09:50:22.435 NotebookApp] No web browser found: could not locate runnable browser.
[C 09:50:22.436 NotebookApp]
```


#### Step 4

Open you browser and go to http://localhost:8888/.
This will ask you for a token. In the log you will find the token. In
my case this is `9c20697181852bdee7b5da928662e7c87824c4b71f0e0f13`. If
you paste that in and click Log in, then that should redirect you to
the Files in your container. Go to `shared` and open
`simple_ellipsoid.ipynb`.

Note that you can make the notebook go the the `shared` folder
directly by passing the argument `-w /home/fenics/shared` to the
docker run command. 


#### Step 5 and 6
If you are done working you can simply stop the container (`docker
stop example-1-notebook`) and when you
want to start working agains you can just start it again (`docker
start example-1-notebook`). 


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


### Example 3

In this example we will be using
[CBCBeat](https://bitbucket.org/meg/cbcbeat). Source code for this
will come later.


## Troubleshooting

### Container is allready in use

If get an error similar to this one
```shell
docker: Error response from daemon: Conflict. The container name "/example-1" is already in use by container "be0a9e4afb6330183bdc352778c330f39cc397893dc2074acb2c14a15d306003". You have to remove (or rename) that container to be able to reuse that name.
```
then you are likely trying to start a container that is allready
running. To fix this you can simply stop the container. In my case
this means to run the command

```
docker stop example-1
```



## Resources

First of all, the best way to improve your workflow is to trry out
different things and reading the [official docker
documentation](https://docs.docker.com).
Also for each docker command you can list all the availbe options by
passing the `--help` flag, i.e `docker run --help`.

The FEniCS community has alse made a very nice resource on how to use
docker as a part of your
[workflow](https://fenics.readthedocs.io/projects/containers/en/latest/work_flows.html).


## License
MIT
