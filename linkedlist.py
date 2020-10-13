class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,x):
        node = Node(x)
        node.next=self.head
        self.head=node
    
    def insertAfter(self,y,x):
        if y is None:
            print("The node is not in the list")
            return
        
        node = Node(x)
        node.next = y.next
        y.next = node
        

    def append(self,x):
        node = Node(x)
        if self.head is None:
            self.head=node
            return
        
        last = self.head
        while(last.next):
            last=last.next

        last.next=node

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

if __name__ == "__main__":
    llist = LinkedList()