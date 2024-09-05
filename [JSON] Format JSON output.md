Before:
```sh
manlix@lab:~$ docker image ls --digests --format json  | head -1 
{"Containers":"N/A","CreatedAt":"2024-08-01 17:23:55 +0300 MSK","CreatedSince":"4 weeks ago","Digest":"sha256:8a37d68f4f73ebf3d4efafbcf66379bf3728902a8038616808f04e34a9ab63ee","ID":"edbfe74c41f8","Repository":"ubuntu","SharedSize":"N/A","Size":"78.1MB","Tag":"24.04","UniqueSize":"N/A","VirtualSize":"78.05MB"}
```

After formatting:
```sh
manlix@lab:~$ docker image ls --digests --format json  | head -1 | python3 -m json.tool
{
    "Containers": "N/A",
    "CreatedAt": "2024-08-01 17:23:55 +0300 MSK",
    "CreatedSince": "4 weeks ago",
    "Digest": "sha256:8a37d68f4f73ebf3d4efafbcf66379bf3728902a8038616808f04e34a9ab63ee",
    "ID": "edbfe74c41f8",
    "Repository": "ubuntu",
    "SharedSize": "N/A",
    "Size": "78.1MB",
    "Tag": "24.04",
    "UniqueSize": "N/A",
    "VirtualSize": "78.05MB"
}
```
