def end_other(a, b):
    a = a.lower()
    b = b.lower()
    endA = len(a) - len(b)
    endB = len(b) - len(a)

    if a in (b[endB:]):
        return True
    elif b in (a[endA:]):
        return True
    else:
        return False
    

end_other('AbC', 'HiaBc')