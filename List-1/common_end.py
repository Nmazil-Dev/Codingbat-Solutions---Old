def common_end(a, b):
    end1 = len(a) -1
    end2 = len(b) -1
    if a[0] == b[0] or a[end1] == b[end2]:
        print (True)
    else:
        print (False)
common_end([1,2,3], [7,3])