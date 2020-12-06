# CPU temperature

# Update APT cache
```
manlix@lab:~$ sudo apt update
```

Install sensors reader (package 'lm-sensors'):
```
manlix@lab:~$ sudo apt install -y lm-sensors
```

Get CPU temperature:
```
manlix@lab:~$ sensors
pch_cannonlake-virtual-0
Adapter: Virtual device
temp1:        +34.0°C  

coretemp-isa-0000
Adapter: ISA adapter
Package id 0:  +32.0°C  (high = +80.0°C, crit = +100.0°C)
Core 0:        +31.0°C  (high = +80.0°C, crit = +100.0°C)
Core 1:        +31.0°C  (high = +80.0°C, crit = +100.0°C)
Core 2:        +31.0°C  (high = +80.0°C, crit = +100.0°C)
Core 3:        +32.0°C  (high = +80.0°C, crit = +100.0°C)
```

Approach to dynamic watching temperature values
Install utility 'watch' (package: 'procps')

```
manlix@lab:~$ sudo apt install procps
```

Start dynamic waching:

```
manlix@lab:~$ watch -n1 -d sensors
```

Where:
```
-n1 — update values every 1 seconds
-d — highlight the differences between successive updates
```
