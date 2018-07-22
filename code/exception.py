#!/usr/bin/env python
# -*- coding:utf-8 -*-

'demo code...'

__author__ = 'maratrix'

import sys
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

def demo1():
    try:
        # print('...BEGIN...')
        print(int('a10'))
    except Exception as e:
        print(e)
        # logging.exception(e)
    # else:
    #     print('no error')
    # finally:
    #     print('...END...')

def demo2():
    with open('111.txt') as ff:
        print(ff.read())
    
    print(ff.closed)


if __name__ == '__main__':
    demo2()