# Ubuntu (GNOME)

Set solid background color for desktop:

```bash
manlix@lab:~$ sudo apt install dconf-cli
manlix@lab:~$ dconf write /org/gnome/desktop/background/picture-options "'none'"
manlix@lab:~$ dconf write /org/gnome/desktop/background/primary-color "'#34414e'"

```

Or you can use GUI by installing **dconf-editor**.


# Node.js

## Useful links about Node.js

* https://nodejs.org — Node.js homepage
* https://snapcraft.io/node — snap page with Node.js
* https://github.com/nodesource/distributions — Node.js binary distributions by NodeSource

## Installing Node.js 13 from snap


```bash
manlix@lab:~$ sudo snap install node --channel=13/stable --classic
node (13/stable) 13.6.0 from NodeSource, Inc. (nodesource✓) installed

manlix@lab:~$ node --version
v13.6.0
```
