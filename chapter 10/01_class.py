class Employe:
    lang = "python"  # This is a class Attribute 
    sallry = 120000
    
rahul = Employe()
rahul.name="Rahul"  # This is an object / instance Attribute 
print(rahul.name,rahul.lang, rahul.sallry)

sager = Employe
sager.name="Sager"
print(sager.name,sager.sallry, sager.lang)

# here name is object atribute and sallry and lang are class attribute as they are directely belong to class