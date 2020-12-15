# Docker

## Run Docker under non-root user

...and fix for '`Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: permission denied`'


**Error message during run Docker under non-root user**
```bash
manlix@lab:~$ docker container list
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.40/containers/json: dial unix /var/run/docker.sock: connect: permission denied
```

**Issue: I am not a member of the group 'docker'**
```bash
manlix@lab:~$ id -Gn
manlix adm cdrom sudo dip plugdev lpadmin sambashare
```

**Solution: add user to group 'docker'**
```bash
$ manlix@lab:~$ sudo usermod -aG docker ${USER}
```

**Re-login or just replace the current process (to load new group 'docker' for me). You must be a member of the group 'sudo'**
```bash
$ manlix@lab:~$ exec su - ${USER}
Password:
```

**Check group list (see 'docker' at the end of line)**
```bash
manlix@lab:~$ id -Gn
manlix adm cdrom sudo dip plugdev lpadmin sambashare docker
```

**Result: list all running containers under non-root user**
```bash
manlix@lab:~$ docker container list
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
ebde53e444fb        ubuntu              "/bin/bash"         11 seconds ago      Up 10 seconds                           happy_zhukovsky
```
