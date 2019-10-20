#!/usr/bin/env python
# coding=utf-8
import time
def consumer(name):
    print("%s 准备学习啦!" %name)
    while True:
       lesson = yield
 
       print("开始[%s]了,[%s]老师来讲课了!" %(lesson,name))
 
 
def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("同学们开始上课 了!")
    for i in range(10):
        time.sleep(1)
        print("到了两个同学!")
        c.send(i*2)
        c2.send(i*2)

producer('C')
