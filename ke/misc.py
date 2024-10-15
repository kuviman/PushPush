from math import *

def array2d(n, m, val):
    return [[val for j in range(m)]
            for i in range(n)]

def hsv(h, s, v, a=1):
    c = v*s
    h /= 60.0
    h %= 6.0
    x = c*(1-abs(h%2-1))
    if 0 <= h < 1:
        r, g, b = c, x, 0
    elif 1 <= h < 2:
        r, g, b = x, c, 0
    elif 2 <= h < 3:
        r, g, b = 0, c, x
    elif 3 <= h < 4:
        r, g, b = 0, x, c
    elif 4 <= h < 5:
        r, g, b = x, 0, c
    elif 5 <= h < 6:
        r, g, b = c, 0, x
    else:
        r, g, b = 0, 0, 0
    m = v-c
    return r+m, g+m, b+m, a

def clamp(x, a, b):
    if x < a:
        return a
    if x > b:
        return b
    return x

def sign(x):
    if x < 0:
        return -1
    if x > 0:
        return +1
    return 0

def lazy(f):
    f.d = {}
    def func(*args):
        if not f.d.has_key(args):
            f.d[args] = f(*args)
        return f.d[args]
    return func

def todo(func):
    print('TODO:', func.__name__)
    return func

def interl(a, b, k):
    return a+(b-a)*k

def inter(a, b, k):
    if k < 0.5:
        return a+2*(b-a)*k*k
    else:
        k = 1-k
        return b-2*(b-a)*k*k
