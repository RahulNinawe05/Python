# # this is normal ####
# class Employee:
#     a = 1  #does NOT print the class attribute
#     def show(self):
#         print(f"the class attribute is a {self.a}")

# e = Employee()
# e.a = 45

# e.show()

# this is concept ###
class Employee:
    a = 1
    @classmethod # does print the class attribute
    def show(cls):
        print(f"the class attribute is a {cls.a}")

e = Employee()
e.a = 45

e.show()

