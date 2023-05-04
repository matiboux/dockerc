#!/bin/sh

# Get context from first parameter
CONTEXT=$1
shift

# Print help
if [ "$CONTEXT" = "help" ]; then
	echo "Usage: $0 <mode> [<args> ...]"
	exit 0
fi

# If context is empty, set to the default context
if [ -z $CONTEXT ]; then
	CONTEXT="dev"
fi

# If arguments are empty, set to the default arguments
if [ -z $@ ]; then
	ARGS="up -d"
else
	ARGS=$@
fi

# Set compose file arguments
if [ $CONTEXT = "dev" ]; then
	COMPOSE_FILE_ARGS="" # Use default docker compose behavior

elif [ $CONTEXT = "prod" ]; then
	COMPOSE_FILE_ARGS="-f docker-compose.yml"

elif [ $CONTEXT = "cicd" ]; then
	COMPOSE_FILE_ARGS=" -f docker-compose.yml -f docker-compose-cicd.yml"

elif [ $CONTEXT = "notebooks" ]; then
	COMPOSE_FILE_ARGS=" -f docker-compose-notebooks.yml"

elif [ $CONTEXT = "notebooks-gpu" ]; then
	COMPOSE_FILE_ARGS=" -f docker-compose-notebooks.yml -f docker-compose-notebooks.gpu.yml"

else # Error
	echo "Error: Invalid context '$CONTEXT'"
	exit 1
fi

# Run docker compose
echo ""
echo "> docker compose$COMPOSE_FILE_ARGS $ARGS"
echo ""
exec docker compose$COMPOSE_FILE_ARGS $ARGS
