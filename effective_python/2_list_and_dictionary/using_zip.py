# -*- coding:utf-8 -*-

names = ['Cacilia', 'Lise', 'Marie']
counts = [len(n) for n in names]

longest_name = None
max_count = 0
# イテレータを並列に処理するには zip を使う
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

print(f'longest name: {longest_name}')

