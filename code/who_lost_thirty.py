# -*- coding: utf-8 -*-

'''
岳云鹏 谁先数到30的二人游戏
1. 从1开始，每人每次可说1或2个数
2. 谁先说30谁输
小红 会尽力让你输掉
'''
import sys


class Player:
    def __init__(self):
        self.current = 1
        self.numed = []

    def reply(self):
        msg = []
        a, b = self.current+1, self.current+2
        msg.append(a)
        if b % 3 != 0:
            msg.append(b)
        self.numed += msg
        print("小红: {}".format(msg))

    def feed(self, num):
        if num not in self.numed:
            self.numed.append(num)
            self.current = num
            self.reply()
        elif self.numed and num not in (self.numed[-1]+1, self.numed[-1]+2):
            raise ValueError("越界了")
        else:
            raise ValueError("重复输入")

if __name__ == "__main__":
    p = Player()
    print("hello, 小明")
    while True:
        try:
            nums = input("小明: ").replace(",", " ")
            nums = nums.split()
            if len(nums) > 2:
                raise ValueError("最多说2个数")
            num = int(nums[-1])
            if num > 30:
                print("小明: 1")
                num = 1
            p.feed(num)
        except KeyboardInterrupt:
            print("bye！")
            sys.exit(0)
        except ValueError as e:
            print("非法输入-{},当前 {}".format(e, p.numed))
            continue
        except:
            print("输入错误，请重新输入")



