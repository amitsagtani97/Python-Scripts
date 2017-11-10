## Decorators...decorators everywhere.

### Collection of useful decorators.

##### [retry decorator](https://github.com/amitsagtani97/Python-Scripts/decorators/retry_decorator.py)
Each time the decorated function throws an exception, the decorator will wait a period of time and retry calling the function until the maximum number of tries is used up. If the decorated function fails on the last try, the exception will occur unhandled.

Example usage:

```python
@retry(Exception, tries=4)
def test_success(text):
    print "Success: ", text

test_success("it works!")
```

```python
import random

@retry(Exception, tries=4)
def test_random(text):
    x = random.random()
    if x < 0.5:
        raise Exception("Fail")
    else:
        print "Success: ", text

test_random("it works!")
```
