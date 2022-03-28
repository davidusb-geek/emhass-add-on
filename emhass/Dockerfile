FROM python:3.8-slim-buster

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# Setup slim-buster
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
        build-essential \
        make \
        gcc \
    && pip3 install --no-cache-dir \
        -r requirements.txt \
    && apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app_server.py" ]

# Labels
LABEL \
  io.hass.name="emhass" \
  io.hass.description="EMHASS: Energy Management for Home Assistant" \
  io.hass.version=${BUILD_VERSION} \
  io.hass.type="addon" \
  io.hass.arch="aarch64|amd64|armhf|armv7|i386"

