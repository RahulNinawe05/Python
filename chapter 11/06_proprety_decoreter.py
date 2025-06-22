'''
getter and setter:-

The getter is like opening the box to see what’s inside.
The setter is like putting something new inside the box.

'''

class Employee:
    a = 1 
    @classmethod
    def show(self):
        print(f"the class attribute is a {self.a}")

    @property 
    def name(self): 
        return f"{self.fname} {self.lname}"
    
    #### this is concept
    @name.setter
    def name (self,value): 
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
e = Employee()
e.a = 45

e.name = "Rahul Ninawe"
print(e.name)

e.show()