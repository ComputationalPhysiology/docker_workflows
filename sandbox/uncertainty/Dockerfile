FROM quay.io/dolfinadjoint/dolfin-adjoint:dolfin-adjoint-2017.2.0

ENV FENICS_PYTHON_MAJOR_VERSION=3
ENV FENICS_PREFIX=/home/fenics/local

RUN /bin/bash -c "source /home/fenics/fenics.env.conf && source /home/fenics/dolfin-adjoint.conf && update_dolfin-adjoint && update_libadjoint"


RUN pip3 install --upgrade pip

RUN apt-get update -y
RUN apt-get install python-vtk6 -y


#RUN python3 -m pip install vtk
#RUN pip3 install h5py
#RUN pip3 install chaospy
#RUN pip3 install scikit-learn


COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

RUN pip3 install -U pytest

RUN cd /usr/local/src \
    && wget https://github.com/pybind/pybind11/archive/v2.2.3.tar.gz \
    && tar xvf v2.2.3.tar.gz \
    && cd pybind11-2.2.3 \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make \
    && make install



COPY ./fiberrules /fiberrules
RUN cd /fiberrules && pip3 install .

#RUN git clone git@bitbucket.org:simula-camo/fiberrules.git fiberrules && \
#    cd fiberrules && git checkout finsberg/pybind11_python3 && \
#    pip3 install .


