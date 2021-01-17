# -*- coding:utf-8 -*-

org = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a = org[:]

print(a[:])
print(a[:5])
print(a[:-1])
print(a[4:])
print(a[:-3])
print(a[2:5])
print(a[2:-1])
print(a[-3:-1])

# リストを置き換える
print('Before: ', a)
a[1:3] = [99, 22, 14]
print('After: ', a)
print('--------------------------')
a = org[:]

# リストに挿入する
print('Before: ', a)
a[1:1] = [99, 22, 14]
print('After: ', a)
print('--------------------------')

# 以下だとコピーではなく参照になる
b = a

