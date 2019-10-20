#!/usr/bin/env python
# coding=utf-8
#列表生成式
lis = [x*x for x in range(10)]
print(lis)
#生成器
generator_ex = (x*x for x in range(10))
print(generator_ex)
for i in generator_ex:
    print(i)
    
print("-"*40)
def fib(max):
    n,a,b =0,0,1
    while n < max:
        a,b =b,a+b
        n = n+1
        print(a)
    return 'done'
 
#a = fib(10)
#print(fib(10))    

def fib1(max):
    n,a,b =0,0,1
    while n < max:
        yield b
        a,b =b,a+b
        n = n+1
#        print(a)
#    return 'done'
aa = fib1(10)
print(aa.__next__())
