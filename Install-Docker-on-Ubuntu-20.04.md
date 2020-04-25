# Install Docker on Ubuntu 20.04 LTS (Focal Fossa)

## Check that you use `Ubuntu 20.04 LTS (Focal Fossa)`
```
manlix@lab:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04 LTS
Release:	20.04
Codename:	focal
```

## Update APT cache

```
manlix@lab:~$ sudo apt update
```

## Install Docker

```
manlix@lab:~$ sudo apt install -y docker.io

```

## Check Docker installed version

```
manlix@lab:~$ docker --version
Docker version 19.03.8, build afacb8b7f0
```

## Allow to run Docker under non-root account

Problem — non-root account is not allowing to use Docker:
```
manlix@lab:~$ docker ps
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.40/containers/json: dial unix /var/run/docker.sock: connect: permission denie
```

Reason — Docker socket is allowing to use only for `root` and group `docker`:
```
manlix@lab:~$ ls -l /var/run/docker.sock 
srw-rw---- 1 root docker 0 апр 25 14:13 /var/run/docker.sock
```

Solution — add yourself to group `docker`

```
manlix@lab:~$ sudo usermod -aG docker ${USER}
```

Login in to a `docker` group:
```
manlix@lab:~$ newgrp docker
```

And check that Docker is allowing ro run commands, for test it run command to list all containers (empty result is OK):
```
manlix@lab:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```


## Check Docker works fine — run first container `hello-world`:

```
manlix@lab:~$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
0e03bdcc26d7: Pull complete 
Digest: sha256:8e3114318a995a1ee497790535e7b88365222a21771ae7e53687ad76563e8e76
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
 ```
