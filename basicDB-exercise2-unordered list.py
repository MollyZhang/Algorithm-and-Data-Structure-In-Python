__author__ = 'Molly'

""" implement append, insert, index and pop methods for linked list"""

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def __str__(self):
        list_str = "head"
        current = self.head
        while current != None:
            list_str = list_str +  "->" + str(current.getData())
            current = current.getNext()
        list_str = list_str +  "->" + str(None)
        return list_str

    def append(self, item):
        """add items into the linked from the other direction compared to add()"""
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        temp = Node(item)
        temp.setNext(current.getNext())
        current.setNext(temp)

    def getIndex(self, item):
        """get the index of an item, assume the first one (head pointing to) is 0"""
        index = 0
        current = self.head
        found = False
        while current != None:
            if current.getData() == item:
                found = True
                break
            else:
                current = current.getNext()
                index += 1
        if not found:
            index = None
        return index

    def getItem(self, index):
        """return an item given an index"""
        current = self.head
        for i in range(index):
            current = current.getNext()
        if current != None:
            return current.getData()
        else:
            raise("index out of range")


    def pop(self, index):
        self.remove(self.getItem(index))


    def insert(self, index, item):
        """insert an item after index item"""
        current = self.head
        for i in range(index):
            current = current.getNext()

        if current != None:
            temp = Node(item)
            temp.setNext(current.getNext())
            current.setNext(temp)
        else:
            raise("index out of range")



class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


alist = UnorderedList()
alist.add(30)
alist.add(31)
alist.add(27)
alist.append(100)
alist.append(101)
print alist
print alist.getIndex(27)
print alist.getItem(4)
alist.pop(4)
print alist
alist.insert(1, 5)
print alist