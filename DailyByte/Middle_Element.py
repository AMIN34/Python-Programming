class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head =None
    
    # Insert value at the begining
    def insert(self,val):
        newNode = Node(val)
        newNode.next = self.head
        self.head=newNode
    
    # Insert value at the end
    # def insert(self,data):
    #     newNode=Node(data)
    #     if self.head:
    #         current = self.head
    #         while current.next:
    #             current=current.next
    #         current.next=newNode
    #     else:
    #         self.head=newNode

    def middleElement(self):
        fast = slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def printLL(self):
        current = self.head
        while (current):
            print(current.data,end=" ")
            current=current.next
    
if __name__=="__main__":
    llist = LinkedList()
    llist.insert(7)
    llist.insert(5)
    llist.insert(3)
    llist.insert(7)
    llist.insert(3)
    llist.insert(7)

    print("Created list: ",end=" ")
    llist.printLL()
    print()
    x=llist.middleElement()
    print(x)