#!/bin/sh

if [ $# -ge 1 ]; then
	DIR=$1
	shift
else
	DIR="."
fi

if [ ! -d "$DIR/files/test" ]; then
	echo "Did not finc ./files/test directory."
	exit 1
fi

if [ -d "$DIR/test" ]; then
	rm -r "$DIR/test/"*

	if [ $? -ne 0 ]; then
		echo "Failed to clear ./test directory."
		exit 1
	fi
fi

cp -r "$DIR/files/test/" "$DIR/test/"
