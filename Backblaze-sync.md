# Backblaze (some tips)


# Install b2 client
```
$ pip install b2
```

# Authorize
```
$ b2 authorize-account
```

# List keys on b2 side
```
$ b2 list-keys
```

# List buckets
```
$ b2 list-buckets
```

# Sync with dry-run only
```
$ b2 sync --dryRun . b2://target-dir-on-b2
```

# Sync with b2 with threads=10
```
$ b2 sync --threads=10 . b2://target-dir-on-b2
```

# Delete remote dir on b2:
```
$ b2 sync --allowEmptySource --delete . b2://target-dir-on-b2
```

# Delete remote bucket
```
$ b2 delete-bucket remove-this-remote-bucket
```

