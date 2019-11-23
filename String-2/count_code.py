def count_code(str):
    str = str.lower()
    count = 0
    letter = "abcdefghijklmnopqrtuvwxyz"
    for i in letter:
        count += (str.count('co'+ i + 'e'))
    return(count)
count_code('codexxcode')