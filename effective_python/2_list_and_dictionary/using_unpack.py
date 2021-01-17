# -*- coding:utf-8 -*-


def bubble_sort1(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp

# こちらのほうがベター
def bubble_sort2(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                a[i-1], a[i] = a[i], a[i-1] # スワップ


names = ['pretzels', 'carrots', 'arugula', 'bacon']
bubble_sort2(names)
print(names)


print ('#############################')

snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]
for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f'#{i+1}: {name} has {calories} calories')

print('-------------------------')

# こちらのほうがベター
for rank, (name, calories) in  enumerate(snacks, 1):
    print(f'#{rank}: {name} has {calories} calories')


# Note:
#  enumerate の第2引数はインデックスの初期値を指定する
#    alist = ["AAA","BBB","CCC","DDD"]
#    for a, b in enumerate(list, 999):
#        print(a)
#    出力結果
#    999
#    1000
#    1001
#    1002
