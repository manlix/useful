# Highlight the differences between successive updates

Use utility **watch**:

Update APT cache:
```
manlix@lab:~$ sudo apt update
```

Install **watch** utility (package **procps**):
```
manlix@lab:~$ sudo apt install -y procps
```

Watching highlight output for date updated every 1 second
```
manlix@lab:~$ watch -n1 -d date
```

Where:
```
# -n1 -- update interval (1 second)
# -d -- highlight the differences between successive updates
```
