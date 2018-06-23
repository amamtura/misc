#!/usr/bin/env python

# 0 1 1 2 3 5 8 13 21 ...

def fibonacciGenerator():
    a=0
    b=1
    while True:
        yield a
        a, b = b, a + b

fg = fibonacciGenerator()
for i in range(15):
    print(next(fg)),

