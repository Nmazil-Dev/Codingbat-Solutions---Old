def extra_end(str):
    length = len(str) -2
    new_word = (str[length] + str[length + 1]) * 3
    return (new_word)


extra_end('Hello')