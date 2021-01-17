# -*- coding:utf-8 -*-

car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_decending = sorted(car_ages, reverse=True)

# 読みづらい
oldest = car_ages_decending[0]
second_oldest = car_ages_decending[1]
others = car_ages_decending[2:]
print(oldest, second_oldest, others)

# 読みやすい
oldest, second_oldest, *others = car_ages_decending
print(oldest, second_oldest, others)

oldest, *others, youngerst = car_ages_decending
print(oldest, others, youngerst)

print('-------------------------------')



# 以下のような使い方もできる

def generate_csv():
    yield('Date', 'Model', 'Year', 'Price')
    yield('2021-01-01', 'A', '2020', '$100')
    yield('2021-01-01', 'B', '2021', '$200')
    yield('2021-01-01', 'C', '2021', '$300')
    yield('2021-01-01', 'A', '2020', '$100')

it = generate_csv()
header, *rows = it
print('CSV Header: ', header)
print('CSV count: ', len(rows))
