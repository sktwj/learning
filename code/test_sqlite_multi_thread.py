# -*- coding: utf-8 -*-
'''
sqlite multi-thread occured " Recursive use of cursors not allowed "

use thread lock can solve it
'''
import time
import random
import string
import sqlite3
import threading

# wiki     https://docs.python.org/zh-cn/2.7/library/sqlite3.html
lock = threading.Lock()

con = sqlite3.connect("test.db", isolation_level="IMMEDIATE", timeout=120, check_same_thread=False)
cursor = con.cursor()


def new():
    con.execute("create table person (id integer primary key, firstname varchar unique)")
    with con:
        con.execute("insert into person(firstname) values (?)", ("Joe",))

def get_name(index):
    name = "".join(random.choice(string.ascii_letters) for i in range(5))
    return "{}-{}".format(index, name)

def get_person(index):
    for i in range(1000):
        sql = "select count(*) from person where id = ?"
        #with lock:
        if 1:
            with con:
                row = con.execute(sql, (index, )).fetchone()
                print(row)

def add_person(index=None):
    for i in range(1000):
        if index == None:
            index = i
        name = get_name(index)
        sql = "insert into person(firstname) values (?)"
        '''
        with lock:
            try:
                cursor.execute(sql, (name,))
                con.commit()
            except:
                con.rollback()
                raise
        '''
        with lock:
            try:
                with con:
                    con.execute(sql, (name, ))
            except sqlite3.IntegrityError:
                print("could not add {}".format(name))


if __name__ == "__main__":
    try:
        new()
    except Exception as e:
        print("new error {}".format(e))
    for i in range(10):
        t = threading.Thread(target=add_person, args=(i,))
        #t = threading.Thread(target=get_person, args=(i,))
        t.start()
    add_person()