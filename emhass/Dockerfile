## EMHASS-Add-On Docker
#build_version options are: addon (default), addon-git
ARG build_version=addon
#see build.yaml for all docker images according to host architecture
ARG BUILD_FROM

FROM ${BUILD_FROM} AS base

#check if BUILD_ARCH passed by build-arg
ARG BUILD_ARCH
ENV BUILD_ARCH=${BUILD_ARCH}

WORKDIR /app
COPY requirements.txt /app/

#apt package install
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libffi-dev \
    python3 \
    python3-pip \
    python3-dev \
    git \
    gcc \
    patchelf \
    cmake \
    meson \
    ninja-build \
    build-essential \
    libhdf5-dev \
    libhdf5-serial-dev \
    pkg-config \
    gfortran \
    netcdf-bin \
    libnetcdf-dev \
    coinor-cbc \
    coinor-libcbc-dev \
    libglpk-dev \
    glpk-utils \
    libatlas-base-dev \
    libopenblas-dev
#specify hdf5
RUN ln -s /usr/include/hdf5/serial /usr/include/hdf5/include && export HDF5_DIR=/usr/include/hdf5

#install packages from pip, use piwheels if arm 32bit
RUN [[ "${BUILD_ARCH}" == "armhf" || "${BUILD_ARCH}" == "armv7" ]] &&  pip3 install --index-url=https://www.piwheels.org/simple --no-cache-dir --break-system-packages -r requirements.txt ||  pip3 install --no-cache-dir --break-system-packages -r requirements.txt

#try, symlink apt cbc, to pulp cbc, in python directory (for 32bit)
RUN [[ "${BUILD_ARCH}" == "armhf" || "${BUILD_ARCH}" == "armv7"  ]] &&  ln -sf /usr/bin/cbc /usr/local/lib/python3.11/dist-packages/pulp/solverdir/cbc/linux/32/cbc || echo "cbc symlink didnt work/not required"

#if armv7, try install libatomic1 to fix scipy issue
RUN [[ "${BUILD_ARCH}" == "armv7" ]] && apt-get update && apt-get install libatomic1 || echo "libatomic1 cant be installed"

#remove build only packages
RUN apt-get purge -y --auto-remove \
    gcc \
    patchelf \
    cmake \
    meson \
    ninja-build \
    build-essential \
    pkg-config \
    gfortran \
    netcdf-bin \
    libnetcdf-dev \
    && rm -rf /var/lib/apt/lists/*

#copy config file (on all builds)
COPY config_emhass.yaml /app/

#-------------------------
#EMHASS-Add-on Default
FROM base as addon

LABEL \
    io.hass.name="emhass" \
    io.hass.description="EMHASS: Energy Management for Home Assistant" \
    io.hass.version=${BUILD_VERSION} \
    io.hass.type="addon" \
    io.hass.arch="aarch64|amd64|armhf|armv7"

ENTRYPOINT python3 -m emhass.web_server --addon True --url http://supervisor/core/api --key $SUPERVISOR_TOKEN

#-----------
#EMHASS-Add-on testing with git
FROM addon as addon-git
ARG build_repo=https://github.com/davidusb-geek/emhass.git
ARG build_branch=master
WORKDIR /tmp/
#Repo
RUN git clone $build_repo
WORKDIR /tmp/emhass
#Branch
RUN git checkout $build_branch
RUN mkdir -p /app/src/emhass/data/
#RUN mkdir -p /app/data/ #if config.yaml DATA_PATH=/app/data/
RUN cp -r /tmp/emhass/src/emhass/. /app/src/emhass/
RUN cp /tmp/emhass/src/emhass/data/*  /app/src/emhass/data/
#RUN cp /tmp/emhass/data/opt_res_latest.csv  /app/data/ #if config.yaml DATA_PATH=/app/data/
RUN cp /tmp/emhass/setup.py /app/
RUN cp /tmp/emhass/README.md /app/
WORKDIR /app
RUN pip3 install --no-cache-dir --break-system-packages --no-deps --force-reinstall  .
ENTRYPOINT python3 -m emhass.web_server --addon True --url http://supervisor/core/api --key $SUPERVISOR_TOKEN

#check build arguments and build
FROM ${build_version} AS final
