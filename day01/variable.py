#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv, path

print(argv, path)

print('hello world')

def hello():
    '''这里是文档'''
    print('hello func')

print(hello.__doc__)
