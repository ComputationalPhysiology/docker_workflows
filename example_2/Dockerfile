FROM quay.io/dolfinadjoint/dolfin-adjoint:dolfin-adjoint-2017.2.0


ENV FENICS_PYTHON_MAJOR_VERSION=3
ENV FENICS_PREFIX=/home/fenics/local

RUN /bin/bash -c "source /home/fenics/fenics.env.conf && source /home/fenics/dolfin-adjoint.conf && update_dolfin-adjoint && update_libadjoint"
    

RUN git clone https://github.com/ComputationalPhysiology/pulse.git pulse && \
    cd pulse && \
    pip3 install -r requirements.txt && \
    pip3 install .


RUN git clone https://github.com/ComputationalPhysiology/pulse_adjoint.git pulse_adjoint && \
    cd pulse_adjoint && \
    pip3 install -r requirements.txt && \
    pip3 install .

