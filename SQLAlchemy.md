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

Print:
```sql
SELECT      paid_services.id,
            paid_services.user_id,
            paid_services.service_id,
            paid_services.created_at,
            paid_services.expired_at 
FROM paid_services 
WHERE
        paid_services.user_id = :user_id_1
        AND
        paid_services.expired_at >= :expired_at_1
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

Print:
```sql
{
    'user_id_1': UUID('584307f1-f87d-44be-bb52-7574d409a192'),
    'expired_at_1': datetime.datetime(2021, 9, 24, 19, 46, 48, 958936)
}
```
