try:
    a = int(input("Enter the no.:-"))
    print(a)

# Exception CRASH HOU DET NAHI
except Exception as a:
    print(a, "TRY AGAIN, This is wrong ")

print("This else statement are inside the else")

###             this is concept                  #####


''' 
return raho ki nahi raho finaly chalel but
finaly cha evagy print asel ter nahi chalel
'''

def main():
        try:
            a = int(input("Enter the no.:-"))
            print(a)
            return

        # Exception CRASH HOU DET NAHI
        except Exception as a:
            print(a, "TRY AGAIN, This is wrong ")
            return # return cha matlab ahe ki khalcha kahi hi print aseel tar nahi chalel

        finally:
             print("This else statement are inside the else")

main()
