

### 1. python中装饰器更改__name__
方法1 使用functools.wrap()
```python
import functools
def set_func(func):
    @functools.wraps(func)
    def call_func(*args, **kwargs):
        print('xx')
        return func(*args, **kwargs)

    return call_func

```
方法2  使用__name__重新赋值
````python
def set_func(func):
    def call_func(*args, **kwargs):
        print('xx')
        return func(*args, **kwargs)

    call_func.__name__ = func.__name__
    return call_func


````