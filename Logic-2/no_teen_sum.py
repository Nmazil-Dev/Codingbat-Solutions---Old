def fix_teen(n):
    if n == 15 or n == 16:
        n = n
        return n
    else:
        return 0

def no_teen_sum(a,b,c):
    sum = a + b + c
    if a in range(13,20) and b in range(13,20) and c in range(13,20):
        return(fix_teen(a) + fix_teen(b) + fix_teen(c))
    elif a in range(13,20) and c in range(13,20):
        return(fix_teen(a) + b + fix_teen(c))
    elif a in range(13,20) and b in range(13,20):
        return(fix_teen(a) + fix_teen(b) + c)
    elif b in range(13,20) and c in range(13, 20):
        return(a + fix_teen(b) + fix_teen(c))
    elif a in range(13,20):
        return(fix_teen(a) + b + c)
    elif b in range(13,20):
        return( a + fix_teen(b) + c)
    elif c in range(13,20):
        return (a + b + fix_teen(c))
    else:
        return sum

no_teen_sum(13, 2, 4)
