from random import randint

class train:

    def __init__(self, trainNo, hour):
        self.trainNo =trainNo
        self.hour = hour
        
    def book(self,fro, to):
        print(f"ticket is booked in train no.{self.trainNo} from {fro} to {to} is Rs.{randint(100, 1000)}")

    def getStatus(self):
        print(f"train no {self.trainNo} is runing on time")
    
    def getFare(self, fro, to):
        print(f"ticket is fare in train no.{self.trainNo}, from {fro} to {to} is Rs.{randint(222,555)}")

    def let(self):
        print(f"train no: {self.trainNo}, Nagpur to Gondia is Delay {self.hour} hour ")

t = train(18345, 5)
t.book("Nagpur" ,"Gondia")
t.getStatus()
t.getFare("Nagpur" ,"Gondia")
t.let()