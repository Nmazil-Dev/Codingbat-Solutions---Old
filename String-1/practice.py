def diff21(n):
  diff = 21 - abs(n)
  dub = diff * 2
  if n > 21:
    print (dub)
  else:
    return (diff)

diff21(22)

def front_back(str):
  if len(str) == 1:
    return str
  else:
    new = []
    length = len(str) -1
    first = (str[0])
    last = str[length]
    new.append(last)
    for i in range(1, length):
      new.append(str[i])
      new.append(first)
    word = ''.join(new)
    print(word)

front_back('eocd')
