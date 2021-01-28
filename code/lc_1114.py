import queue
import threading

def printFirst():
    print("first")

def printSecond():
    print("second")

def printThird():
    print("third")

class Foo(object):
    def __init__(self):
        self.c = threading.Condition()
        self.iii = 1



    def cc(val):
        def wrapper(func):
            def inner(self, print_func):
                #nonlocal self.iii
                with self.c:
                    self.c.wait_for(lambda:self.iii == val)
                    print_func()
                    self.iii += 1
                    self.c.notifyAll()
            return inner
        return wrapper

    @cc(1)
    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
    @cc(2)
    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """

        # printSecond() outputs "second". Do not change or remove this line.


    @cc(3)
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """



class TT:

    def t2(msg):
        def mid(func):
            def inner(*args, **kwargs):
                print("我在这里...", msg)
                return func(*args, **kwargs)
            return inner
        return mid


    @t2("握草！！！")
    def t1(self):
        pass

if __name__ == "__main__":
    #t = TT()
    #t.t1()
    ff = Foo()
    t1 = threading.Thread(target=ff.first, args=(printFirst,))
    t2 = threading.Thread(target=ff.second, args=(printSecond,))
    t3 = threading.Thread(target=ff.third, args=(printThird,))

    t3.start()
    t2.start()
    t1.start()