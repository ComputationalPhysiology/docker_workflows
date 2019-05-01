FROM quay.io/dolfinadjoint/dolfin-adjoint:dolfin-adjoint-2017.2.0


ENV FENICS_PYTHON_MAJOR_VERSION=3
ENV FENICS_PREFIX=/home/fenics/local

RUN /bin/bash -c "source /home/fenics/fenics.env.conf && source /home/fenics/dolfin-adjoint.conf && update_dolfin-adjoint && update_libadjoint"

RUN pip3 install gotran https://bitbucket.org/finsberg/cbcbeat/get/default.tar.gz --upgrade
