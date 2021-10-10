# pytest 


## Mark test requires Python 3.10+

```python3
import sys
import pytest

require_py310 = pytest.mark.skipif(sys.version_info < (3, 10), reason="Python 3.10+ is required")

@require_py310
def test_hello():
  assert "hello" == "hello"

```


## Do something if all tests completed successfully

Create `conftest.py` file in tests root directory with following data:

```python3
def do_something():
  print("All tests have been completed succesfully")

def pytest_sessionfinish(session, exitstatus):
    assert exitstatus == ExitCode.OK
    do_something()
```
