ARG BUILD_FROM=python:3.9-alpine3.14
FROM ${BUILD_FROM}

# Copy root filesystem
COPY rootfs /

# Copy Python requirements file
COPY requirements.txt /tmp/

# Setup base
ARG BUILD_ARCH=amd64
RUN \
    apk add --no-cache --virtual .build-dependencies \
        gcc=9.3.0-r0 \
        libc-dev=0.7.2-r3 \
        libffi-dev=3.2.1-r6 \
        openssl-dev=1.1.1l-r0 \
    \
    && apk add --no-cache \
        dbus=1.12.20-r1 \
    \
    && pip3 install \
        --no-cache-dir \
        --prefer-binary \
        --find-links "https://wheels.home-assistant.io/alpine-3.14/${BUILD_ARCH}/" \
        -r /tmp/requirements.txt \
    \
    && find /usr/local \
        \( -type d -a -name test -o -name tests -o -name '__pycache__' \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    \
    && apk del --no-cache --purge .build-dependencies

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
