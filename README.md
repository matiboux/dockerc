# DockerC

![GitHub Release](https://img.shields.io/github/v/release/matiboux/dockerc)
[![Check CI](https://github.com/matiboux/dockerc/actions/workflows/check.yml/badge.svg)](https://github.com/matiboux/dockerc/actions/workflows/check.yml)

Wrapper for docker compose commands in your project.


## Install

First, install required dependencies on your system:
- Docker
- Docker Compose v2

Then, install DockerC with the following command:

```bash
/bin/sh -c "$(curl -fsSL https://raw.githubusercontent.com/matiboux/dockerc/HEAD/install.sh)"
# Usage: /bin/sh -c "$(cat install.sh)" -- [--help] [--install-dir <dir>] [tag]
```

Take a look at the [install.sh](install.sh) script to see what it does.

If you get a cURL error, check the following:

- cURL error `22`: Requested tag was not found. Verify your network and that the tag exists.

- cURL error `23`: Failed to install DockerC. Verify your permissions in the install directory or try to run the command again with `sudo`.
  ```bash
  sudo /bin/sh -c "$(curl -fsSL https://raw.githubusercontent.com/matiboux/dockerc/HEAD/install.sh)"
  ```


## Usage

DockerC simplifies the use of docker compose commands in your project.

Imagine you have a project with one or more docker compose files:

```
my-project/
├── ...
├── docker/
│   ├── docker-compose-train.yml
│   └── docker-compose-train.gpu.yml
├── docker-compose.yml
├── docker-compose.override.yml
├── docker-compose.prod.yml
└── ...
```

You can now run your docker compose commands with DockerC:

```sh
# The default context uses the override file if it exists!
dockerc               # -> docker compose -f docker-compose.yml -f docker-compose.override.yml up -d

# Use "-" to use the default context with arguments.
dockerc -             # -> docker compose -f docker-compose.yml -f docker-compose.override.yml up -d
dockerc - down        # -> docker compose -f docker-compose.yml -f docker-compose.override.yml down
dockerc - exec app sh # -> docker compose -f docker-compose.yml -f docker-compose.override.yml exec app bash

# Use "--" to use docker compose without file arguments.
dockerc --            # -> docker compose up -d
dockerc -- start      # -> docker compose start

# The dev context works like the default context as long as no matching file is found.
dockerc dev           # -> docker compose -f docker-compose.yml -f docker-compose.override.yml up -d
dockerc dev logs      # -> docker compose -f docker-compose.yml -f docker-compose.override.yml logs

dockerc prod          # -> docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
dockerc prod restart  # -> docker compose -f docker-compose.yml -f docker-compose.prod.yml restart

dockerc train         # -> docker compose -f docker/docker-compose-train.yml up -d
dockerc train stop    # -> docker compose -f docker/docker-compose-train.yml stop

dockerc train.gpu     # -> docker compose -f docker/docker-compose-train.yml -f docker/docker-compose-train.gpu.yml up -d
dockerc train.gpu ps  # -> docker compose -f docker/docker-compose-train.yml -f docker/docker-compose-train.gpu.yml ps

# Use "@exec" to execute a command in a running container.
dockerc @exec <container> <command>  # -> docker exec <container> <command>

# Use "@execi" to execute a command in a running container with interactive mode.
dockerc @execi <container> <command>  # -> docker exec -i <container> <command>

# Use "@execd" to execute a command in a running container with detached mode.
dockerc @execd <container> <command>  # -> docker exec -d <container> <command>
```


## License

Copyright (c) 2023 [Matiboux](https://github.com/matiboux) ([matiboux.me](https://matiboux.me))

Licensed under the [MIT License](https://opensource.org/license/MIT). You can see a copy in the [LICENSE](LICENSE) file.

Disclaimer:  
Docker is a trademark of Docker, Inc.
The license of this project does not grant any rights to use the Docker name, logo, or trademarks.
This project is not affiliated with Docker, Inc. or any of its related projects.
