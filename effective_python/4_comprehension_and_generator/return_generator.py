# -*- coding:utf-8 -*-

def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


address = 'Four score and seven years ago...'

result = index_words(address)
print(result)

# result = list(index_word_iter(address))
it = index_words_iter(address)
print(next(it))
print(next(it))



