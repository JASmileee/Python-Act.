#DUPLICATES

def byedupli():
    jasmile = input("Enter numbers: ")
    jasmile=list(jasmile)
    jas= []
    smile= []
    for i in jasmile:
        jasmile.count(i)
        if jasmile.count(i) !=1:
                jas.append(i)
        elif jasmile.count(i) ==1:
                smile.append(i)
    set(smile)
    print smile
    return(byedupli())
byedupli()
