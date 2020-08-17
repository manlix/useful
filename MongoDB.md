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

## [Documents]

### Select all documents
```
db.inventory.find( {} )
```

### Select all documents in pretty format
```
db.inventory.find( {} ).pretty()
```


### Select documents with existing field 'item'
```
db.inventory.find( { item: { $exists: true } } )
```

### Select documents with non-existing field 'item'
```
db.inventory.find( { item: { $exists: false } } )
```

### Select documents with field 'item' = "hello"

```
db.inventory.find( { item: "hello" } )
```
