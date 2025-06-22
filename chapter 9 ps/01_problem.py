f = open("poem.txt", "r")
content  = f.read()
# print(content) ## this line are print of poem.txt
if("Twinkal" in content):
   print("Twinkal is present in content")

else:
   print("Twinkal is not present in content")

# if ("How are" in content):
#    print("How are you present in content")

# else:
#    print("how are not present in content")

f.close()