#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Maratrix Lee'

import os


def read_demo(filename):
    with open(filename) as f:
        f = open(filename, 'rb')
        print('readable:', f.readable())
        con = f.read()
        con = str(con.decode('utf-8')).splitlines()
        con.reverse()
        print(con)
    
    f = open(filename, 'r')
    while True:
        line = str(f.readline()).strip()
        if line == '' or line.isspace():
            print('end', line.isspace(), line.encode('utf-8'))
            break
        print(line)
    f.close()

    with open(filename) as f:
        lines = f.readlines()
        print(lines)
        print(list(map(lambda l: str(l).rstrip(), lines)))

    with open(filename, 'r') as f:
        for line in f:
            print(line, end = '')
    
    try:
        f = open(filename, 'r')
    except IOError as err:
        print(err)
    finally:
        if f: f.close()
        


def write_demo(filename):
    with open(filename, 'w+') as ff:
        con = 'hello\nworld'
        
        n = ff.write(con)
        print('write: ', n)

        ff.seek(0)
        r = ff.read()
        print('read: ', r.encode('utf-8'), ' seek: ', ff.tell(), ' filename: ', ff.name)

    
def truncate_demo(filename):
    with open(filename, 'r+') as ff:
        ff.seek(4)
        ff.truncate()
        print(ff.readlines())

if __name__ == '__main__':
    try:
        # print([d for d in os.listdir()])
        read_demo('./data.txt')
        # write_demo('./data_r.txt')
        # truncate_demo('./data.txt')
    except FileNotFoundError as ve:
        print(ve)
    else:
        print('no error')