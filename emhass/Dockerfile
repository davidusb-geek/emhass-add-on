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
    && pip3 install --no-cache-dir -U setuptools wheel \
    && pip3 install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove \
        git \
        build-essential \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /

# copy contents
COPY app_server.py /usr/src
COPY config_emhass.json /usr/src
COPY templates /usr/src/templates
COPY static /usr/src/static
COPY data /usr/src/data
COPY rootfs /

# Labels
LABEL \
  io.hass.name="emhass" \
  io.hass.description="EMHASS: Energy Management for Home Assistant" \
  io.hass.version=${BUILD_VERSION} \
  io.hass.type="addon" \
  io.hass.arch="aarch64|amd64|armhf|armv7"

