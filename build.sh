#!/bin/bash

DOCKER_IMAGE=local/certbot-dns-vultr

docker build \
    --force-rm \
    -t $DOCKER_IMAGE \
    .

# List image in docker
docker images $DOCKER_IMAGE
