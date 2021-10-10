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
