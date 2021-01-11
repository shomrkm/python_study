# -*- coding:utf-8 -*-

# アンパックを効果的に使って、複数の戻り値を返す

def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum


lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

minimum, maximum = get_stats(lengths)
print(f'Min: {minimum}, Max: {maximum}')



# 4個以上の変数ならば、アンパックしない
# (読みづらく間違いが起きやすい)
# 代わりに、軽量クラスや namedtuple を検討する

def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count

    sorted_numbers = sorted(numbers)
    middle = count // 2
    if count % 2 == 0:
        lower = sorted_numbers[middle-1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]

    return minimum, maximum, average, median, count


lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

minimum, maximum, average, median, count = get_stats(lengths)
print(f'Min: {minimum}, Max: {maximum}')
print(f'Average: {average}, Median: {median}, Count: {count}')
