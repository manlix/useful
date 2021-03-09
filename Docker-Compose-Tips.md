# Docker Compose Tips

## Run service with host network

```yml
version: '3.7'

services:

  srv:
    image: ubuntu
    network_mode: host
```

## Run service with host network during building image from Dockerfile

```yml
version: '3.7'

services:

  srv:
    build:
      contex: .
      dockerfile: Dockerfile
      network: host
```

## Run service with openned STDIN

```yml
version: '3.7'

services:

  srv:
    image: ubuntu
    stdin_open: true
    tty: true
```

After that you can run service as daemon and run bash:
```bash
$ docker-compose up -d
$ docker-compose exec srv bash
```
