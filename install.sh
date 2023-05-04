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

curl -fsSL https://raw.githubusercontent.com/matiboux/dockerc/HEAD/dockerc -o "$INSTALL_DIR/dockerc"
if [ $? -ne 0 ]; then
	echo "Error: Installation failed."
	exit 1
fi

chmod +x "$INSTALL_DIR/dockerc"
if [ $? -ne 0 ]; then
	echo "Error: Failed to add execute permission."
	exit 1
fi

echo "DockerC installed successfully at '$INSTALL_DIR/dockerc'!"
