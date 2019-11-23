def double_char(str):
    new_word = []
    for i in str:
        new_word.append(i*2)
    return (''.join(new_word))
    
double_char('The dog')
