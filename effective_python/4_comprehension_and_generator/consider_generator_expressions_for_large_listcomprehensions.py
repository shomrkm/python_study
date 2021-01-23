# -*- coding:utf-8 -*-

# my_numbers.txt が巨大なファイルだと膨大なメモリを消費してしまう
value = [len(x) for x in open('reference\\my_numbers.txt')]
print(value)

# ジェネレータ式でイテレータを返す
it = (len(x) for x in open('reference\\my_numbers.txt'))
print(next(it))
print(next(it))

# 上のジェネレータ式からかえされたイテレータ(it)を使って、
# 別のジェネレータへの入力にする
roots = ((x, x**0.5) for x in it)
# このイテレータ(roots)を1つ進めるごとに内部のイテレータ(it)も1つ進み、ループする
print(next(roots))
print(next(roots))
