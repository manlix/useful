# Ubuntu (GNOME)

Set solid color for desktop background:

```bash
manlix@lab:~$ sudo apt install dconf-cli
manlix@lab:~$ dconf write /org/gnome/desktop/background/picture-options "'none'"
manlix@lab:~$ dconf write /org/gnome/desktop/background/primary-color "'#34414e'"

```
