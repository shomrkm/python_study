# -*- coding:utf-8 -*-


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}

def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)

sort_priority(numbers, group)
print(numbers)


# 以下の関数は意図通りに found を返さない(必ず False を返す)
# nonlocal でクロージャの外のスコープにあることを明示すれば、意図通りの found が返すようになる
# 単純な場合ならよいが、複雑な場合は、nonlocal を使うのは良くない

def sort_priority2(values, group):
    found = False               # スコープ: sort_priority2
    def helper(x):
        # nonlocal found        # この行をいれれば、意図通り動作するようになる
        if x in group:
            found = True        # スコープ: helper
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found

found = sort_priority2(numbers, group)
print('Found: ', found)     # Found: False
print(numbers)


# ヘルパークラスで状態をラップするとわかりやすくなる

class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in group:
            self.found = True
            return (0, x)
        return (1, x)

sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True