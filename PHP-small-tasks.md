# PHP small tasks

## Task about square brackets

```php
<?php

declare(strict_types=1);

function square_brackets(string $str): bool
{

    $stack = new SplStack();

    foreach (str_split($str) as $item) {

        if ($item == '[') {
            $stack->push('[');
        } else {

            if ($stack->isEmpty() || $stack->pop() != '[') {
                return false;
            }
        }
    }

    if ($stack->isEmpty()) {
        return true;
    }

    return false;
}

var_dump(square_brackets('[]')); // true
var_dump(square_brackets('[]]')); // false
var_dump(square_brackets('[[[[[[]]]]]]')); // true
```
