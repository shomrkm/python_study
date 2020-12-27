# -*- coding:utf-8 -*-

from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(repr(my_values))

red = int(my_values.get('red', [''])[0] or 0)
green = int(my_values.get('green', [''])[0] or 0)
opacity = int(my_values.get('opacity', [''])[0] or 0)
print(f'Red:    {red!r}')
print(f'Green:  {green!r}')
print(f'Blue:   {opacity!r}')

print('===================================')


# Using helper function

def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    else:
        return default

red = get_first_int(my_values, 'red')
green = get_first_int(my_values, 'green')
opacity = get_first_int(my_values, 'opacity')
print(f'Red:    {red!r}')
print(f'Green:  {green!r}')
print(f'Blue:   {opacity!r}')


# Note:
#  {red!r} : "!r" は repr を返すことを表す.


