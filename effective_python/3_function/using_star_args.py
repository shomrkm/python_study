# -*- coding:utf-8 -*-

def log(message, *values):
    if not values:
        print(message)
    else:
        value_str = ', '.join(str(x) for x in values)
        print(f'{message}: {value_str}')


log('My numbers', 1, 2)
log('Hi there')
