# -*- coding:utf-8 -*-


flavor_list = ['vasnilla', 'chocolate', 'pecan', 'strawberry']
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f'{i+1}: {flavor}')

print('##################################')

# range でループしてシーケンスのインデックスを処理するよりも、enumerate を使う.
# enumerate は第2引数でインデックスの初期値を指定できる.
for i, flavor in enumerate(flavor_list, 1):
    print(f'{i}: {flavor}')
