# Git

## Show detail config settings

* Like:
  * `user.name`
  * `user.email`
  * `core.editor`

```console
manlix@lab:~/git/b7$ git config --list --show-origin
...
file:/home/manlix/.gitconfig    user.email=username@example.com
file:/home/manlix/.gitconfig    user.name=User Name
file:/home/manlix/.gitconfig    core.editor=vim
...
```

## Set up config about name & email in current Git repository

```console
manlix@lab:~/git/b7$ git config user.name "User Name"
manlix@lab:~/git/b7$ git config user.email username@example.com
```

## Set up config about name & email (GLOBALLY)

```console
manlix@lab:~/git/b7$ git config --global user.name "User Name"
manlix@lab:~/git/b7$ git config --global user.email username@example.com
```


## Create TAR.GZ archvie from Git repository
```console
# Create archive
manlix@lab:~/PhpstormProjects/untitled3$ git archive -o archive.tar.gz HEAD

# list archive
manlix@lab:~/PhpstormProjects/untitled3$ tar -tf ./archive.tar.gz 
.gitattributes
README.md
composer.json
index.php
phpstan.neon.dist
phpunit.xml.dist
src/
src/HelloWorld.php
```

## Push an existing repository from the CLI
```console
$ git remote add origin git@github.com:LOGIN/PROJECT.git
$ git branch -M main
$ git push -u origin main
```
