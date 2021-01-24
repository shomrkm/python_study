# -*- coding:utf-8 -*-

# e.g. 画面表示プログラムでジェネレータを使ってイメージの動きをアニメーション示すプログラム

def move(period, speed):
    for _ in range(period):
        yield speed

def pause(delay):
    for _ in range(delay):
        yield 0

def animate():
    # yield from はループと yield 式を Python インタプリタで使う決り文句
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(2, 3.0)

def render(delta):
    print(f'Delta: {delta:.1f}')
    # イメージをスクリーン上で動かす

def run(func):
    for delta in func():
        render(delta)
    
run(animate)



################################
# yield from を使ったほうが性能も上がる
# 以下はベンチマーク

import timeit

def child():
    for i in range(1_000_000):
        yield i

def slow():
    for i in child():
        yield i

def fast():
    yield from child()

baseline = timeit.timeit(
    stmt='for _ in slow(): pass',
    globals=globals(),
    number=50
)
print(f'Manual nesting {baseline:.2f}s')

comparison = timeit.timeit(
    stmt = 'for _ in fast(): pass',
    globals=globals(),
    number=50
)
print(f'Composed nesting {comparison:.2f}s')

reduction = -(comparison - baseline) / baseline
print(f'{reduction:.1%} less time')

