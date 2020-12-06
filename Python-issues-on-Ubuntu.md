# Solutions for Python related issues on Ubuntu

**JFYI**: before apply a solution: update APT cache
```
# Update APT cache
manlix@lab:~$ sudo apt update
```

## Problem: cannot create virtualenv

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

### Solution: install package **python3-venv** providing module **venv**

```
manlix@lab:~/venv$ sudo apt install -y python3-venv
```

## Problem: cannot run setup.py

```
manlix@lab:~/git/project$ python3 setup.py 
Traceback (most recent call last):
  File "setup.py", line 3, in <module>
    import setuptools
ModuleNotFoundError: No module named 'setuptools'
```

### Solution: install package python3-setuptools

```
manlix@lab:~$ sudo apt install python3-setuptool
```

## Problem: cannot install uWSGI via: python3 -m pip install uWSGI

```
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-install-sg47zmid/uWSGI/setup.py", line 117, in <module>
        setup(
      File "/usr/lib/python3.8/site-packages/setuptools/__init__.py", line 145, in setup
        return distutils.core.setup(**attrs)
      File "/usr/lib/python3.8/distutils/core.py", line 148, in setup
        dist.run_commands()
      File "/usr/lib/python3.8/distutils/dist.py", line 966, in run_commands
        self.run_command(cmd)
      File "/usr/lib/python3.8/distutils/dist.py", line 985, in run_command
        cmd_obj.run()
      File "/tmp/pip-install-sg47zmid/uWSGI/setup.py", line 77, in run
        conf = uc.uConf(get_profile())
      File "/tmp/pip-install-sg47zmid/uWSGI/uwsgiconfig.py", line 750, in __init__
        raise Exception("you need a C compiler to build uWSGI")
    Exception: you need a C compiler to build uWSG
```

### Solution: install C compiler

```
manlix@lab:~$ sudo apt install -y gcc
```

## Problem: cannot install python package

```
fatal error: Python.h: No such file or directory
```

### Solution : install development files

```
manlix@lab:~$ sudo apt install -y libpython3.8-dev
```

## Problem: 'fatal error: Python.h: No such file or directory'


### Solution: install Python headers files: install package 'python3-dev'

```
manlix@lab:~$ sudo apt install python3-dev
```
