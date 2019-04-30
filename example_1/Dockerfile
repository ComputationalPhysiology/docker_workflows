FROM quay.io/fenicsproject/stable:2017.2.0

RUN git clone https://github.com/ComputationalPhysiology/pulse.git pulse && \
    cd pulse && \
    pip3 install -r requirements.txt && \
    pip3 install .
