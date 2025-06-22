class Emplyee:
    sallry = 1000
    increment = 25

    @property # this function are return the value
    def salaryAfterIncrement(self):
        return (self.sallry + self.sallry * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sallry):
        self.increment = ((sallry/self.sallry)-1) *100 # ((new sallry/old sallry) - 1) * 100


e = Emplyee()
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement= 400
print(e.increment)