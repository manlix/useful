# pytest 


## Mark test requires Python 3.9+

```python3
import pytest

require_py39 = pytest.mark.skipif(sys.version_info < (3, 9), reason="Python 3.9+ is required")

@require_py39
def test_hello():
  assert "hello" == "hello"

```
