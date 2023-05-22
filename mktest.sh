#!/bin/sh

if [ $# -ge 1 ]; then
	DIR=$1
	shift
else
	DIR="."
fi

if [ -d "$DIR/test" ]; then
	rm -r "$DIR/test/"*

	if [ $? -ne 0 ]; then
		echo "Failed to clear ./test directory."
		exit 1
	fi
fi

mkdir -p "$DIR/test"
mkdir -p "$DIR/test/docker"

touch "$DIR/test/docker-compose.yml"
touch "$DIR/test/docker-compose.override.yml"
touch "$DIR/test/docker-compose.prod.yml"
touch "$DIR/test/docker-compose.dev.yml"

touch "$DIR/test/.env"
touch "$DIR/test/.env.local"
touch "$DIR/test/.env.dev"
touch "$DIR/test/.env.dev.local"
touch "$DIR/test/.env.prod"
touch "$DIR/test/.env.prod.local"

touch "$DIR/test/docker-compose.top.yml"
touch "$DIR/test/docker/docker-compose.sub.yml"

touch "$DIR/test/.env.top"
touch "$DIR/test/docker/.env.sub"
