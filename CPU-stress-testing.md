## CPU stress testing by loading all cores on 100%

Update APT cache
```
manlix@lab:~$ sudo apt update
```

Install **stress-ng** utility
```
manlix@lab:~$ sudo apt install stress-ng
```

Load all CPU cores on 100% for 1 minute
```
manlix@lab:~$ stress-ng --cpu 0 -t 1m
```
