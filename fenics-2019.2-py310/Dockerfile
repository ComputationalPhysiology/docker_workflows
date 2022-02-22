FROM python:3.10-slim-bullseye

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    bison \
    ccache \
    cmake \
    curl \
    doxygen \
    flex \
    g++ \
    gfortran \
    git \
    graphviz \
    libboost-filesystem-dev \
    libboost-iostreams-dev \
    libboost-math-dev \
    libboost-program-options-dev \
    libboost-system-dev \
    libboost-thread-dev \
    libboost-timer-dev \
    libeigen3-dev \
    libfreetype6-dev \
    liblapack-dev \
    libmpich-dev \
    libopenblas-dev \
    libpcre3-dev \
    libpng-dev \
    libhdf5-mpich-dev \
    libgmp-dev \
    libcln-dev \
    libmpfr-dev \
    man \
    mpich \
    nano \
    pkg-config \
    wget \
    bash-completion \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set up a virtual environment
ENV PATH=/venv/bin:$PATH
RUN python -m venv /venv

# Install petsc
RUN git clone -b release https://gitlab.com/petsc/petsc petsc \
    && cd petsc \
    && ./configure --COPTFLAGS="-O2" \
        --CXXOPTFLAGS="-O2" \
        --FOPTFLAGS="-O2" \
        --with-fortran-bindings=no \
        --with-debugging=0 \
        --download-blacs \
        --download-hypre \
        --download-metis \
        --download-mumps \
        --download-ptscotch \
        --download-scalapack \
        --download-spai \
        --download-suitesparse \
        --download-superlu \
        --prefix=/venv/petsc \
    && make \
    && make install \
    && rm -rf /tmp/* \
    && rm -rf /petsc

ENV PETSC_DIR=/venv/petsc

# Install slepsc
RUN git clone -b release https://gitlab.com/slepc/slepc slepc \
    && cd slepc \
    && ./configure --prefix=/venv/slepc \
    && make SLEPC_DIR=$(pwd) \
    && make install SLEPC_DIR=$(pwd) \
    && rm -rf /tmp/* \
    && rm -rf /slepc

ENV SLEPC_DIR=/venv/slepc

# Install FFC
RUN python -m pip install dev-fenics-ffc mpi4py petsc4py pybind11 cmake wheel --no-cache-dir

# Install dolfin
RUN git clone https://finsberg@bitbucket.org/finsberg/dolfin.git dolfin \
    && cd dolfin \
    && git checkout finsberg/fix-hdf5-boost-deprecation-errors \
    && cmake -DCMAKE_INSTALL_PREFIX=/venv -DCMAKE_PREFIX_PATH=/venv -DCMAKE_BUILD_TYPE=Release -B build -S . \
    && cmake --build build -j6 \
    && cmake --install build

# This is basically what is in the /venv/share/dolfin/dolfin.conf
ENV LD_LIBRARY_PATH=/venv/lib:$LD_LIBRARY_PATH
ENV PATH=/venv/bin:$PATH
ENV PKG_CONFIG_PATH=/venv/lib/pkgconfig:$PKG_CONFIG_PATH
ENV MANPATH=/venv/share/man:$MANPATH

# Install the python API
RUN cd dolfin/python \
    && python -m pip install . --no-cache-dir \
    && rm -rf /dolfin



CMD ["bash"]