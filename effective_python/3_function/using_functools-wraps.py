# -*- coding:utf-8 -*-

def trace1(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
            f'-> {result!r}')
        return result
    return wrapper


# デコレータで関数をラップする

@trace1
def fibonacci1(n):
    """ Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci1(n-2) + fibonacci1(n-1))

# @trace は以下と等価
#fibonacci = trace(fibonacci)

fibonacci1(4)

# 問題点
#   関数名が fibonacci ではなく、wrapper 返してしまう
#   help も docstring を返してくれない
print(fibonacci1)
help(fibonacci1)


# 解決法
#   functools の wrap ヘルパー関数を使う



from functools import wraps

def trace2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
            f'-> {result!r}')
        return result
    return wrapper


@trace2
def fibonacci2(n):
    """ Return the n-th Fibonacci number """
    if n in (0, 1):
        return n
    return (fibonacci2(n-2) + fibonacci2(n-1))

print(fibonacci2)
help(fibonacci2)
