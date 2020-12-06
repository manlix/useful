# cURL

## Upload file

```
manlix@lab:~$ curl -v -F title="document title" -F document=@/home/manlix/tmp/1M http://localhost/document/
```

Where:
```
# -v -- verbose
# -F title -- text field "title" with value "document title"
# -F document=@/home/manlix/tmp/1M -- field 'document' with file data '/home/manlix/tmp/1M' to upload
# http://localhost/document/ -- endpoint to upload
```

## Fetch the headers only

```
manlix@lab:~$ curl -I https://nginx.org
HTTP/1.1 200 OK
Server: nginx/1.15.7
Date: Sat, 17 Aug 2019 18:53:51 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 9868
Last-Modified: Thu, 15 Aug 2019 17:07:12 GMT
Connection: keep-alive
Keep-Alive: timeout=15
ETag: "5d559140-268c"
Accept-Ranges: bytes
```
