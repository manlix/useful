# Install Docker Compose v2 on Ubuntu 21.10 system-wide

Before start you should install Docker (see: [Install-Docker-on-Ubuntu-21.10.md](Install-Docker-on-Ubuntu-21.10.md))

## Check Ubuntu version

```
manlix@lab:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 21.10
Release:	21.10
Codename:	impish
```

## Create directory for Docker Compose v2

```
manlix@lab:~$ sudo mkdir -p /usr/local/lib/docker/cli-plugins
```

## Install wget

```
manlix@lab:~$ sudo apt update && sudo apt install -y wget
```

## Install Docker Compose v2

```
manlix@lab:~$ sudo wget -q https://github.com/docker/compose/releases/download/v2.1.0/docker-compose-linux-x86_64 -O /usr/local/lib/docker/cli-plugins/docker-compose

```

## Check installed Docker Compose v2 version
```
manlix@lab:~$ sudo docker compose version
Docker Compose version v2.1.0
```

Originally from official docs: https://github.com/docker/compose/blob/v2/README.md
