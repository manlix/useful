# Highlight the differences between successive updates


## Installation

Update APT cache:
```
manlix@lab:~$ sudo apt update
```


Install **watch** utility (package **procps**):
```
manlix@lab:~$ sudo apt install -y procps
```

## Hightlights for every 1 seconds

Watching highlight output for `date` updated every 1 second
```
manlix@lab:~$ watch -n1 -d date
```

### Where
```
-n1 — update interval (1 second)
-d — highlight the differences between successive updates
```

## Incremental hightlights for every 1 seconds

Watching hightlight output changes for `date` since 1st run:
```
manlix@lab:~$ watch -n1 -d=1 date
```

### Where
```
-n1 — update interval (1 second)
-d=1 — incremental highlight the differences between successive updates
```
