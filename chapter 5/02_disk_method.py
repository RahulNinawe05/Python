d = {} #empty dict
mark = {
    "Rahul": 100,
    "harish": 94,
    "Sager": 84,
    0 : "ghhochu"
}

# print(mark.clear())  #But since mark is already empty (you cleared it before), it will print:
print(mark.copy())
d = mark.copy()     #store the value
print(d)
print(mark.items())
print(mark.keys())
print(mark.values())
mark.update({"Rahul": 99, "Pratik" : 57}) #jo nahi hii add hota hii
print(mark)

print(mark.get("harish"))  #PRINTS NONE
# print(mark["harish2"]) #RETURNS AND ERROR