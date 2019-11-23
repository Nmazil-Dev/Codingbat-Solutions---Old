def round_sum(a, b, c):
    def round10(num):
        rem = num % 10
        if  rem >= 5:
            new = num - rem + 10
            return(new)
        elif rem < 5:
            new = num - rem
            return(new)
    return (round10(a) + round10(b) + round10(c))
    

