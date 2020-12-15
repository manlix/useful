# Python generators

## Receive generator

```python
def receive_gen():
    return_var = 'I am return variable'  # Returns during 'g.send(None)'
    msg = yield return_var  # Income value passed to 'msg'
    print(msg)


g = receive_gen()
print(g.send(None))
g.send('Hello world')
```

Output:
```python
I am return variable
Hello world
Traceback (most recent call last):
  File "./receive-gen.py", line 11, in <module>
    g.send('Hello world')
StopIteration
```

## Simple generator

```python
def simple_gen():
    yield 'Hello world'

for i in simple_gen():
    print(i)
```

Output:
```python
Hello world
```

## Simple infinity generator with random integer

```python
import time
from random import randint

def simple_infinity_gen():
    while True:
        yield f'Random: {randint(10, 99)}\n'
        print('Press [CTRL]+[C] to stop infinity loop...')
        time.sleep(0.3)

for i in simple_infinity_gen():
    print(i)
```

Output:
```python
Random: 66

Press [CTRL]+[C] to stop infinity loop...
Random: 73

Press [CTRL]+[C] to stop infinity loop...
Random: 69

Press [CTRL]+[C] to stop infinity loop...
^CTraceback (most recent call last):
  File "./simple_gen.py", line 10, in <module>
    for i in simple_infinity_gen():
  File "./simple_gen.py", line 8, in simple_infinity_gen
    time.sleep(0.3)
KeyboardInterrupt
```
