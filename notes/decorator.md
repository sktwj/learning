
https://www.jb51.net/article/168276.htm

## 函数定时退出
```python
class TimeoutException(Exception):
    def __init__(self, error='Timeout waiting for response from Cloud'):
        Exception.__init__(self, error)


def timeout_limit(timeout_time):
    def wraps(func):
        def handler(signum, frame):
            raise TimeoutException()

        def deco(*args, **kwargs):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(timeout_time)
            func(*args, **kwargs)
            signal.alarm(0) # 关闭定时器
        return deco
    return wraps
```

## 保持原方法的属性
functools.wraps

```python

from functools import wraps
 
def wrapper(func):
    @wraps(func)
    def inner_function():
        pass
    return inner_function
 
@wrapper
def wrapped():
    pass
 
print(wrapped.__name__)
# wrapped
```

## 带参数的类装饰器

__init__ ：不再接收被装饰函数，而是接收传入参数。

__call__ ：接收被装饰函数，实现装饰逻辑。
```python

class logger(object):
  def __init__(self, level='INFO'):
    self.level = level
 
  def __call__(self, func): # 接受函数
    def wrapper(*args, **kwargs):
      print("[{level}]: the function {func}() is running..."\
        .format(level=self.level, func=func.__name__))
      func(*args, **kwargs)
    return wrapper #返回函数
 
@logger(level='WARNING')
def say(something):
  print("say {}!".format(something))
 
say("hello")
```

## 不带参数的类装饰器

__init__ ：接收被装饰函数

__call__ ：实现装饰逻辑。

```python
class logger(object):
  def __init__(self, func):
    self.func = func
 
  def __call__(self, *args, **kwargs):
    print("[INFO]: the function {func}() is running..."\
      .format(func=self.func.__name__))
    return self.func(*args, **kwargs)
 
@logger
def say(something):
  print("say {}!".format(something))
 
say("hello")
```