# Working with APT


## List all packages from APT repository

Update APT cache
```
manlix@lab:~$ sudo apt update
```

Where `REPO_PREFIX` — APT repository file
`sort -u` is required to sort packages list and remove duplicatesfrom different architectures

```
manlix@lab:~$ awk '/^Package/ {print $2}' /var/lib/apt/lists/REPO_PREFIX*Packages | sort -u
```

List all packages from repository:
```
manlix@lab:~$ sudo apt update
manlix@lab:~$ awk '/^Package/ {print $2}' /var/lib/apt/lists/ppa.launchpad.net_ondrej_php_ubuntu_dists_eoan_*Packages | sort -u
dh-php
icu-devtools
icu-doc
...
python3-libxml2-dbg
python-libxml2
python-libxml2-dbg
```
