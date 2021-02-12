#decorator2.py

from time import ctime, sleep
import os,yaml
import random

def timefun_arg(pre="hello"):
    def timefun(func):
        def wrappedfunc():
            print("%s called at %s %s"%(func.__name__, ctime(), pre))
            return func()
        return wrappedfunc
    return timefun

@timefun_arg("itcast")
def foo():
    print("I am foo")

@timefun_arg("python")
def too():
    print("I am too")

# 1, 1, 2, 3, 5, 8, 13, 21, 34

def lis(arr):

    for i in range(len(arr)-1):
        print('10')
        x=arr[i]+arr[i+1]
        yield x
        print('20')
    return x

def sums(arr):
    sum=0
    for i in range(len(arr)):
        print(len(arr),arr[i])
        sum+=arr[i]
    return sum

if __name__ == '__main__':
    lists =[1, 1, 2, 3, 5]
    data={'id': 341402, 'title': '居巢区'}
    test=os.path.join(os.path.dirname(__file__),'test.yaml')
    with open(test,'r') as a:
        config=yaml.safe_load(a)
    print(config['database'])
    print(config['database1'])
