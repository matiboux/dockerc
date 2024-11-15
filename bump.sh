#!/bin/sh

# DockerC Version Bumper
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

			'--disable-git' | '-n' )
				# Disable git support
				DOCKERC_DISABLE_GIT='true'
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

	# Parse mandatory version positional argument
	if [ "$#" -le 0 ] || [ -z "$1" ]; then
		echo 'Error: No version specified.' >&2
		DOCKERC_PRINT_HELP='true'
		ERROR_CODE=1
		break
	fi
	DOCKERC_VERSION="$1"
	shift

	# Stop parsing arguments
	break

done

if [ "$DOCKERC_PRINT_HELP" = 'true' ]; then
	# Print help & exit
	echo "Usage: $0 [options] <version>"
	echo ''
	echo 'Options:'
	echo '  -h, --help         Print this help message'
	echo '  -n, --disable-git  Disable git support'
	echo ''
	echo 'Arguments:'
	echo '  version  Version to bump to (e.g. 1.1.0)'
	exit ${ERROR_CODE:-0}
fi

# Get whether to use git
USE_GIT='true'
if [ "$DOCKERC_DISABLE_GIT" = 'true' ]; then
	# Disable git
	USE_GIT='false'
fi

if [ "$USE_GIT" = 'true' ]; then
	if [ ! -d './.git' ]; then
		# Directory is not a git repository
		USE_GIT='false'
	else
		# Check that git is installed
		git --version > /dev/null 2>&1
		if [ $? -ne 0 ]; then
			echo 'Warning: Git is not installed.' >&2
			USE_GIT='false'
		fi
	fi
fi

# Get version from argument
VERSION="$DOCKERC_VERSION"

# Bump version in dockerc
if [ "$(uname -s)" = 'Darwin' ]; then
	# MacOS
	sed -i '' "3 s/\# DockerC.*/\# DockerC (v$VERSION)/g" ./dockerc
	sed -i '' "10 s/VERSION=.*/VERSION='$VERSION'/g" ./dockerc
else
	# Linux
	sed -i "3 s/\# DockerC.*/\# DockerC (v$VERSION)/g" ./dockerc
	sed -i "10 s/VERSION=.*/VERSION='$VERSION'/g" ./dockerc
fi

if [ "$USE_GIT" = true ]; then
	# Commit changes in git
	git add ./dockerc > /dev/null 2>&1
	git commit -m "Bump version to $VERSION" > /dev/null 2>&1
	if [ $? -ne 0 ]; then
		echo 'Warning: Failed to commit changes.' >&2
	else
		git tag -a "v$VERSION" -m "Bump version to $VERSION"
		echo "Info: Commited changes & tagged 'v$VERSION' in git" >&2
	fi
fi

echo "Version bumped to $VERSION!"
