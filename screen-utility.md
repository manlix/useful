# Screen — screen manager

## Installation

```(bash)
manlix@lab:~$ sudo apt update
manlix@lab:~$ sudo apt install -y screen
```

## Usage

### Run screen

```(bash)
manlix@lab:~$ screen
```

### Detach screen session

```
[Ctrl] + [a] [d]
```

### List runned screen sessions

```(bash)
manlix@lab:~$ screen -ls
```

### Relauching screen and attach to last session

```(bash)
manlix@lab:~$ screen -r
````


### Relauching screen and attach to soecified session

```(bash)
manlix@lab:~$ screen -r SESSION_NAME
````
