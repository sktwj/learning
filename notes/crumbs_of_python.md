

## 1. python中装饰器更改__name__
1.1 使用functools.wrap()
```python
import functools
def set_func(func):
    @functools.wraps(func)
    def call_func(*args, **kwargs):
        print('xx')
        return func(*args, **kwargs)

    return call_func

```
1.2  使用__name__重新赋值
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
2.2.1 fromhex
```
bytes.fromhex('2Ef0 F1f2  ')
b'.\xf0\xf1\xf2'
```
2.2.2 hex 
```python
b'\xf0\xf1\xf2'.hex()
'f0f1f2'
```
### 2.3  [ 字符串格式化 ](https://docs.python.org/zh-cn/3/library/string.html#formatstrings )
- 元组、字典
```python
>>> coord = (3, 5)
>>> 'X: {0[0]};  Y: {0[1]}'.format(coord)
'X: 3;  Y: 5'
>>> a = A()
>>> a.cc = 123
>>> a.dd = 456
>>> "{0.dd} {0.cc}".format(a)
'456 123'
```
-  Replacing %s and %r:

```python
>>> "repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
"repr() shows quotes: 'test1'; str() doesn't: test2"
    
```
- 左右对齐 
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
- 进制
```python
>>> # format also supports binary numbers
>>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
>>> # with 0x, 0o, or 0b as prefix:
>>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'
```
- 千分逗号
```python
>>> '{:,}'.format(1234567890)
'1,234,567,890'
```
- 百分比
```python
>>> points = 19
>>> total = 22
>>> 'Correct answers: {:.2%}'.format(points/total)
'Correct answers: 86.36%'
```
- 特定时间格式
```python
>>> import datetime
>>> d = datetime.datetime(2010, 7, 4, 12, 15, 58)
>>> '{:%Y-%m-%d %H:%M:%S}'.format(d)
'2010-07-04 12:15:58'
```
- 复杂格式
```python
>>> for align, text in zip('<^>', ['left', 'center', 'right']):
...     '{0:{fill}{align}16}'.format(text, fill=align, align=align)
...
'left<<<<<<<<<<<<'
'^^^^^center^^^^^'
'>>>>>>>>>>>right'
>>>
>>> octets = [192, 168, 0, 1]
>>> '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
'C0A80001'
```




