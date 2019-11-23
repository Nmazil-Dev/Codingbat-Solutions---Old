def make_out_word(out, word):
    first =  out[:2]
    second = out[2:]
    new_word = first + word + second
    return(new_word)
make_out_word("<<>>", "Yay")