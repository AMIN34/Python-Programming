class call_counter:
    def __init__(self):
        self.res=[]
    def ping(self,t:int)-> int:
        self.res.append(t)
        while self.res[0] < t - 3000:
            self.res.pop(0)
        return len(self.res)

if __name__=="__main__":
    ob = call_counter()
    print(ob.ping(1))
    print(ob.ping(300))
    print(ob.ping(3000))
    print(ob.ping(3002))
    print(ob.ping(7000))