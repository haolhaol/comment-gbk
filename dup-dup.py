#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ���õݹ麯������׳�
# N! = 1 * 2 * 3 * ... * N
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print('���õݹ麯���ƶ���ŵ��:fact(1) =', fact(1))
print('���õݹ麯���ƶ���ŵ��:fact(5) =', fact(5))
print('fact(10) =', fact(10))

# ���õݹ麯���ƶ���ŵ��:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')