#syntax=docker/dockerfile:1

# This Dockerfile uses the root folder as context.


# --
# Upstream images

FROM alpine:3.19 AS alpine_upstream
FROM python:3.11-slim AS python_upstream


# --
# Base image

FROM python_upstream AS app_base

# Create app directory
WORKDIR /app


# --
# Dev base image

FROM app_base AS app_dev_base

ENV APP_ENV=dev
ENV NODE_ENV=development


# --
# Test image

FROM app_dev_base AS app_test

ENV APP_ENV=test

# Install jq
RUN --mount=type=cache,target=/var/cache/apt \
	--mount=type=cache,target=/var/lib/apt \
	apt-get update && \
	apt-get install -y 'jq=1.6-2.1'

# Install pytest & plugins
RUN --mount=type=cache,target=/root/.cache/pip \
	pip install \
		'pytest ~= 8.3.2' \
		'pytest-cov ~= 5.0.0' \
		'pytest-shell-utilities ~= 1.9.0'

COPY --link --chmod=755 ./docker/docker-test-command.sh /usr/local/bin/docker-test-command

CMD [ "docker-test-command" ]
