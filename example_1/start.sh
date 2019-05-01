#/bin/bash
NAME="example-1"
IMAGE="example_1"
if [ ! "$(docker ps -q -f name=${NAME})" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=${NAME})" ]; then
        # cleanup
        docker start ${NAME}
	docker exec -ti -u fenics ${NAME} /bin/bash -l
    fi
    # run your container
    docker run -ti --name ${NAME} -w /home/fenics/shared -v $(pwd):/home/fenics/shared ${IMAGE}
fi
