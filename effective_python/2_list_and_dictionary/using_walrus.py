# -*- coding:utf-8 -*-

fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5
}


def make_lemonade(count):
    print(f'{count} lemonade were created.')

def out_of_stock():
    print('Out of stock.')


if count:= fresh_fruit.get('lemon', 0):
    make_lemonade(count)
else:
    out_of_stock()
