# -*- coding:utf-8 -*-

# 以下のようにジェネレータ関数の中で throw メソッドで
# 例外インスタンスを再度上げるという高度な機能があるが、避けたほうがよい

class MyError(Exception):
    pass

def my_generator():
    yield 1
    try:
        yield 2
    except MyError:
        print('Got Error!')
    else:
        yield 3

    yield 4

it = my_generator()
print(next(it))
print(next(it))
print(it.throw(MyError('test error')))


####################
# 以下は必要以上に読みづらい

class Reset(Exception):
    pass

def timer(period):
    current = period
    while current:
        current -= 1
        try:
            yield current
        except Reset:
            current = period

def check_for_reset():
    # 外部イベントをポーリングして待つ
    # :
    return False

def announce(remaining):
    print(f'{remaining} ticks remaining')

def run1():
    it = timer(4)
    while True:
        try:
            if check_for_reset():
                current = it.throw(Reset())
            else:
                current = next(it)
        except StopIteration:
            break
        else:
            announce(current)

run1()


####################
# クラスを使って Timer ジェネレータを定義したほうがわかりやすい

class Timer:
    def __init__(self, period):
        self.current = period
        self.period = period

    def reset():
        self.current = self.period

    def __iter__(self):
        while self.current:
            self.current -= 1
            yield self.current

def run2():
    timer = Timer(4)
    for current in timer:
        if check_for_reset():
            timer.reset()
        announce(current)

run2()

