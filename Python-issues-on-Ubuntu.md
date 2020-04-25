# Solutions for Python related issues on Ubuntu

**Problem**: cannot create virtualenv

```
manlix@lab:~/venv$ python3 -m venv ./test
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt-get install python3-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: ['/home/manlix/venv/test/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']
```

**Solution**: install related package **python3-venv** providing module **venv**

```
manlix@lab:~/venv$ sudo apt install -y python3-venv
```
