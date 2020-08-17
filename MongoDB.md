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


### Documents with existing field 'item'
```
db.inventory.find( { item: { $exists: true } } )
```

### Documents with non-existing field 'item'
```
db.inventory.find( { item: { $exists: false } } )
```

### Documents where field 'item' = "hello"
```
db.inventory.find( { item: "hello" } )
```

### Documents where field 'status' = "D" and field 'qty' = 0
```
db.inventory.find( { status: "D", qty: 0 } )
```

### Documents where the 'uom' field is nested inside the 'size' document and equals "in"
```
db.inventory.find( { "size.uom": "in" } )
```

### Documents where the tags array contains "red" as one of its elements
```
db.inventory.find( { tags: "red" } )
```

### Documents where the tags field matches the specified array exactly, including the order
```
db.inventory.find( { tags: [ "red", "blank" ] } )
```
