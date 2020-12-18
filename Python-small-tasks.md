# Python small tasks

## There are all given words in article

```python
from collections import Counter

def check_words(article: str, text: str) -> bool:
    
    text = text.split(" ")
    article = article.split(" ")
    
    if Counter(text) - Counter(article):
        return False

    return True

# check_words("ARTICLE", "W O R D S")
check_words("Welcome to our ship! Hello world 123 123", "Hello world 123")  # True
check_words("Welcome to our ship! Hello world 123 123", "Hello world 123 123")  # True
check_words("Welcome to our ship! Hello world 123 123", "Hello world 123 123 123")  # False
```
