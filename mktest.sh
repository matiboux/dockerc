#!/bin/sh

mkdir -p ./test
mkdir -p ./test/docker

touch ./test/docker-compose.yml
touch ./test/docker-compose.override.yml
touch ./test/docker-compose.prod.yml
touch ./test/docker-compose.dev.yml

touch ./test/.env
touch ./test/.env.local
touch ./test/.env.dev
touch ./test/.env.dev.local
touch ./test/.env.prod
touch ./test/.env.prod.local

touch ./test/docker-compose.top.yml
touch ./test/docker/docker-compose.sub.yml

touch ./test/.env.top
touch ./test/docker/.env.sub
