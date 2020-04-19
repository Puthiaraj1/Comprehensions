import timeit


text = "time to learn python programming"


def capitals():
    text_caps = [char.upper() for char in text]
    return text_caps


def map_capitals():
    text_caps = list(map(str.upper, text))
    return text_caps


def capitals_word():
    word_caps =  [word.upper() for word in text.split(' ')]
    return word_caps


def map_capitals_word():
    word_caps = list(map(str.upper, text.split(' ')))
    return word_caps

if __name__ == '__main__':

    print(timeit.timeit("capitals()", setup="from map_intro import capitals", number=10000))
    print(timeit.timeit(map_capitals, number=10000))
    print(timeit.timeit(capitals_word, number=10000))
    print(timeit.timeit(map_capitals_word, number=10000))



