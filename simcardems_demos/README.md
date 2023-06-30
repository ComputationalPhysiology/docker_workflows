# Running Simcardems demos using docker

## Install docker

Install the community edition (CE).

* [Windows](https://docs.docker.com/docker-for-windows/install/)

* [Mac](https://docs.docker.com/docker-for-mac/install/)

* [Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)


## About docker

![Docker architecture (image is taken from http://apachebooster.com/kb/wp-content/uploads/2017/09/docker-architecture.png)](docker-architecture.png)

An image is a frozen snapshot of a virtual machine, while a
container is a running instance of an image.

This means that every container is associated with a single image, and
many container can be associated with the same image. 

In order to run the Simcardems demos we need to (i) install docker, (ii) download the
simcardems image, (iii) start a container based on this image, (iv) make sure
that our working folder is shared between the container and the native system, and (v) run the
relevant python scripts from inside the container. 

Step (iv) is not always strictly needed, but it is very useful for being able to edit the 
demo scripts and to visualize the results. Here are the detailed instructions for each step. 

## Step-by-step recipe

### Download the simcardems image

```
docker pull ghcr.io/computationalphysiology/simcardems:latest
```

Once this is done you can see a list of the available images on your laptop
```
docker images
```
### Create and run a container based on the image

```
docker run --name simcardems -v "$(pwd)":/home/shared -w /home/shared -it ghcr.io/computationalphysiology/simcardems
```

* `-i` : We want to run the container `i`nteractively

* `-v` : We want to share a `v`olume between our computer and a
  running container. Here we share current working directory on our
  laptop (`pwd`), and this is mounted in the path
  `/home/shared` inside the running docker container.
  
* `-w` : We set the `w`orking directory to `/home/shared`.

* `--name`: We give this container a name `simcardems` so
  that it is easy to refer to it later.

If you open a different terminal and type
```
docker ps
```
you will see the container listed there

### Exit the container
To exit the container type `exit` or `Ctrl+D`.
If you type `docker ps` now you will see that the container
disappeared. However if you type `docker ps -a` you will see it
appear again. It is good practice to delete old containers that are
not used anymore. You can delete the container with `docker rm simcardems`. 

It seems that sometimes the command `exit` will make you both exit the container and stop it,
as described above. However, other times it will just exit the container, and it keeps running
in the background. I am not exactly sure why this happens, but it is easy to check by typing
`docker ps`. If the container is listed it means that it is still running, and you can stop it with 
`docker stop simcardems`. 

### Restart container
If you want to restart the container you can type
```
docker start simcardems
```
This will start the container, but you are still outside the container and cannot directly 
run commands inside it. In order to do so, we must use the `docker exec` command, which 
can be used either to run specific commands or simply to open a shell interactively so we
can run commands directly from inside the container:
type 
```
docker exec -ti simcardems bash 
```
The last command just says that we want to run a bash shell inside the container. We can then 
use standard shell commands to navigate and run scripts etc. inside the container, similar
to what we got from the `docker run` command above.

### Running the Simcardems demos
In order to run the demos and visualize the results, it is useful to have two 
separate terminal windows open. One terminal should have the container running interactively 
so we can run commands inside it, and in the other we are "outside" the container, but navigate
to the folder which is shared between the container and the native system. We will refer to these
two windows as inside and outside the container, respectively. It is also useful
to clone the simcardems repo on your native system, to have the demo files available.

In the shared folder, outside the container, first do the following:
```
cp -r path_to_simcardems/simcardems/demos .
```
with `path_to_simcardems` replaced by the path to the folder where you cloned the repo. 
Now, the folder `demos` should contain all the demo scripts, and should be visible both from
outside and inside the container (since we placed it in the shared folder). 

Inside the container, run for instance
```
cd demos
python3 simple_demo.py
```
Although it is a simple demo, it still takes a little while to complete. After it completes you 
should see a new folder named `results_simple_demo`. Since everything was kept inside our shared folder, 
this folder is also accessible both inside and outside the container. From outside the container
you can now browse the result files and visualize them using Paraview or any other tool you prefer.

Since the folder containing both the scripts and the results is shared between the container and the
native system, a natural workflow is to edit the scripts from outside the container (using your favorite editor),
then run them from inside the container, and then go back to the native system to visualize the results. 

## Resources

* https://github.com/ComputationalPhysiology/docker_workflows

* https://fenics.readthedocs.io/projects/containers/en/latest/

* https://docs.docker.com
