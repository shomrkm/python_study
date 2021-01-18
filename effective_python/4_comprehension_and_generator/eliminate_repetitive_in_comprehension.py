# -*- coding:utf-8 -*-

stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

order = ['screws', 'wingnuts', 'clips']

def get_batches(count, size):
    return count // size


result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches

print(result)

# リスト内表記とウォルラス演算子を使って簡潔に書ける
found = {name: batches for name in order
         if (batches := get_batches(stock.get(name, 0), 8))}
print(found)