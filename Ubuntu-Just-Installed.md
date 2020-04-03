# Install Ansible
```
# Update APT cache
manlix@lab:~$ sudo apt update


# Get Ansible version in repo (2.8.3)
manlix@lab:~$ apt-cache policy ansible
ansible:
  Installed: (none)
  Candidate: 2.8.3+dfsg-1
  Version table:
     2.8.3+dfsg-1 500
        500 http://ru.archive.ubuntu.com/ubuntu eoan/universe amd64 Packages
        500 http://ru.archive.ubuntu.com/ubuntu eoan/universe i386 Packages
        100 /var/lib/dpkg/status
        

# Install Ansible
manlix@lab:~$ sudo apt-get install -y --no-install-recommends ansible

# Check installed version
manlix@lab:~$ ansible --version | head -1
ansible 2.8.3
```

# Playbook (playbook.yml)
```yaml
---

- name: run the playbook tasks on the localhost
  hosts: localhost
  become: True

  vars:
    useful_soft:
      - apache2-utils  # To use load testing utility 'ab'
      - apt-file  # To look for package with given binary name program
      - curl
      - lm-sensors
      - python3-dev  # To prevent 'fatal error: Python.h: No such file or directory' during install some Python extensions
      - python3-distutils  # To prevent during creating venv: ModuleNotFoundError: No module named 'distutils.core'
      - python3-venv  # To install virtual env: python3 -m venv newvenv
      - tree
      - vim-nox
      - whois  # To get info about domains
      - xclip  # To copy output to clipboard (see: http://sandipbgt.com/2015/10/22/copy-text-to-clipboard-from-terminal-in-ubuntu/)

  tasks:

  - name: upgrade system
    apt:
      autoremove: True
      update_cache: True
      upgrade: dist
      cache_valid_time: 3600

  - name: install useful soft
    apt:
        name: "{{ useful_soft }}"
        update_cache: True
        cache_valid_time: 3600
```

# Run Ansible with related playbook

```
manlix@lab:~$ ansible-playbook -K -l localhost playbook.yml

# -K -- ask password for sudo
# -l localhost palybook.yml-- apply playbook 'playbook.yml' to 'localhost'
```
