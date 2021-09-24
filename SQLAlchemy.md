# SQLAlchemy examples

## Get query statement

```python
query = db.query(
            models.PaidService,
        ).filter(
            models.PaidService.user_id == user.user_id,
            models.PaidService.expired_at >= datetime.utcnow()
        )

print(query.statement)
```

## Get query params

```python
query = db.query(
            models.PaidService,
        ).filter(
            models.PaidService.user_id == user.user_id,
            models.PaidService.expired_at >= datetime.utcnow()
        )

print(query.statement.compile().params)
```
