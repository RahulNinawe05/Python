class Employe:
    lang = "python" 
    sallry = 120000

    def getinfo(self):
        print(f"the languege is: {self.lang}. the sallry is: {self.sallry}")

    @staticmethod
    def greet():
        print("Good Morning")
    
rahul = Employe()

rahul.getinfo()
rahul.greet()
#Employe.getinfo(rahul)
