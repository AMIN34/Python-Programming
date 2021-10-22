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

    def remove(self,key):
        # Storing head node
        temp = self.head
        prev = None

        # If the head node itself is the key or their are multiple occurences of the key
        while temp!=None and temp.data==key:
            self.head = temp.next # Changed head
            temp = self.head    # Changed temp
        
        # Delete occurences other than head
        while temp!=None:
            # Search for the key to be deleted while keeping track of the previous node
            while temp != None and temp.data !=key:
                prev = temp
                temp = temp.next
            # if key is not present in linked list
            if temp == None:
                return self.head
            # Unlinking the node from the linked list (i.e deleting)
            prev.next = temp.next
            # Completing the linked List connection
            temp = prev.next
        return self.head

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
    llist.remove(2)
    print("Modified list: ",end=" ")
    llist.printLL()