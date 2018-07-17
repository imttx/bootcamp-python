#!/usr/bin/env python
#coding:utf-8

from functools import reduce

def say_hello(name, age = 18):
    print('name is: ', name, '，age is:', age)

say_hello('maratrix', 18)

say_hello(age = 20, name='Monica')

say_hello('Monica')

def add_list(l = []):

    l.append('end')
    print(l)

def more_params(**params):
    print(params)

more_params(name = 'hanson', age = 18)

d = {'name':'Maratrix', 'hobby': 'python', 'sex':'male'}

more_params(**d)

def person(name, age, *, city, job = 'it...', **kw):
    print(name, age, city, job, kw)

person('hanson', 18, city = 'BJ', adr = 'beijing')

def foo(a, b, c=0, *args, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'd =', d, 'kw =', kw)

foo(*[1, 2, 3, 4, 5], **{'d':'dd', 'e':'ee', 'f':'ff'})



sum = lambda a, b: a + b

print(sum(1, 2))
print(sum(3, 4))

li = [lambda :x for x in range(10)]

print(li, type(li))
print(type(li[0]))

for k, v in {1:11, 2:22}.items():
    print(k, v)

for k, v in enumerate([1,2,3]):
    print(k, v)


# ----------------------


def odd(max_num = 10):
    n = 0

    while n <= max_num:
        yield n**2
        n+=1

    return 'done'

o = odd(5)

print(type(o))

# try:
#     # for x in o:
#         # print(x)
#     print(next(o))
# except StopIteration as e:
#     print('yield return:', e.value)


while True:
    try:
        print(next(o))
    except StopIteration as e:
        print(e.value)
        break

def foo1():
    yield 1
    yield 2


f = foo1()

# print(next(f))
# print(next(f))
# print(next(f))

for x in f:
    print(x)


f = foo1()

print(type(f))
print(next(f))
print(next(f))

# ????

digits_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(x):
    return digits_map[x]


res = reduce(lambda x, y: x * 10 + y, map(lambda x: int(x), '123456'))

print(res, type(res))

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n

        return ax
    return sum

s = lazy_sum(1,2,3,4,5)

# print(s())

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i**2
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1(), f2(), f3())

def get_func():
    return lambda x, y: x**y

ff = get_func()

print(ff(5, 2))