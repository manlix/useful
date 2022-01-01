# Burn ISO to USB drive in Ubuntu

```shell
$ sudo dd if=/path/to/image.iso of=/path/to/USB_DRIVE bs=4M conv=fdatasync status=progress
```

In my case `/path/to/USB_DRIVE` is `/dev/sdb`:

```
$ lsblk -S
NAME HCTL       TYPE VENDOR   MODEL                  REV SERIAL           TRAN
sda  5:0:0:0    disk ATA      KINGSTON_SA400S37240G B1D2 50026B7682FAFC82 sata
sdb  6:0:0:0    disk USB2.0   Flash_Disk            2.b0 0MMDDP8174603127 usb     <----
```
