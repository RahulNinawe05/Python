with open("log.txt","r") as f:
    lines = f.readlines()

lineno= 1
for line in lines:
    if("python" in line):
        print(f"Yes, they are present in parougrap line number:{lineno}")
        
        break
    lineno+= 1

else:
    print("No, they are not present in parougrep")