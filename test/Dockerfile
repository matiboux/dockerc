#syntax=docker/dockerfile:1.4

# This Dockerfile uses the root project folder as context.

# Versions
FROM python:3.12-slim AS python_upstream


# --
# App base image
FROM python_upstream AS app_base

WORKDIR /app

# Installing requirements
COPY --link ./test/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
	# Clean up
	pip cache purge && \
	rm -rf /root/.cache/pip


# --
# Prod build image

FROM app_base AS app_prod

ENV APP_ENV=prod

# Mount source code as volume
VOLUME /app

CMD [ "pytest" ]
