"""
How to create a Linked List

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,data):
        newNode=Node(data)
        if self.head:
            current = self.head
            while current.next:
                current=current.next
            current.next=newNode
        else:
            self.head=newNode
    
    def printLL(self):
        current = self.head
        while (current):
            print(current.data,end=" ")
            current=current.next
"""
# Merging
# taken from leeetcode
def mergeTwoLists(self, l1, l2):
    # Base Cases
    if not l1 and not l2:
        return l1
    if not l1:
        return l2
    if not l2:
        return l1
    # Starting node for the merged list
    if l1.val <= l2.val:
        head = l1
        new = l1
        l1 = l1.next
    else:
        head = l2
        new = l2
        l2 = l2.next
    # traversing the 2 lists and checking the minimum among them and adding that to the new lists
    while l1 and l2:
        if l1.val <= l2.val:
            new.next = l1
            new = l1
            l1 = l1.next
        else:
            new.next = l2
            new = l2
            l2 = l2.next
    # The last node
    if l1:
        new.next = l1
    elif l2:
        new.next = l2
    return head
