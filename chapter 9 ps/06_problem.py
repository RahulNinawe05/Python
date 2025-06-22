with open("log.txt","r") as f:
    content = f.read()

if("python" in content):
    print("Yes, they are present in parougrap")

else:
    print("No, they are not present in parougrep")