#EXERCISE NO. 4 -   FUNCTION
#JASTIN DEILE L. ORDA
#github.com/JASmileee
#KILLER KILLER GAME

print "LET'S PLAY KILLER KILLER"
def killerkiller():
    Killer = input("[1] -Winks at the Judge\n[2] -Winks at the Doctor\n[3] -Winks at the Police\n   Enter Action: ")
    Doctor = input ("[1] -Winks at the Judge\n[2] -Winks at the Police\n   Enter Action: ")
    Police = input ("[1] -Winks at the Killer\n Enter Action: ") 
    Judge = input ("[1] -Winks at the Police\n Enter Action: ")
    if Killer == 1:
        if DOCTOR == 1:
             print "   JUDGE WILL BE ALIVE!\n"
        elif DOCTOR ==2:
            print ("   POLICE WILL BE ALIVE!\n")
        elif KILLER==2:
             print ("   DOCTOR WILL BE DEAD AND NO ONE WILL HEAL THEM!\n")
        return killerkiller()
    elif KILLER ==3:
        if DOCTOR==2:
             print ("   POLICE WILL BE ALIVE!\n")
        elif DOCTOR==1:
             print ("   POLICE WILL BE DEAD AND THE KILLER WON'T GET CAUGHT!\n")
        return killerkiller()
    elif POLICE ==1:
        if JUDGE==1:
             print ("   THE KILLER GOT CAUGHT AND PUNISHED!\n")
        elif KILLER==1:
             print ("   THE KILLER WON'T BE PUNISHED!\n")
        return killerkiller()
    
killerkiller()
