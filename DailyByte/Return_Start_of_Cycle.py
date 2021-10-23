"""
Given a potentially cyclical linked list where each value is unique, return the node at which the cycle 
starts. If the list does not contain a cycle, return null.

Ex: Given the following linked lists...

1->2->3, return null
1->2->3->4->5->2 (5 points back to 2), return a reference to the node containing 2
1->9->3->7->7 (7 points to itself), return a reference to the node containing 7
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,val):
        newNode = Node(val)
        newNode.next=self.head
        self.head=newNode
    
    def detectLoop(self):
        s = set()
        temp = self.head
        while temp:
            if temp in s:
                return temp
            s.add(temp)
            temp=temp.next
        return None

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
    
    print(llist.detectLoop().data)
