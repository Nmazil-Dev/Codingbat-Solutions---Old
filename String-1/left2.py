def left2(str):
    left = str[:2]
    new_str = str[2:] + left
    return new_str
left2('Hello')