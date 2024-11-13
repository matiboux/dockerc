#!/bin/sh

# DockerC Installer
# Wrapper for docker compose commands in your project.
# https://github.com/matiboux/dockerc
# MIT License
# Copyright (c) 2023 Matiboux
# This project is not affiliated with Docker, Inc.

ERROR_CODE=''
DOCKERC_PARSE_ARGUMENTS='true'

# Parse options arguments
while [ "$DOCKERC_PARSE_ARGUMENTS" = 'true' ] && [ "$#" -gt 0 ]; do

	if [ "$1" = '--help' ] || [ "$1" = '-h' ]; then
		DOCKERC_PRINT_HELP='true'
		shift

	elif [ "$1" = '--install-dir' ] || [ "$1" = '-i' ]; then
		# Installation directory argument is provided
		shift
		if [ -z "$1" ]; then
			echo 'Error: Missing installation directory.' >&2
			DOCKERC_PRINT_HELP='true'
			ERROR_CODE=1
			# Stop parsing arguments
			DOCKERC_PARSE_ARGUMENTS='false'
			break
		fi
		DOCKERC_INSTALL_DIR="$1"
		shift

	else
		# Unknown option, maybe first argument
		# Stop parsing options
		break
	fi

done

if [ "$DOCKERC_PARSE_ARGUMENTS" = 'true' ]; then
	# Parse positional arguments

	# Parse install tag optional argument
	if [ "$#" -gt 0 ]; then
		DOCKERC_INSTALL_TAG="$1"
		shift
	fi

fi

if [ "$DOCKERC_PRINT_HELP" = 'true' ]; then
	# Print help & exit
	echo "Usage: $0 [options] [tag]"
	echo ''
	echo 'Options:'
	echo '  --help, -h         Display this help message'
	echo '  --install-dir, -i  Installation directory (defaults to /usr/local/bin)'
	echo ''
	echo 'Arguments:'
	echo '  tag  DockerC tag/version to install (defaults to HEAD)'
	exit ${ERROR_CODE:-0}
fi

# Get installation directory
INSTALL_DIR='/usr/local/bin' # Default installation directory
if [ -n "$DOCKERC_INSTALL_DIR" ]; then
	# Use from argument or environment variable
	INSTALL_DIR="$DOCKERC_INSTALL_DIR"
fi

# Get install tag
INSTALL_TAG='HEAD' # Default required tag
if [ -n "$DOCKERC_INSTALL_TAG" ]; then
	# Use from argument or environment variable
	INSTALL_TAG="$DOCKERC_INSTALL_TAG"
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

curl -fsSL "https://raw.githubusercontent.com/matiboux/dockerc/$INSTALL_TAG/dockerc" -o "$INSTALL_DIR/dockerc"
if [ $? -ne 0 ]; then
	echo 'Error: DockerC installation failed.' >&2
	exit 1
fi

chmod +x "$INSTALL_DIR/dockerc"
if [ $? -ne 0 ]; then
	echo 'Error: Failed to add execute permission.' >&2
	exit 1
fi

echo "DockerC ($INSTALL_TAG) installed successfully at '$INSTALL_DIR/dockerc'!"
