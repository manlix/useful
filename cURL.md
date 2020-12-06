# Upload file via cURL

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
