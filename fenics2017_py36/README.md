# FEniCS 2017.2 version with python 3.6

The available docker image for fenics version 2017.2 uses python 3.5
or 2.7, but we want to also have support for the python version 3.6.
For example in python 3.6 there is support for
[f-strings](https://realpython.com/python-f-strings/) which is
definitly a feature that worth upgrading for. 

The fenics developers made a
[repo](https://bitbucket.org/fenics-project/docker/src/master/)
containing the available Dockerfiles but they did not tag the
different versions, which makes it a bit difficult to go back to a
previous image and upgrade certain things (like the version of
python). As a consequence, we will create a standalone Dockerfile
here, that rebuilds FEniCS version 2017.2 using the latest version of
everything (including python, which at the time of writing is at
version 3.6.7.

Note that the Dockerfile (ane the other files) are based on the commit
with SHA 2b39cf3. Also note that for this image there is python3 only.
