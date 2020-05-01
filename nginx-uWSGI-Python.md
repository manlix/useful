**Dockerfile**
```
# Tags at Docker hub: https://hub.docker.com/_/python
FROM python:3.8.2-alpine3.11

# Place "truedoc" python package to this path on local filesystem
ARG TRUEDOC_PATH="/var/lib/truedoc"

RUN apk add uwsgi uwsgi-python3
COPY ./uwsgi/truedoc.ini /etc/uwsgi/

RUN mkdir -p ${TRUEDOC_PATH}
WORKDIR ${TRUEDOC_PATH}

# Copy required files to ${WORKDIR}
COPY ./requirements.txt .
COPY ./setup.py .

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r ${TRUEDOC_PATH}/requirements.txt && \
    python3 setup.py develop

EXPOSE 36456
CMD /usr/sbin/uwsgi --ini /etc/uwsgi/truedoc.ini

# Docs about "Dockerfile": https://docs.docker.com/engine/reference/builder/
```
**uwsgi/truedoc.ini**
```
; Options list: https://uwsgi-docs.readthedocs.io/en/latest/Options.html

[uwsgi]
module = truedoc.website:app

plugins = python3

; Workaround to prevent load packages from invalid place
python-path = /usr/local/lib/python3.8/site-packages/

uid = uwsgi
gid = uwsgi

master = true
processes = 5
threads = 2

; Remember that non-root user cannot bind to ports 1-1024
socket = [::]:36456
vacuum = true
```

**nginx**:
```
#############################
#
# Host: truedoc-app.localhost
#
#############################

server {

    listen truedoc-nginx:80;

    client_max_body_size 5M;  # Max allowed document filesize is 4M + some its stuff = (approx.) 5M

    server_name truedoc-app.localhost;

    location / {

        include uwsgi_params;

        uwsgi_pass uwsgi://truedoc-app:36456;  # port from uWSGI config "uwsgi/truedoc.ini"

        proxy_buffering on;
        proxy_buffers 12 12k;
        proxy_redirect off;

        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto https;
    }
}

```
