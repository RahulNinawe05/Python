def myfun():
    print("hello word")


myfun()
print(__name__) 
print("This program has finished running")


if __name__== "__main__": # this program are not run in Q9 import 
    # if this code are directily exicuted by runing the file its present in!
    print("This file is running directly")
    myfun()
    print(__name__) 
    print("This program has finished running")
