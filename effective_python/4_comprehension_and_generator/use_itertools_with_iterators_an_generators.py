# -*- coding:utf-8 -*-

import itertools

# chain
# 複数のイテレータを組み合わせて1つのシーケンスにする
it = itertools.chain([1, 2, 3], [4, 5, 6])
print(list(it))

# repeat
# 1つの値を何回も出力したり、第2引数で指定した最大繰り返し回数で出力する
it = itertools.repeat('hello', 3)
print(list(it))

# cycle
# イテレータの要素を何回も繰り返す
it = itertools.cycle([1,2])
result = [next(it) for _ in range(10)]
print(result)

# tee
# 1つのイテレータを分割して第2引数で指定した複数の並列イテレータにする
it1, it2, it3 = itertools.tee(['first', 'second'], 3)
print(list(it1))
print(list(it2))
print(list(it3))

# zip_longest
# zip 時に長さが異なるイテレータの場合にイテレータが終了したらプレースホルダ値を返す
keys = ['ones', 'two', 'three']
values = [1, 2]
normal = list(zip(keys, values))
print('zip: ', normal)

it = itertools.zip_longest(keys, values, fillvalue='nope')
longest = list(it)
print('zip_longest: ', longest)

# islice
# 複製せず、インデックスでイテレータをスライスする
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_five = itertools.islice(values, 5)
print('First Five: ', list(first_five))

middle_odds = itertools.islice(values, 2, 8, 2)
print('Middle odds: ', list(middle_odds))

# takewhile
# 述語関数が False を返すまで、イテレータの要素を返す
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7
it = itertools.takewhile(less_than_seven, values)
print(list(it))

# dropwhile
# 述語関数が最初に True を返すまで、イテレータは要素をスキップする
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7
it = itertools.dropwhile(less_than_seven, values)
print(list(it))

# filterfalse
# 述語関数が False になるイテレータの全要素を返す
# (filter の逆)
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = lambda x: x % 2 == 0

filter_result = filter(evens, values)
print('Filter:       ', list(filter_result))

filter_false_result = itertools.filterfalse(evens, values)
print('Filter false: ', list(filter_false_result))

# accumulate
# 2引数関数をイテレータの返す値に適用していき進行値を作る
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_reduce = itertools.accumulate(values)
print('Sum: ', list(sum_reduce))

def sum_modulo_20(first, second):
    output = first + second
    return output % 20

modulo_reduce = itertools.accumulate(values, sum_modulo_20)
print('Sum: ', list(modulo_reduce))

# product
# 1つ以上のイテレータから要素の直積を返す
# 入れ子の深い内包表記を使う代わりとして適している
single = itertools.product([1, 2], repeat=2)
print('Single: ', list(single))
multiple = itertools.product([1, 2], ['a', 'b'])
print('Multiple: ', list(multiple))

# permulations
# イテレータからN個の要素を取り出してできる順列を返す
it = itertools.permutations([1, 2, 3, 4], 2)
print(list(it))

# combinations
# イテレータからN個の要素を取り出したときに可能となる全ての組み合わせを順不同で返す
it = itertools.combinations([1, 2, 3, 4], 2)
print(list(it))

# combinations_with_replacement
# combinations とほぼ同じだが、取り出した要素を元に戻す形式で同じ要素の反復を許す
it = itertools.combinations_with_replacement([1, 2, 3, 4], 2)
print(list(it))
