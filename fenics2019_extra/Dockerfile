

FROM finsberg/fenics:latest

RUN python3 -m pip install --upgrade pip --no-cache-dir \
    && python3 -m pip install black \
    bump2version \
    coverage \
    flake8 \
    ipython \
    ipywidgets \
    isort  \
    myst-nb \
    myst-parser \
    mypy \
    nbsphinx \
    pandoc \
    pre-commit \
    pytest \
    pytest-cov \
    pytest-sugar \
    Sphinx \
    tox \
    wheel \
    jupytext \
    jupyter-book \
    daiquiri \
    scipy \
    gmsh \
    meshio \
    matplotlib \
    fenics_plotly --no-cache-dir 


RUN git clone https://bitbucket.org/fenics-project/mshr.git  \
    && cd mshr \
    && git checkout 2019.1.0 \
    && cmake -DCMAKE_INSTALL_PREFIX=/venv -DCMAKE_PREFIX_PATH=/venv -DCMAKE_BUILD_TYPE=Release -B build -S . \
    && cmake --build build -j6 \
    && cmake --install build \
    && cd python \
    && python -m pip install .  --no-cache-dir \
    && rm -rf build
