# Flask

Original sources about Application and Request contexts in Flask are:
* https://testdriven.io/blog/flask-contexts/
* https://testdriven.io/blog/flask-contexts-advanced/

## Bind to Application context

### Without a context manager

```python3
from app import app
from flask import current_app

app_ctx = app.app_context()
app_ctx.push()

print(current_app.config['ENV'])  # 'production'

app_ctx.pop()
```

### With a context manager

```python3
from app import app
from flask import current_app

with app.app_context():
  print(current_app.config['ENV'])  # 'production'
```

## Bind to Request context

### Without a context manager

```python3
from app import app
from flask import request

request_ctx = app.test_request_context()
request_ctx.push()

print(request.method)  # 'GET'
print(request.path)  # '/'

request_ctx.pop()
```

### With a context manager

```python3
from app import app
from flask import current_app

with app.test_request_context('/'):
  print(request.method)  # 'GET'
  print(request.path)  # '/'
```
