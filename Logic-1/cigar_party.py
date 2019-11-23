def cigar_party(cigars, is_weekend):
    if cigars <= 60 and cigars >= 40:
        return True
    elif is_weekend and cigars>=40:
        return True
    else:
        return False

cigar_party(30,False)