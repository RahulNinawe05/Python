class programmer:
    company = "Microsoft"
    def __init__(self, name, sallry, pin):
        self.name = name
        self.sallry = sallry
        self.pin = pin

#### new #####

class collge:
    student ="PCE"
    def __init__(self, name, branch, Section ):
        self.nme=f"my name is {name} and branch is {branch} section is {Section}" 
c = collge ("Rahul" , "ECE", "A")
print(c.nme)

 
'''
##### this is new choice
p = programmer("Rahul", 1200000, 441201) 
print(f"my name is {p.name}sallry is {p.sallry}located in {p.pin}company name is {p.company} ")

'''

p = programmer("Rahul", 1200000, 441201)
print(f"this is name is {p.name} this sallry is {p.sallry}")
print(p.name, p.sallry, p.pin, p.company)

r = programmer("Rohan", 1200000, 441202)
print(r.name, r.sallry, r.pin, r.company)


class programming:
    company="Microsoft"
    def __init__(self, name, sallry, pin):
        self.name = name  
        self.sallry = sallry
        self.pin = pin

p = programming("Rahul", 150000, 441201)
print(p.name, p.sallry, p.pin, p.company)