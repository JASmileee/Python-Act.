#DUPLICATES

def byedupli():
    jas=input ("ENTER numbers: ")
    smile =list(set(jas))
    print smile
    return byedupli()
byedupli()
