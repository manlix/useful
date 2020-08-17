# MongoDB (shell)

## [Databases]

### List databases
```
show dbs
```

### Switch to necessary database
```
use anotherdb
```

### Current database
```
db
```

## [Collections]

### Show collections in current database
```
show collections
```

### Drop collection COLLECTION_NAME in current database
```
db.COLLECTION_NAME.drop()
```

### Drop collection with dot in its name
```
db["COLLECTION.NAME"].drop()
```
