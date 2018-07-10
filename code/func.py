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