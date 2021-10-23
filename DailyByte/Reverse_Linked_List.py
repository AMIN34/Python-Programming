"""
Given a linked list, containing unique values, reverse it, and return the result.

Ex: Given the following linked lists...

1->2->3->null, return a reference to the node that contains 3 which points to a list that looks like the following: 3->2->1->null
7->15->9->2->null, return a reference to the node that contains 2 which points to a list that looks like the following: 2->9->15->7->null
1->null, return a reference to the node that contains 1 which points to a list that looks like the following: 1->null
"""

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head= None
    
    def insert(self,val):
        newNode = Node(val)
        newNode.next=self.head
        self.head=newNode
    
    # Itterative Approach
    # def reverse(self):
    #     prev = None
    #     curr = self.head
    #     while curr:
    #         next = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = next
    #     self.head=prev
    
    # Recursive Approach
    def reverse(self,head):
        # If head is empty or has reached the list end
        if head == None or head.next == None:
            return head
        
        # Reverse the rest of the list
        rest = self.reverse(head.next)

        # Put the first element at end
        head.next.next =head
        head.next = None

        # Fixing the header pointer
        return rest
    
    def printLL(self):
        current = self.head
        while (current):
            print(current.data,end=" ")
            current=current.next
        print()

if __name__=="__main__":
    llist = LinkedList()
    
    #Inserting at the beginning
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)
    llist.insert(5)
    llist.insert(6)

    print("Given linked list: ")
    llist.printLL()
    llist.head = llist.reverse(llist.head)
    print("Reversed List: ")
    llist.printLL()
