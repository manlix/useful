# SUDO without password

## I would like to use 'sudo' without password
```
manlix@lab:~$ sudo -s
[sudo] password for manlix: 
```

## Issue: create rule for sudo:
```
manlix@lab:~$ echo "${USER} ALL=(ALL:ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/${USER}
manlix ALL=(ALL:ALL) NOPASSWD: ALL
```

## Result:
```
manlix@lab:~$ cat /etc/sudoers.d/manlix 
manlix ALL=(ALL:ALL) NOPASSWD: ALL
```

```
manlix@lab:~$ sudo -s
root@lab:~# whoami
root
```
