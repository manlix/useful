## Fix Arduino IDE issue: Error opening serial port '/dev/ttyUSB0'

Issue: access denied to use device **/dev/ttyUSB0**:
```
manlix@lab:~$ ls -l /dev/ttyUSB0 
crw--w---- 1 root dialout 188, 0 Aug 17 11:09 /dev/ttyUSB0
```

Solution: add user to group 'dialout' and re-run Arduino IDE:
```
manlix@lab:~$ sudo usermod -aG dialout ${USER}
```
