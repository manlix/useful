### Celery

### Run task with specific id

```python3
task.apply_async(task_id="my-custom-task-id")
```


## Chain
### Current chain state:
```python3
def chain_current_state(chain_id):
    for task_id in chain_id.as_list():
        if AsyncResult(task_id).state != "PENDING":
            return AsyncResult(task_id).state
```

### Current chain result:
```python3
def chain_current_state(chain_id):
    for task_id in chain_id.as_list():
        if AsyncResult(task_id).state != "PENDING":
            return AsyncResult(task_id).info
```

### Chaining several tasks:

```python3
from celery import chain
from celery.result import AsyncResult

c = chain(tasks.task1.s(), tasks.task2.s())
res = c.apply_async()

res.as_list())  # ['fc23f3ec-dfcf-4242-b750-b7a49870754b', 'ec3a6f1b-5c3d-4eef-a675-bd45c12e557c']
chain_current_state(res)  # 'COUNTING'
chain_current_value(res)  # {'value': 50}
```
