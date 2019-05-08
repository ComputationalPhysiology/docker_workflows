FROM finsberg/fenics2017

# tzdata workaround
ENV TZ=Europe
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install some ubuntu packages
RUN sudo apt-get update && DEBIAN_FRONTEND=noninteractive &&\
    sudo apt-get -y install git mayavi2 && \
    rm -rf /var/lib/apt/lists/*

# Install gmsh from source 
RUN wget http://gmsh.info/src/gmsh-3.0.0-source.tgz && \
    tar -xvf gmsh-3.0.0-source.tgz && cd gmsh-3.0.0-source && \
    mkdir -p build && cd build && \
    sudo cmake -DENABLE_BUILD_SHARED=True -DENABLE_BUILD_LIB=True -DENABLE_MPI=True .. && \
    sudo make -j 4 && sudo make install

RUN sudo pip3 install numpy vtk scipy
RUN sudo pip3 install --no-binary=h5py h5py mayavi
RUN sudo pip3 install git+https://bitbucket.org/peppu/fenicshotools.git
RUN git clone https://github.com/ComputationalPhysiology/ldrb.git && cd ldrb && \
    pip3 install -r requirements.txt && pip3 install . 
RUN git clone https://github.com/ComputationalPhysiology/pulse.git && cd pulse && \
    pip3 install -r requirements.txt && pip3 install . 
