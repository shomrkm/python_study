# -*- coding:utf-8 -*-

def careful_devide_1(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def careful_devide_2(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


# このやり方がベスト
# 戻り値をチェックする必要がなく、正当だと仮定して使用できる
def careful_devide_3(a, b):
    """ Divide a by b.

    Raise:
        ValueError: When the inputs cannot be divided.
    """
    try:
        return a / b
    except ValueError:
        raise ValueError('Invalid inputs')


x, y = 5, 2
try:
    result = careful_devide_3(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print(f'Result is {result:.1f}')
