class Emploee:
    company = "ITC"
    def show (self):
        print(f"this is my {self.name}")

# class programmer:
#     company = "ITC INFOTEC"
#     def show (self):
#         print(f"this is my {self.name}")
    
#     def no (self):
#         print(f"this is my sallry{self.sallry}")

class programmer(Emploee):  # THIS IS CONCEPT
    company = "ITC INFOTEC"
    def no (self):
        print(f"this is my sallry{self.name}")

a = Emploee()
b = programmer()


print(a.company, b.company)