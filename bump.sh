#!/bin/sh

# DockerC Version Bumper
# Wrapper for docker compose commands in your project.
# https://github.com/matiboux/dockerc
# MIT License
# Copyright (c) 2023 Matiboux
# This project is not affiliated with Docker, Inc.

# Parse options arguments
if [ "$#" -gt 0 ]; then

	if [ "$1" = "--disable-git" ] || [ "$1" = "-n" ]; then
		DOCKERC_DISABLE_GIT='true'
		shift
	fi

fi

# Parse version argument
if [ "$#" -le 0 ] || [ -z "$1" ]; then
	echo "Error: No version specified." >&2
	exit 1
fi
VERSION="$1"
shift

HAS_GIT='true'
if [ "$DOCKERC_DISABLE_GIT" = 'true' ]; then
	# Disable git
	HAS_GIT='false'
fi

# Check that git is installed
if [ ! -d ".git" ]; then
	HAS_GIT=false
else
	git --version > /dev/null 2>&1
	if [ $? -ne 0 ]; then
		echo "Warning: Git is not installed."
		HAS_GIT=false
	fi
fi

# Bump version in dockerc
if [ "$(uname)" = "Darwin" ]; then
	# MacOS
	sed -i "" "3 s/\# DockerC.*/\# DockerC (v$VERSION)/g" dockerc
	sed -i "" "10 s/VERSION=.*/VERSION=\"$VERSION\"/g" dockerc
else
	# Linux
	sed -i "3 s/\# DockerC.*/\# DockerC (v$VERSION)/g" dockerc
	sed -i "10 s/VERSION=.*/VERSION=\"$VERSION\"/g" dockerc
fi

if [ "$HAS_GIT" = true ]; then
	# Commit changes
	git add dockerc
	git commit -m "Bump version to $VERSION"
	if [ $? -ne 0 ]; then
		echo "Warning: Failed to commit changes."
	else
		git tag -a "v$VERSION" -m "Bump version to $VERSION"
	fi
fi

echo "Version bumped to $VERSION!"
