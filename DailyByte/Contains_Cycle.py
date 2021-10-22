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

    def cycleChecker(self) -> bool:
        s=set()
        temp = self.head
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False

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

    # Created a loop for testing
    llist.head.next.next.next.next = llist.head
    # print("Created list: ",end=" ")
    # llist.printLL()
    print()
    print(llist.cycleChecker())