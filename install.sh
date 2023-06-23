#!/bin/sh

# DockerC Installer
# https://github.com/matiboux/dockerc
# MIT License
# Copyright (c) 2023 Matiboux

if [ "$#" -gt 0 ]; then
	# Get install directory from parameter and shift
	INSTALL_DIR="$1"
	shift
else
	INSTALL_DIR="/usr/local/bin"
fi

if [ "$#" -gt 0 ]; then
	# Get specific version from parameter and shift
	REQUIRED_TAG="v$1"
	shift
else
	REQUIRED_TAG="HEAD"
fi

# Check that docker compose is installed
docker compose --help > /dev/null 2>&1
if [ $? -ne 0 ]; then
	echo "Error: Docker compose is not installed."
	exit 1
fi

curl -fsSL https://raw.githubusercontent.com/matiboux/dockerc/$REQUIRED_TAG/dockerc -o "$INSTALL_DIR/dockerc"
if [ $? -ne 0 ]; then
	echo "Error: DockerC installation failed."
	exit 1
fi

chmod +x "$INSTALL_DIR/dockerc"
if [ $? -ne 0 ]; then
	echo "Error: Failed to add execute permission."
	exit 1
fi

echo "DockerC ($REQUIRED_TAG) installed successfully at '$INSTALL_DIR/dockerc'!"
