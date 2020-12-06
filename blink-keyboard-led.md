# Blink keyboard LED from console (bash)

### Update APT cache
```
manlix@lab:~$ sudo apt update
```

### Install package 'x11-xserver-utils' with utility 'xset'
```
manlix@lab:~$ sudo apt install x11-xserver-utils
```

### Blink led 'Scroll Lock' on keyboard every 1 second. To exit from infinity loop — press [CTRL]+[C]
```
manlix@lab:~$ while :; do xset led on; sleep 1; xset led off; sleep 1; done
```
