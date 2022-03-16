ARG BUILD_FROM
FROM $BUILD_FROM

# Copy root filesystem
COPY rootfs /

# Copy the EMHASS wheel
COPY emhass-0.2.2-py3-none-any.whl /tmp/

# Install requirements for add-on
RUN apk add --update py3-pip
RUN pip3 install \
    --no-cache-dir \
    --prefer-binary \
    -r /tmp/emhass-0.2.2-py3-none-any.whl

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
