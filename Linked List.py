#LinkedList

class Node:

    def __init__(self, data = None):
        self.data = data 
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self,data):
        new_node = Node(data)
        cur = self.head
        while cur.next!=None:
            cur =cur.next
        cur.next=new_node
    def size(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total +=1
            cur = cur.next
        return total
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print elems
    def get(self,index):
        if index >=self.size():
            print"ERROR: 'Get' Index out of range"
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index: returncur_node.data
            cur_index+=1
    def erase(self,index):
        if index >=self.size():
            print"ERROR: 'Erase' Index out of range"
            return
        cur_index = 0
        cur_node = self.head
        while True:
            last_node=cur_node
            cur_node=cur_node.next
            if cur_index== index:
                last_node.next=cur_node.next
                return
            cur_index+=1


if __name__=='__main__':

    mylist=LinkedList()
    maxitems=input("How many items do you want to input in your list? : ")
    x = 1
    while mylist.size() <maxitems:
        print"Item No.",x,
        y =input("Enter here:  " )
        mylist.append(y)
        x +=1

    print"\nORIGINAL LINKED LIST"
    mylist.display()

    jas= []
    def reverse():
        while mylist.size() !=0:
            jas.append(mylist.get(mylist.size()-1))
            mylist.erase(mylist.size()-1)
        print"REVERSED LINKED LIST \n", jas
    reverse()
