# GIT


## Create TAR.GZ archvie from Git repository
```shell
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
