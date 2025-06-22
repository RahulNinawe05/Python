class calculater:
    def __init__(self,c):
        self.n = c # this is concept

    def square (self):
        print(f"The square is {self.n*self.n}")

    def cube (self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot (self):
        print(f"The squareroot is {int(self.n**0.5)}") # use int function 
        
c = calculater(int(input("Enter the no:-")))
# c = calculater(4)
c.square()
c.cube()
c.squareroot()