# -*- coding:utf-8 -*-

def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

# イテレータが渡されたとき意図通りにならず、エラーにもならない 
it = read_visits('reference\\my_numbers.txt')
percentages = normalize(it)
print(percentages)


########################################################

class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


def normalize_defensive(numbers):
    if iter(numbers) is numbers:
        raise TypeError('Must supply a container') # イテレータは許可しない 
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = ReadVisits('reference\\my_numbers.txt')
percentages = normalize_defensive(visits)
print(percentages)
assert sum(percentages) == 100.0

visits = [15, 35, 80]
percentages = normalize_defensive(visits)
print(percentages)
assert sum(percentages) == 100.0
