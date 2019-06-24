# Docker tutorial

## Install docker

Install the community edition (CE).

* [Windows](https://docs.docker.com/docker-for-windows/install/)

* [Mac](https://docs.docker.com/docker-for-mac/install/)

* [Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)


## About docker

![Docker architecture (image is taken from http://apachebooster.com/kb/wp-content/uploads/2017/09/docker-architecture.png)](docker-architecture.png)

An image is a fronzen snapshot of a virtual mechanics, while a
container is an instance of an image, i.e a container is a running
instance of an image.

This means that every container is associated with a single image, and
many container can be associated with the same image. 

People upload their images to a remote registry where you can download
and run instances of these images, and also create your own images on
top of existing images.


## Working example

### Download latest FEniCS image

```
docker pull quay.io/fenicsproject/stable:latest
```

Once this is done you can see a list of the available images on your laptop
```
docker images
```


### Run an instance of the container

```
docker run -ti --name simula-summer-school -v $(pwd):/home/fenics/shared -w /home/fenics/shared quay.io/fenicsproject/stable:latest
```

* `-i` : We want to run the container `i`nteractively

* `-v` : We want to share a `v`olume between our computer and a
  running container. Here we share current working directory on out
  laptop (`pwd`), and this is mounted in the path
  `/home/fenics/shared`.
  
* `-w` : We set the `w`orking directory to `/home/fenics/shared`.

* `--name`: We give this container a name `simula-summer-school` so
  that it is easy to refer to it later.

If you open a differnt terminal and type
```
docker ps
```
you will see the container listed there

### Exit the container
To exit the container type `exit` or `Ctrl+D`.
If you type `docker ps` now you will see that the container
disappeared. However if you type `docker ps -a` you will see it
appear again. It is good practice to delete old containers that are
not used anymore.

### Restart container
If you want to restart the container you can type
```
docker start simula-summer-school
```
There is an equivalent command for stopping it
```
docker stop simula-summer-school
```
Now if you want to go into the container and continue working you can
type 

```
docker exec -ti -u fenics simula-summer-school /bin/bash -l
```
The last command just says that we want to run a bash login shell,
with user `fenics`

## Creating your own image
If you want to add some additional packages to the image of don't want
to install them every time you launch a new container you can create
your own docker image. To do this you create a new file called a
`Dockerfile`. For example if we want to install a package called
`ldrb` (which is a package for assigning fiber orientations in a heart
model) we can put the following in the `Dockerfile`
```Dockerfile
FROM quay.io/fenicsproject/stable

RUN pip3 install ldrb
```
Now we can build a new image an call it `ldrb`

```
docker build -t ldrb .
```
(note the `.` at the end).

Finally, you can run the container with the same command as before
(but with a different image)


```
docker run -ti --name simula-summer-school-ldrb -v $(pwd):/home/fenics/shared -w /home/fenics/shared ldrb
```



## Resources

* https://github.com/ComputationalPhysiology/docker_workflows

* https://fenics.readthedocs.io/projects/containers/en/latest/

* https://docs.docker.com
