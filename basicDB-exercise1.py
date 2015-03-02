__author__ = 'Molly'


class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


def revstring(mystr):
    s = Stack()
    for char in mystr:
        s.push(char)
    reversed_str = ""
    while not s.isEmpty():
        reversed_str += s.peek()
        s.pop()
    return reversed_str

def main():
    print revstring("MollyZhang")

if __name__ == "__main__":
    main()