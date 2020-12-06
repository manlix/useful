## Which debian package belongs utility **X**

For example: installed package — **whois**
```
manlix@lab:~$ dpkg -S whois
whois: /usr/share/man/man1/whois.1.gz
whois: /usr/share/man/man5/whois.conf.5.gz
language-pack-en-base: /usr/share/locale-langpack/en_GB/LC_MESSAGES/whois.mo
whois: /usr/share/doc/whois/copyright
whois: /usr/share/doc/whois/README
whois: /usr/bin/whois                                                             <-------------------------
language-pack-en-base: /usr/share/locale-langpack/en_CA/LC_MESSAGES/whois.mo
language-pack-en-base: /usr/share/locale-langpack/en_AU/LC_MESSAGES/whois.mo
whois: /usr/share/doc/whois/changelog.gz
whois: /usr/share/doc/whois
```

Based on info below: **whois** is a part of package **whois** =)

## List all files belong to debian package

For example: package — **apache2-utils**

```
manlix@lab:~$ dpkg -L apache2-utils
/.
/usr
/usr/bin
/usr/bin/ab
...
/usr/share/man/man8/htcacheclean.8.gz
/usr/share/man/man8/rotatelogs.8.gz
/usr/share/man/man8/split-logfile.8.gz
```


## List files from package.deb

For example: package file — **cprocsp-rdr-pcsc-64_4.0.9963-5_amd64.deb**

```
manlix@lab:~$ dpkg -c ./cprocsp-rdr-pcsc-64_4.0.9963-5_amd64.deb
drwxr-xr-x root/root         0 2018-11-23 00:00 ./
drwxr-xr-x root/root         0 2018-11-23 00:00 ./opt/
drwxr-xr-x root/root         0 2018-11-23 00:00 ./opt/cprocsp/
...
lrwxrwxrwx root/root         0 2018-11-23 00:00 ./opt/cprocsp/lib/amd64/librdrpcsc.so.4 -> librdrpcsc.so.4.0.4
lrwxrwxrwx root/root         0 2018-11-23 00:00 ./opt/cprocsp/lib/amd64/librdrric.so.4 -> librdrric.so.4.0.4
lrwxrwxrwx root/root         0 2018-11-23 00:00 ./opt/cprocsp/lib/amd64/librdrpcsc.so -> librdrpcsc.so.4.0.4
```
