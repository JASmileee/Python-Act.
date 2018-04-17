#Queue&Dequeue

class Queue:
    def __init__(self):
        self.items= []

    def isEmpty(self):
        return self.items== []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def printqueue(self):
        for items in self.items:
            print (items)

q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(3)
q.enqueue(19)
q.enqueue(98)
q.enqueue(17)
q.enqueue(8)
q.printqueue()
q.dequeue()
print("\n")
q.printqueue()
