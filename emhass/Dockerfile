## EMHASS-Add-On Docker

#build_version options are: addon (default), addon-git
ARG build_version=addon
ARG BUILD_ARCH


FROM ghcr.io/home-assistant/$BUILD_ARCH-base-debian:bookworm AS base

WORKDIR /app
COPY requirements.txt /app/

# Setup
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libffi-dev \
    python3 \
    python3-pip \
    python3-dev \
    git \
    build-essential \
    gcc \
    coinor-cbc \
    coinor-libcbc-dev \
    libglpk-dev \
    glpk-utils \
    libhdf5-dev \
    libhdf5-serial-dev \
    netcdf-bin \
    libnetcdf-dev \
    pkg-config \
    gfortran \
    libatlas-base-dev \
    && ln -s /usr/include/hdf5/serial /usr/include/hdf5/include \
    && export HDF5_DIR=/usr/include/hdf5 \
    && pip3 install --extra-index-url=https://www.piwheels.org/simple --no-cache-dir --break-system-packages -U setuptools wheel \
    && pip3 install --extra-index-url=https://www.piwheels.org/simple --no-cache-dir --break-system-packages -r requirements.txt \
    && apt-get purge -y --auto-remove \
    gcc \
    build-essential \
    libhdf5-dev \
    libhdf5-serial-dev \
    pkg-config \
    gfortran \
    && rm -rf /var/lib/apt/lists/*


#copy config file (on all builds)
COPY config_emhass.yaml /app/

#-------------------------
#EMHASS-ADDON Default
FROM base as addon

LABEL \
    io.hass.name="emhass" \
    io.hass.description="EMHASS: Energy Management for Home Assistant" \
    io.hass.version=${BUILD_VERSION} \
    io.hass.type="addon" \
    io.hass.arch="aarch64|amd64|armhf|armv7"

ENTRYPOINT python3 -m emhass.web_server --addon True --url http://supervisor/core/api --key $SUPERVISOR_TOKEN

#-----------
#EMHASS-ADD-ON testing with git
FROM addon as addon-git
ARG build_repo=https://github.com/davidusb-geek/emhass.git
ARG build_branch=master
WORKDIR /tmp/
#Repo
RUN git clone $build_repo
WORKDIR /tmp/emhass
#Branch
RUN git checkout $build_branch
RUN mkdir -p /app/src/emhass/
#RUN mkdir -p /app/data/ #if config.yaml DATA_PATH=/app/data/
RUN cp -r /tmp/emhass/src/emhass/. /app/src/emhass/
#RUN cp /tmp/emhass/data/opt_res_latest.csv  /app/data/ #if config.yaml DATA_PATH=/app/data/
RUN cp /tmp/emhass/setup.py /app/
RUN cp /tmp/emhass/README.md /app/
WORKDIR /app
RUN python3 -m pip install --no-cache-dir --break-system-packages -U  .
ENTRYPOINT python3 -m emhass.web_server --addon True --url http://supervisor/core/api --key $SUPERVISOR_TOKEN

#check build arguments and build
FROM ${build_version} AS final