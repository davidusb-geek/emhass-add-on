ARG BUILD_FROM
FROM ${BUILD_FROM}

# switch working directory
WORKDIR /usr/src

# copy the requirements file into the image
COPY ./requirements.txt /usr/src/requirements.txt

# Setup
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libffi-dev \
        python3 \
        python3-pip \
        python3-dev \
        git \
        build-essential \
        coinor-libcbc-dev \
        coinor-cbc \
        libglpk-dev \
        glpk-utils \
        libhdf5-dev \
        libhdf5-serial-dev \
        netcdf-bin \
        libnetcdf-dev \
        pkg-config \
        python3-h5py \
        gfortran \
        libatlas-base-dev \
    && ln -s /usr/include/hdf5/serial /usr/include/hdf5/include \
    && export HDF5_DIR=/usr/include/hdf5 \
    && pip3 install netCDF4==1.5.4 \
    && pip3 install --extra-index-url=https://www.piwheels.org/simple --no-cache-dir -U setuptools wheel \
    && pip3 install --extra-index-url=https://www.piwheels.org/simple --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove \
        python3-pip \
        python3-dev \
        git \
        build-essential \
        libhdf5-dev \
        libhdf5-serial-dev \
        netcdf-bin \
        libnetcdf-dev \
        pkg-config \
        gfortran \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /

# copy contents
COPY config_emhass.yaml /usr/src
COPY rootfs /

# Labels
LABEL \
  io.hass.name="emhass" \
  io.hass.description="EMHASS: Energy Management for Home Assistant" \
  io.hass.version=${BUILD_VERSION} \
  io.hass.type="addon" \
  io.hass.arch="aarch64|amd64|armhf|armv7"

