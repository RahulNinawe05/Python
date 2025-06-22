class calculater:
    def __init__(self,n):
        self.n = n

    def square (self):
        print(f"The square is {self.n*self.n}")

    def cube (self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot (self):
        print(f"The squareroot is {int(self.n**0.5)}") # use int function 
    
    @staticmethod
    def hello():
        print(f"hello Rahul")
        
c = calculater(int(input("Enter the no:-")))
# c = calculater(4)
c.hello()
c.square()
c.cube()
c.squareroot()