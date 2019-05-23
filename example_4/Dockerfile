FROM quay.io/dolfinadjoint/dolfin-adjoint:dolfin-adjoint-2017.2.0

ENV FENICS_PYTHON_MAJOR_VERSION=3
ENV FENICS_PREFIX=/home/fenics/local

RUN /bin/bash -c "source /home/fenics/fenics.env.conf && source /home/fenics/dolfin-adjoint.conf && update_dolfin-adjoint && update_libadjoint"

RUN apt-get update && apt-get install -y -q mercurial

RUN hg clone https://bitbucket.org/meg/cbcbeat cbcbeat && cd cbcbeat && hg pull && hg update voltage_bcs  && pip3 install .


