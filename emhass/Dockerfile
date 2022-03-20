#FROM python:3.8-slim-buster
ARG BUILD_FROM
FROM $BUILD_FROM

# Copy root filesystem
COPY rootfs /

# Copy Python requirements file
COPY requirements.txt /tmp/

# Install packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3 \
        python3-dev \
        build-essential \
        git \
    && curl --silent --show-error --retry 5 \
        "https://bootstrap.pypa.io/get-pip.py" \
        | python3 \
    && pip3 install --no-cache-dir \
        -r /tmp/requirements.txt \
    && apt-get remove -y --purge \
        python3-dev \
        build-essential \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Setup base
#RUN apt-get update \
#    && pip3 install --no-cache-dir \
#    -r /tmp/requirements.txt \

# Build arguments
ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_REF
ARG BUILD_VERSION

# Labels
LABEL \
    io.hass.name="emhass" \
    io.hass.description="EMHASS: Energy Management for Home Assistant" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="David" \
    org.label-schema.description="EMHASS: Energy Management for Home Assistant" \
    org.label-schema.build-date=${BUILD_DATE} \
    org.label-schema.name="emhass" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.url="https://github.com/davidusb-geek/emhass" \
    org.label-schema.usage="https://github.com/davidusb-geek/emhass/README.md" \
    org.label-schema.vcs-ref=${BUILD_REF} \
    org.label-schema.vcs-url="https://github.com/davidusb-geek/emhass" \
    org.label-schema.vendor="Community Hass.io Addons"
