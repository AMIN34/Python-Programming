class queueStack:
    def __init__(self) -> None:
        self.queue = []
    
    def push(self,val:int)-> None:
        self.queue.append(val)
        for i in range(len(self.queue)-1):
            x=self.queue.pop(0)
            self.queue.append(x)
    
    def pop(self):
        if len(self.queue)==0:
            return " Stack Empty 😵"
        x=self.queue.pop(0)
        return x
    
    def peek(self):
        if len(self.queue)==0:
            return " Stack Empty 😵"
        return self.queue[0]

if __name__=="__main__":
    ob = queueStack()
    ob.push(10)
    ob.push(20)
    ob.push(25)
    ob.push(15)
    ob.push(5)
    ob.push(2)
    
    print(ob.queue)
    print("Popped element : ", ob.pop())
    print(ob.queue)
    print("Top element: ", ob.peek())
    
