#!/bin/sh

# DockerC Installer
# https://github.com/matiboux/dockerc
# MIT License
# Copyright (c) 2023 Matiboux

if [ "$#" -gt 0 ]; then
	# Get install directory from first parameter and shift
	INSTALL_DIR="$1"
	shift
else
	INSTALL_DIR="/usr/local/bin"
fi

# Check that docker compose is installed
docker compose --help &> /dev/null
if [ $? -ne 0 ]; then
	echo "Error: Docker compose is not installed."
	exit 1
fi

curl -fsSL https://raw.githubusercontent.com/matiboux/dockerc/HEAD/dockerc -o "$INSTALL_DIR/dockerc"
if [ $? -ne 0 ]; then
	echo "Error: DockerC installation failed."
	exit 1
fi

chmod +x "$INSTALL_DIR/dockerc"
if [ $? -ne 0 ]; then
	echo "Error: Failed to add execute permission."
	exit 1
fi

echo "DockerC installed successfully at '$INSTALL_DIR/dockerc'!"
