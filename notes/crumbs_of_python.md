

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
#的作用: 在8进制前面显示0o  16进制前面显示0x

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

### 2.4 一些常识

- 空循环可利用好else
```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

- except
```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
 B
 C
 D 
```
请注意如果 except 子句被颠倒（把 except B 放到第一个），它将打印 B，B，B --- 即第一个匹配的 except 子句被触发。

-  Fibonacci 数列
```python
>>> def fib(n):    # write Fibonacci series up to n
...     """Print a Fibonacci series up to n."""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> # Now call the function we just defined:
... fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```
- python docstring

第一行应该是对象目的的简要概述。为简洁起见，它不应显式声明对象的名称或类型，因为这些可通过其他方式获得（除非名称恰好是描述函数操作的动词）。这一行应以大写字母开头，以句点结尾。

如果文档字符串中有更多行，则第二行应为空白，从而在视觉上将摘要与其余描述分开。后面几行应该是一个或多个段落，描述对象的调用约定，它的副作用等。

```python
>>> def my_function():
...     """Do nothing, but document it.
...
...     No, really, it doesn't do anything.
...     """
...     pass
...
>>> print(my_function.__doc__)
Do nothing, but document it.

    No, really, it doesn't do anything.
```

- 函数标注

```python
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```

- 函数的默认值

函数的默认值只会执行一次，这条规则在默认值为可变对象（列表、字典以及大多数类实例）时很重要。
```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

[1]
[1, 2]
[1, 2, 3]
```
如果你不想要在后续调用之间共享默认值，你可以这样写这个函数:
```python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```
- 集合set操作

```python
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```
- 模块导入

出于效率的考虑，每个模块在每个解释器会话中只被导入一次。因此，如果你更改了你的模块，则必须重新启动解释器， 或者，如果它只是一个要交互式地测试的模块，请使用 importlib.reload()，例如 import importlib; importlib.reload(modulename)。

- 格式字符串
```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```

- 类内私有变量
```python
由于存在对于类私有成员的有效使用场景（例如避免名称与子类所定义的名称相冲突），因此存在对此种机制的有限支持，称为 名称改写。 任何形式为 __spam 的标识符（至少带有两个前缀下划线，至多一个后缀下划线）的文本将被替换为 _classname__spam，其中 classname 为去除了前缀下划线的当前类名称。 这种改写不考虑标识符的句法位置，只要它出现在类定义内部就会进行。

名称改写有助于让子类重载方法而不破坏类内方法调用

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
            
上面的示例即使在 MappingSubclass 引入了一个 __update 标识符的情况下也不会出错，因为它会在 Mapping 类中被替换为 _Mapping__update 而在 MappingSubclass 类中被替换为 _MappingSubclass__update。
```
- python 类单例模式

```python

def singleton(cls, *args, **kwargs):
    instance = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    
    return get_instance
       

```

- contextmanager

```python
class MyResource:

    def query(self):
        print("query data..")

from contextlib import contextmanager

@contextmanager
def get_resource():
    print("connect db..")
    yield MyResource()
    print("disconnect db..")

with get_resource() as r:
    r.query()
    


```

- from operator import itemgetter, attrgetter

```python
After f = itemgetter(2), the call f(r) returns r[2].

After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3]).
After f = attrgetter('name'), the call f(b) returns b.name.

After f = attrgetter('name', 'date'), the call f(b) returns (b.name, b.date).

After f = methodcaller('name'), the call f(b) returns b.name().

After f = methodcaller('name', 'foo', bar=1), the call f(b) returns b.name('foo', bar=1).

```

- 多条件排序

```python
>>> student_objects = [
...     Student('john', 'A', 15),
...     Student('jane', 'B', 12),
...     Student('dave', 'B', 10),
... ]

def multisort(xs, specs):
...     for key, reverse in reversed(specs):
...         xs.sort(key=attrgetter(key), reverse=reverse)
...     return xs
 multisort(list(student_objects), (('grade', True), ('age', False)))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

```


- functools.lru_cache(maxsize=128, typed=False)

```python
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

>>> [fib(n) for n in range(16)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

>>> fib.cache_info()
CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)
```

- __getattr__ 和 __getattribute__

```python
__getattr__()与__getattribute__()
这两个是类对象的魔法函数，在访问对象属性的时候会被调用，但是两者之间也有一点区别, 我们通过代码来看一下:

class A(object):
  def __init__(self, x):
    self.x = x

  def hello(self):
    return 'hello func'

  def __getattr__(self, item):
    print('in __getattr__')
    return 100

  def __getattribute__(self, item):
    print('in __getattribute__')
    return super(A, self).__getattribute__(item)

a = A(10)
print(a.x)
print(a.y)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
运行代码，得到下面输出:

in __getattribute__
10
in __getattribute__
in __getattr__
100
1
2
3
4
5
可以看出，在获到对象属性时，__getattribute__()是一定会被调用的，无论属性存不存在，首先都会调用这个魔法方法。

如果调用像a.y这种不存在的对象时，调用__getattribute__()找不到y这个属性，就会再调用__getattr__()这个魔法方法，可以通过在这个方法里实来设置属性不存在时的默认值。使用上面的getattr()方法获取属性时，也是同样的调用关系，只不过只有在getattr()带第三个参数作为默认值时，才会调用
__getattr__()方法。
```
使用__getattr__能大幅简化代码。Why we use python，life is short。


### 2.5 python 解释器中方向键乱码

    sudo apt install libreadline-dev
    then reinstall this python version
    
### 单例脚本

from tendo.singleton import SingleInstance
在main 中
me = SingleInstance()


### 装饰器 检测 function 参数类型  

```python
def checked(func):
    ann = func.__annotations__
    sig = inspect.signature(func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            if name in ann:
                assert isinstance(val, ann[name]), f'Excepted {ann[name]}'

        return func(*args, **kwargs)
    return wrapper

@checked
def gcd(a:int, b:int) -> int:

    return a + b

```


### pyenv install python

```bash
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
    
```


### 简易进度条
```python

from tqdm import tqdm
import time

for i in tqdm(range(1000)):
    time.sleep(.01)
```