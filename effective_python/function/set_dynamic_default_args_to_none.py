# -*- coding:utf-8 -*-

from time import sleep
from datetime import datetime


def log(message, when=datetime.now()):
    print(f'{when}] {message}')

# 以下は同じ時間になる。
# default 引数の datatime.now() が初回の一回しか評価されないため。
log('Hi there!')
sleep(0.1)
log('Hi again!')


# 以下のように実装すると意図した動作となる
def log2(message, when=None):
    """Log a message with a timestamp.

    Args：
        message：Message to print.
        when: datetime of when the message occurred.
            Defaults to the present time.
    """
    if when is None:
        when = datetime.now()
    print(f'{when}] {message}')

log2('Hi there!')
sleep(0.1)
log2('Hi again!')