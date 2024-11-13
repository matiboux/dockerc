# DockerC

Wrapper for docker compose commands in your project.


## Install

First, install required dependencies on your system:
- Docker
- Docker Compose v2

Then, install DockerC with the following command:

```bash
/bin/sh -c "$(curl -fsSL https://raw.githubusercontent.com/matiboux/dockerc/HEAD/install.sh)"
```

Take a look at the [install.sh](install.sh) script to see what it does.

If you get the error `Failure writing output to destination`,
try to run the command again with `sudo` or grant yourself write permissions to install directory (`/usr/local/bin` by default).

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
```


## License

**MIT License**  
Copyright (c) 2023 Matiboux

You can find a copy of the MIT License in the [LICENSE](LICENSE) file.

Visit [matiboux.me](https://matiboux.me) for contact information.
