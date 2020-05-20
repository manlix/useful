# VirtualBox CLI

### Use Efi instead BIOS
```
manlix@lab:~$ VBoxManage modifyvm "VM_NAME_OR_UUID" --firmware efi

# See: https://www.virtualbox.org/manual/ch03.html#efi
```

### Select "Full HD: 1920x1080" for a graphics resolution to VM with EFI
```
manlix@lab:~$ VBoxManage setextradata "VM_NAME_OR_UUID" VBoxInternal2/EfiGraphicsResolution 1920x1080

# See: https://www.virtualbox.org/manual/ch03.html#efividmode
```
