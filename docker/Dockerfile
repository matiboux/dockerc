#syntax=docker/dockerfile:1

# This Dockerfile uses the root folder as context.


# --
# Upstream images

FROM python:3.11-slim AS python_upstream


# --
# Python + Docker image

FROM python_upstream AS python_docker

# Install Docker CLI
RUN --mount=type=cache,target=/var/cache/apt \
	--mount=type=cache,target=/var/lib/apt \
	apt-get update && \
	apt-get install -y \
		ca-certificates \
		curl \
		&& \
	install -m 0755 -d /etc/apt/keyrings && \
	curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc && \
	chmod a+r /etc/apt/keyrings/docker.asc && \
	echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
		https://download.docker.com/linux/debian \
		$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
		tee /etc/apt/sources.list.d/docker.list > /dev/null \
		&& \
	apt-get update && \
	apt-get install -y \
		docker-ce \
		docker-ce-cli \
		containerd.io \
		docker-buildx-plugin \
		docker-compose-plugin


# --
# Base image

FROM python_docker AS app_base

# Set app directory
WORKDIR /app


# --
# Runtime base image

FROM app_base AS app_runtime_base

# Set runtime environment
ENV APP_ENV=dev
ENV NODE_ENV=development

# Copy application source code
COPY --link . .


# --
# Test image

FROM app_runtime_base AS app_test

ENV APP_ENV=test
ENV PYTHONPATH=/app

# Install jq
RUN --mount=type=cache,target=/var/cache/apt \
	--mount=type=cache,target=/var/lib/apt \
	apt-get update && \
	apt-get install -y jq

# Install pytest & plugins
RUN --mount=type=cache,target=/root/.cache/pip \
	pip install \
		'pytest ~= 8.3.2' \
		'pytest-cov ~= 5.0.0' \
		'pytest-shell-utilities ~= 1.9.0'

COPY --link --chmod=755 ./docker/test-command.sh /usr/local/bin/app-test-command

CMD [ "app-test-command" ]


# --
# Test watch image

FROM app_test AS app_test_watch

# Install pytest-watch
RUN --mount=type=cache,target=/tmp/pip-cache \
	export PIP_CACHE_DIR=/tmp/pip-cache && \
	pip install \
		'pytest-watch ~= 4.2.0' \
		'pytest-testmon ~= 2.1.1'

ENV TESTMON_DATAFILE='/tmp/pytest/.testmondata'

COPY --link --chmod=755 ./docker/test-watch-command.sh /usr/local/bin/app-test-watch-command
CMD [ "app-test-watch-command" ]
