

## 1. python中装饰器更改__name__
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

## 2. python 语法

### 2.1 字符串中的回车换行会自动包含到字符串中，如果不想包含，在行尾添加一个 \ 即可
### 2.2 bytes 对象 
1. fromhex
```
bytes.fromhex('2Ef0 F1f2  ')
b'.\xf0\xf1\xf2'
```
2. hex 
```python
b'\xf0\xf1\xf2'.hex()
'f0f1f2'
```
### 2.3 字符串格式化
1.
```python
>>> coord = (3, 5)
>>> 'X: {0[0]};  Y: {0[1]}'.format(coord)
'X: 3;  Y: 5'
```
2. Replacing %s and %r:

```python
>>> "repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
"repr() shows quotes: 'test1'; str() doesn't: test2"
    
```
3. 
```python
>>> '{:<30}'.format('left aligned')
'left aligned                  '
>>> '{:>30}'.format('right aligned')
'                 right aligned'
>>> '{:^30}'.format('centered')
'           centered           '
>>> '{:*^30}'.format('centered')  # use '*' as a fill char
'***********centered***********'
```





