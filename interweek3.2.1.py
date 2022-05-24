'''
Реализуйте модуль  word_utils.py, позволяющий:

- очистить предложение от знаков препинания;

- получить список слов из предложения;

- получить самое длинное слово в предложении;
'''

from word_utils import *

while True:
    datastring = input("Введите предложение:\n")
    print(f"Предложение без знаков препинания:\n{exlude_punctuation(datastring)}")
    print(f"Список слов:\n{get_words(datastring)}")
    print(f"Самое длинное слово:\n{get_longest_word(datastring)}")
