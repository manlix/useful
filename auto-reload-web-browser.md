# Automatically reload browser when files in specified directory change

Started on `http://localhost:3000` by default

Monitor `all files` inside specified directory:
```
manlix@homepc:~/git/microblog$ sudo apt install -y npm
manlix@homepc:~/git/microblog$ npx browser-sync start --proxy "localhost:5000" --no-open --files "**/*"
```

Monitor changes to `*.html` and `*.py` files only:
```
manlix@homepc:~/git/microblog$ npx browser-sync start --proxy "localhost:5000" --no-open --files "**/*.py,**/*.html" --logLevel
 info
```

`--no-open ` -- do not open web browser automatically

`All commands for CLI` -- https://browsersync.io/docs/command-line
