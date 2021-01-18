# -*- coding:utf-8 -*-

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for x in a:
    squares.append(x**2)
print(squares)

# リスト内表記
squares = [x**2 for x in a]
print(squares)

even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)

three_cubed_set = {x**3 for x in a if x % 3 == 0}
print(three_cubed_set)