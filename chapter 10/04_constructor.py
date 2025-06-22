class Employe:
    lang = "python" 
    sallry = 120000

    def __init__(self, name, sallry, lang):  # DUNDER method they Automatically call

        self.name = name
        self.sallry = sallry
        self.lang = lang
        print("Hey Thes is My Persnal Information")


    def getinfo(self):
        print(f"the languege is: {self.lang} the sallry is: {self.sallry}")

    @staticmethod
    def greet():
        print("Good Morning")
    
rahul = Employe("Rahul", 1300000, "python")
# rahul.getinfo() dunder method are not writing
print(rahul.name, rahul.sallry, rahul.lang)

