class Emploee:
    company = "ITC"
    def show (self):
        print(f"this is my {self.company}")

class coder:
    language = "Python"
    def pylanguage(self):
        print(f"this is my fourite language is {self.language}")

class programmer(Emploee, coder):  # THIS IS CONCEPT
    company = "ITC INFOTEC"
    name = "Defoult Name"
    sallry = 123333

    def no (self):
        print(f"this is my sallry {self.company} My Name is {self.name} and sallry {self.sallry}")

a = Emploee()
b = programmer()

b.show()
b.pylanguage()
b.no()