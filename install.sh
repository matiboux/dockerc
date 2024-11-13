#!/bin/sh

# DockerC Installer
# Wrapper for docker compose commands in your project.
# https://github.com/matiboux/dockerc
# MIT License
# Copyright (c) 2023 Matiboux
# This project is not affiliated with Docker, Inc.

ERROR_CODE=''

# Parse options arguments
if [ "$#" -gt 0 ]; then

	if [ "$1" = '--help' ] || [ "$1" = '-h' ]; then
		DOCKERC_PRINT_HELP='true'
		shift
	fi

	if [ "$1" = '--install-dir' ] || [ "$1" = '-i' ]; then
		# Installation directory argument is provided
		shift
		if [ -z "$1" ]; then
			echo 'Error: Missing installation directory.' >&2
			exit 1
		fi
		DOCKERC_INSTALL_DIR="$1"
		shift
	fi

	if [ -n "$1" ]; then
		# Version argument is provided
		DOCKERC_REQUIRED_TAG="v$1"
		shift
	fi

fi

if [ "$DOCKERC_PRINT_HELP" = 'true' ]; then
	# Print help & exit
	echo "Usage: $0 [options] [version]"
	echo ''
	echo 'Options:'
	echo '  --help, -h         Display this help message'
	echo '  --install-dir, -i  Installation directory (defaults to /usr/local/bin)'
	echo ''
	echo 'Arguments:'
	echo '  version  DockerC version to install (defaults to HEAD)'
	exit ${ERROR_CODE:-0}
fi

# Get installation directory
if [ -n "$DOCKERC_INSTALL_DIR" ]; then
	# Use from argument or environment variable
	INSTALL_DIR="$DOCKERC_INSTALL_DIR"
else
	# Default installation directory
	INSTALL_DIR='/usr/local/bin'
fi

# Get required tag to install
if [ -n "$DOCKERC_REQUIRED_TAG" ]; then
	# Use from argument or environment variable
	REQUIRED_TAG="$DOCKERC_REQUIRED_TAG"
else
	# Default required tag
	REQUIRED_TAG='HEAD'
fi

# Check that docker is installed
docker --help > /dev/null 2>&1
if [ $? -ne 0 ]; then
	echo 'Error: Docker is not installed.' >&2
	exit 1
fi

# Check that docker compose is installed
docker compose --help > /dev/null 2>&1
if [ $? -ne 0 ]; then
	echo 'Error: Docker compose is not installed.' >&2
	exit 1
fi

curl -fsSL https://raw.githubusercontent.com/matiboux/dockerc/$REQUIRED_TAG/dockerc -o "$INSTALL_DIR/dockerc"
if [ $? -ne 0 ]; then
	echo 'Error: DockerC installation failed.' >&2
	exit 1
fi

chmod +x "$INSTALL_DIR/dockerc"
if [ $? -ne 0 ]; then
	echo 'Error: Failed to add execute permission.' >&2
	exit 1
fi

echo "DockerC ($REQUIRED_TAG) installed successfully at '$INSTALL_DIR/dockerc'!"
