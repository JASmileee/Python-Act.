#EXERCISE NO. 6 - STACK
#JASTIN DEILE L. ORDA
#github.com/JASmileee


class Stack:
    def __init__(self):
        self.items = ["The Notebook",
                      "A Walk to Remember",
                      "Message in a Bottle",
                      "Dear John",
                      "The Last Song",
                      "Safe Haven",
                      "The Lucky One",
                      "The Best of Me",
                      "The Choice",
                      "The Longest Ride",
                      "Deliverance Creek",
                      "Nights in Rodante",]
        self.items2 = sorted(self.items)  #to peek the sorted items in the original list
        self.items3 = self.items2[::-1]   #to peek the reversed original list

    def sort(self):
        return sorted(self.items2)
    def reverse(self):
        return self.items2[::-1]
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peekname(self):
        return self.items3[len(self.items)-1]
    def peeknamenext(self):
        return self.items3[len(self.items)-2]
    def peektime(self):
        return self.items[len(self.items)-1]
    def peektimenext(self):
        return self.items[len(self.items)-2]
    def size(self):
        return len(self.items)




if __name__ == "__main__":
    jas = Stack()
    print "NICHOLAS SPARKS MOVIES"
    print "It has",jas.size(),"movies"
    x = input("Sort by:\n1. Name(A-Z)\n2.Time(new-old)\n\tEnter your choice: ")
    if x == 1:
        while jas.size() >= 2:
            print "Now Watching ",jas.peekname()
            print "Next movie is ",jas.peeknamenext(), "\n - - - - - - - - - - - - - - - - - - "
            jas.pop()
    elif x == 2:
        while jas.size() >= 2:
            print "Now Watching ",jas.peektime()
            print "Next movie is ", jas.peektimenext(), "\n - - - - - - - - - - - - - - - - - - "
            jas.pop()
    else:
        print "INVALID SORTING"
        



