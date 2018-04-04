#JASTIN DEILE L. ORDA
#Char & String Manipulation



def only_upper(s):
    upper_chars = ""
    for char in s:
        if char.isupper():
            upper_chars += char
    return upper_chars

print only_upper("JASmile jasMILE JASmile jasMILE")
