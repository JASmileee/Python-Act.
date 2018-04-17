#MIDTERM EXAMINATION

def match_a():
    print ("Function match_a() \n")

    jas1 = input ("Enter 1st input:")
    jas2 = input ("Enter 2nd input:")
    jas3 = input ("Enter 3rd input:")

    jas22 = []
    jas33 = []
    jas11 = []

    
    for i in jas1:
        if len(i) != 1:      #exclude character
            if i == i[::-1]: #Palindrome checker
                jas11.append(i)

    for i in jas2:
        if len(i) != 1:      #exclude character
            if i == i[::-1]: #Palindrome checker
                jas22.append(i)

    for i in jas3:
        if len(i) != 1:      #exclude character
            if i == i[::-1]: #Palindrome checker
                jas33.append(i)

    print "1st output: ",len(jas11)
    print "2nd output: ",len(jas22)
    print "3rd output: ",len(jas33)

match_a()
print ("\n\n")






def front_x():
    print ("Function front_x()\n")

    jas1 = input ("Enter 1st input:")
    jas2 = input ("Enter 2nd input:")
    jas3 = input ("Enter 3rd input:")

    jas11 = []
    jas111 = []
    jas22 = []
    jas222 = []
    jas33 =[]
    jas333 = []

    for i in jas1:
        if i.startswith('x'): #new list of strings that starts with 'x' from others
            jas11.append(i)
        else:
            jas111.append(i) #new list of other strings
            
    print "1st output: ",sorted(jas11) + sorted(jas111) #to alphabetically arranged


    for i in jas2:
        if i.startswith('x'): #new list of strings that starts with 'x' from others
            jas22.append(i)
        else:
            jas222.append(i) #new list of other strings
            
    print "2nd output: ",sorted(jas22) + sorted(jas222) #to alphabetically arranged


    for i in jas3:
        if i.startswith('x'): #new list of strings that starts with 'x' from others
            jas33.append(i)
        else:
            jas333.append(i) #new list of other strings
            
    print "3rd output: ",sorted(jas33) + sorted(jas333) #to alphabetically arranged

    
front_x()
