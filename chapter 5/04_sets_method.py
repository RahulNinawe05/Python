# repitation method
e = set() # don't use set{} in as will be  empty dict. 
s = {2,4,5,3,3,3,3,"rahul",56} #you will orderd then use list

# # add method

# print(s,type(s))

# s.add(566)
# print(s)

s.update("abc")
print(s)

s.add(87)
print(s)

# remove method # this is not indexing 2 remove 
s.remove(2)     #actual value
print(s)

s.discard(2) # remove  #this is not indexing 2 remove 
print(s)

s1 = {3,56,2,4,6,34,200,100,300}
b = (s.union(s1))
print(b)
s1.clear()
print(s1)

s.union({2,"rahul,56", })
print(s)