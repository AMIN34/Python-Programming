class movingAvg:
    def __init__(self):
        self.items = []
    def next(self,val:int,cap:int)->int:
        self.items.append(val)
        return sum(self.items[-cap:])//(len(self.items) if len(self.items) <= 3 else 3)

if __name__=="__main__":
    ob= movingAvg()
    cap=int(input())
    while True:
        try:
            print(ob.next(int(input()),cap))
        except:
            break
    
    