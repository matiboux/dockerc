# DockerC

Wrapper for docker compose commands in your project.


## Install

First, make sure you have required dependencies installed on your system:
- Docker
- Docker Compose V2

Then, paste this in your terminal to install DockerC:

```bash
/bin/sh -c "$(curl -fsSL https://raw.githubusercontent.com/matiboux/dockerc/HEAD/install.sh)"
```

Take a look at the [install.sh](install.sh) script to see what it does.

If you get the error `Failure writing output to destination`, you can try to run the command again with `sudo`:

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
dockerc               # -> docker compose up -d

dockerc -             # -> docker compose up -d
dockerc - down        # -> docker compose down
dockerc - exec app sh # -> docker compose exec app bash

dockerc --            # -> docker compose up -d
dockerc -- start      # -> docker compose start

# The dev context works in the same way as long as no matching file is found!
dockerc dev           # -> docker compose up -d
dockerc dev logs      # -> docker compose logs

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
