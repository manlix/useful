# Install pyenv on Ubuntu 21.04


## Install dependencies
```bash
manlix@lab:~$ sudo apt-get update
```
```bash
manlix@lab:~$ sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev git
```

## Install pyenv

```bash
manlix@lab:~$ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

## Edit ~/.profile
Add these lines above all lines:
```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
```

## Edit ~/.bashrc
Add this line to the end:

```bash
eval "$(pyenv init -)"
```

## Check pyenv

```bash
manlix@lab:~$ pyenv --version
pyenv 2.0.1
```
---

Based on https://github.com/pyenv/pyenv/wiki
