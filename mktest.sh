#!/bin/sh

mkdir -p ./test
mkdir -p ./test/docker

touch ./test/docker-compose.yml
touch ./test/docker-compose.override.yml
touch ./test/docker-compose.prod.yml
touch ./test/docker-compose.dev.yml

touch ./test/docker-compose.top.yml
touch ./test/docker/docker-compose.sub.yml
