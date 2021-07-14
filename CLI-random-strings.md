# Random strings in one line

## by OpenSSL

```bash
manlix@lab:~$ openssl rand -hex 32
5c441a019990d0c86254e7c82288a1b6066c4c97e2398e0f225d43d020f2a0eb
```

## by Python 3.6+

###  Method 1

```bash
manlix@lab:~$ python3 -c 'import secrets; print(secrets.token_hex(32))'
c330ebfec812b73039a7dde849dba190da59bbf48d09c67a8024d1d6e6a7c6a2
```

### Method 2

```bash
manlix@lab:~$ python3 -c 'import secrets; print(secrets.token_urlsafe(32))'
KLnBoCCUnyOUrfIGMEsUDK5kz5zmnc_ywRujmzjj56A
```

### Method 3

```bash
manlix@lab:~$ python3 -c 'import secrets, string; print("".join(secrets.choice(string.ascii_letters + string.digits) for i in range(32)))'
oEcuL1URZsLxWHmcOHf9ws1NUEeHSRJG
```
