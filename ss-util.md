# ss util

# Looking for process is listening on port 8000

```shell
manlix@lab:~$ ss -4 -p -l "sport == 8000"
Netid                                       State                                        Recv-Q                                       Send-Q                                                                             Local Address:Port                                                                             Peer Address:Port                                      Process                                      
tcp                                         LISTEN                                       0                                            2048                                                                                     0.0.0.0:8000                                                                                  0.0.0.0:*                                          users:(("python3.10",pid=436917,fd=3),("uvicorn",pid=435347,fd=3))
```

It's **uvicorn** has runned by **python**:

```shell
manlix@lab:~$ readlink  /proc/436917/exe 
/home/manlix/.pyenv/versions/3.10.0/bin/python3.10
```
