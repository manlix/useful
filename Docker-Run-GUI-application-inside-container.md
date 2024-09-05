# Docker: run GUI application inside container

```sh
# Run Docker container with latest Ubuntu and pass $DISPLAY from host into it
manlix@lab:~$ docker run --rm --net=host --env="DISPLAY" --volume="$XAUTHORITY:/root/.Xauthority:rw" -it ubuntu

# Install simple GUI applications for test
root@lab:/# apt update && apt install -y x11-apps

# Run GUI application 'calculator'
root@lab:/# xcalc
```
