#!/bin/sh

# DockerC Version Bumper
# https://github.com/matiboux/dockerc
# MIT License
# Copyright (c) 2023 Matiboux

HAS_GIT=true

if [ "$1" = "-n" ]; then
	# Disable git
	HAS_GIT=false
	shift
fi

# Get version from first parameter and shift
if [ "$#" -gt 0 ]; then
	VERSION="$1"
	shift

else
	echo "Error: No version specified."
	echo "Usage: $0 [-n] <version>"
	exit 1
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
sed -i "3 s/\# DockerC.*/\# DockerC (v$VERSION)/g" dockerc

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
