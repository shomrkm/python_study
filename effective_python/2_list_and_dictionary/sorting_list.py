# -*- coding:utf-8 -*-

numbers = [93, 86, 11, 68, 70]
numbers.sort()
print(numbers)


class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight!r}'


tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('chisel', 0.25)
]

# name でソート
tools.sort(key=lambda x: x.name)
print(tools)
# weight でソート
tools.sort(key=lambda x: x.weight)
print(tools)

# tuple を使って weight -> name でソート
tools.sort(key=lambda x: (x.weight, x.name))
print(tools)