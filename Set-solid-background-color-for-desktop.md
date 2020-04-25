# Ubuntu 20.04 (GNOME)

Set solid background color for desktop:

```bash
manlix@lab:~$ sudo apt update
manlix@lab:~$ sudo apt install dconf-cli
manlix@lab:~$ dconf write /org/gnome/desktop/background/picture-options "'none'"
manlix@lab:~$ dconf write /org/gnome/desktop/background/primary-color "'#34414e'"

```

Or you can use GUI by installing **dconf-editor**.

```
manlix@lab:~$ sudo apt update
manlix@lab:~$ sudo apt install dconf-editor
manlix@lab:~$ dconf-editor
```

1) Follow to: `org` -> `gnome` -> `desktop` -> `background` -> `picture-options`
2) Follow to: `org` -> `gnome` -> `desktop` -> `background` -> `primary-color`
