#!/usr/bin/env python
#coding:utf-8

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