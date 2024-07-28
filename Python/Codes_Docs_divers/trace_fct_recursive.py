# -*- coding: utf-8 -*-
"""
Recursivity: showing fact execution
@author: nathalie
"""

import time

def trace(f, wait = 1.0):
    f.indent = 0
    def g(x):
        time.sleep(wait) 
        print('|   ' * f.indent + '|--', f.__name__, x, flush=True)
        f.indent += 1
        value = f(x)
        time.sleep(wait) 
        print('|   ' * f.indent + '|--', 'return', repr(value), flush=True)
        f.indent -= 1
        return value
    return g

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

fact = trace(fact,1.5)
