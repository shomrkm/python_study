# -*- coding:utf-8 -*-

# C Style
a = 0b10111011
b = 0xc5f
print('Binary is %d, hex is %d' % (a, b))

print('==========================================')


# Python3 Style
a = 1234.5678
formatted = format(a, ',.2f')  # ","で3桁で区切る
print(formatted)

b = 'my string'
formatted = format(b, '^20s')  # "^" でセンタリング
print('*', formatted, '*')

key = 'my_var'
value = 1.234
formatted = '{} = {}'.format(key, value)
print(formatted)
formatted = '{0} = {1}'.format(key, value)
print(formatted)
formatted = '{:<10} = {:.2f}'.format(key, value)
print(formatted)

print('==========================================')


# Python3.6 format string
key = 'my_var'
value = 1.234
formatted = f'{key} = {value}'
print(formatted)
formatted = f'{key!r:<10} = {value:.2f}'
print(formatted)

pantry = [
    ('avocados', 1.25),
    ('bananas', 2.5),
    ('cherries', 15)
]
for i, (item, count) in enumerate(pantry):
    f_string = f'#{i+1}: {item.title():<10s} = {round(count)}'
    print(f_string)


# Note:
#  str.title() : 単語の先頭の一文字を大文字、他を小文字に変換
#  round : 数値の丸め込み(正確な四捨五入にはならにので注意)
