#!/bin/sh

# DockerC Installer
# Wrapper for docker compose commands in your project.
# https://github.com/matiboux/dockerc
# MIT License
# Copyright (c) 2023 Matiboux
# This project is not affiliated with Docker, Inc.

ERROR_CODE=''

# Parse arguments
# Dummy while loop to allow breaking
while true; do

	# Parse options arguments
	while [ "$#" -gt 0 ]; do

		case "$1" in

			'--help' | '-h' )
				# Print help
				DOCKERC_PRINT_HELP='true'
				shift
				;;

			'--install-dir' | '-i' )
				shift
				# Check for installation directory argument
				if [ -z "$1" ]; then
					echo 'Error: Missing installation directory.' >&2
					DOCKERC_PRINT_HELP='true'
					ERROR_CODE=1
					break
				fi
				# Set installation directory
				DOCKERC_INSTALL_DIR="$1"
				shift
				;;

			* )
				break
				;;

		esac

	done

	if [ "$DOCKERC_PRINT_HELP" = 'true' ]; then
		# Stop parsing arguments
		break
	fi

	# Check for optional positional arguments
	if [ "$#" -le 0 ]; then
		# No more arguments
		break
	fi

	# Parse first optional positional argument
	# Parse install tag argument
	DOCKERC_INSTALL_TAG="$1"
	shift

	# Stop parsing arguments
	break

done

if [ "$DOCKERC_PRINT_HELP" = 'true' ]; then
	# Print help & exit
	echo "Usage: $0 --update [options] [tag]"
	echo ''
	echo 'Options:'
	echo '  -h, --help         Print this help message'
	echo '  -i, --install-dir  Set installation directory'
	echo "    (defaults to directory '/usr/local/bin')"
	echo ''
	echo 'Arguments:'
	echo '  tag  DockerC tag/version to install'
	echo '    (defaults to latest version)'
	exit ${ERROR_CODE:-0}
fi

# Get install directory
INSTALL_DIR='/usr/local/bin' # Default installation directory
if [ -n "$DOCKERC_INSTALL_DIR" ]; then
	# Use from argument or environment variable
	INSTALL_DIR="$DOCKERC_INSTALL_DIR"
fi

# Get install tag
INSTALL_TAG='latest'
if [ -n "$DOCKERC_INSTALL_TAG" ]; then
	# Use from argument or environment variable
	if
		[ "$DOCKERC_INSTALL_TAG" = 'HEAD' ] || [ "$DOCKERC_INSTALL_TAG" = 'head' ] ||
		[ "$DOCKERC_INSTALL_TAG" = '.' ] || [ "$DOCKERC_INSTALL_TAG" = '-' ]
	then
		INSTALL_TAG='HEAD'
	else
		INSTALL_TAG="$DOCKERC_INSTALL_TAG"
	fi
fi

if [ ! -d "$INSTALL_DIR" ]; then
	echo 'Error: Install directory does not exist.' >&2
	exit 1
fi

get_latest_version() {
	# Syntax: '"tag_name": "v1.0.0",'
	LATEST_VERSION_JSON=$(
		curl -fsSL "https://api.github.com/repos/matiboux/dockerc/releases/latest" 2>/dev/null \
		| grep -Eo '"tag_name": "(.+?)",'
	)

	if [ -n "$LATEST_VERSION_JSON" ]; then
		if [ "$(uname -s)" = 'Darwin' ]; then
			# MacOS
			LATEST_VERSION="${LATEST_VERSION_JSON:14:$((${#LATEST_VERSION_JSON}-14-2))}"
		else
			# Linux
			LATEST_VERSION=$(expr substr "$LATEST_VERSION_JSON" $(expr 1 + 14) $(expr length "$LATEST_VERSION_JSON" - 14 - 2))
		fi

		echo "$LATEST_VERSION"
	fi
}

if [ "$INSTALL_TAG" = 'latest' ]; then
	# Default install tag is latest released version
	INSTALL_TAG="$(get_latest_version)"
	if [ -z "$INSTALL_TAG" ]; then
		echo 'Error: Failed to get latest version.' >&2
		exit 1
	fi
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
