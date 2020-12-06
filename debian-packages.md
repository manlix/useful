## Which debian package belongs utility **X** (for example: **whois**)

Try to look up **package_name** for installed utility **whois**
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
