# React

## Install Node.js — 16 version

```console
manlix@lab:~$ sudo snap install node  --channel=16/stable --classic
```

## Check intalled versions:
```console
manlix@lab:~$ node --version
v16.8.0
manlix@lab:~$ npm --version
7.21.0
manlix@lab:~$ npx --version
7.21.0
manlix@lab:~$ yarn --version
1.22.5
```

## Create React empty project *hello-world* via `create-react-app`:
```console
manlix@lab:~$ cd tmp
manlix@lab:~/tmp$ npx create-react-app hello-world
...
manlix@lab:~/tmp$ cd hello-world
manlix@lab:~/tmp/hello-world$ tree -L 1
.
├── node_modules
├── package.json
├── public
├── README.md
├── src
├── yarn-error.log
└── yarn.lock

3 directories, 4 files
```

## Start project
```console
$ npm start

Compiled successfully!

You can now view hello-world in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://192.168.1.2:3000

Note that the development build is not optimized.
To create a production build, use yarn build
```

Open in web browser: http://localhost:3000
