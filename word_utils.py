'''
Реализуйте модуль  word_utils.py, позволяющий:

- очистить предложение от знаков препинания;

- получить список слов из предложения;

- получить самое длинное слово в предложении;
'''
punctuation_marks = [',', '.', '!', '?', ';', '-', ':']

def exlude_punctuation(datastring):
    outstring = datastring
    for mark in punctuation_marks:
        outstring = outstring.replace(mark, ' ')
    return outstring

def get_words(datastring):
    clearstring = exlude_punctuation(datastring)
    return clearstring.split()

def get_longest_word(datastring):
    words = get_words(datastring)
    maxlen = 0
    index_longest_word = 0
    for i, word in enumerate(words):
        if len(word) > maxlen:
            maxlen = len(word)
            index_longest_word = i
    
    return words[index_longest_word]



