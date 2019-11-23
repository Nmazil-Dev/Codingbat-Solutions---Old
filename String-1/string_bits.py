def string_bits(str):
    length = len(str) -1
    letters = []
    x = 0
    while x <= length:
        letters.append(str[x])
        x += 2
    new_word =  ''.join(letters)
    return (new_word)
string_bits('hello')