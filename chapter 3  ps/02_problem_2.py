letter = ''' Dear <|Name|>,                       # Qoustion no 1
             You are selected!
             <|Date|> '''

print(letter.replace("<|Name|>", "Rahul").replace("<|Date|>", "25 July"))

# this program they will be use replace function


# # My example 

joining_letter = '''Dear <|Name|>,                  # Qoustion no 2
You are selected! in this <|name|> organization,
You are Reporting <|Time|> ,
In This Place <|Location|> ,
WELCOME
<|Name|> '''

#  this is my mistake :-  "Overwriting a Variable:"

# a =joining_letter.replace("<|Name|>", "Rahul")
# a =joining_letter.replace("<|Time|>", " 10.00 'o clock")
# a =joining_letter.replace("<|Location|>", "Lokmanya Nagar")
# a =joining_letter.replace("<|Name|>", "Rahul Ninawe")

# print(a)


a =joining_letter.replace("<|Name|>", "Rahul Ninawe..")
a =a.replace("<|Location|>", "Lokmanya Nagar")
a =a.replace("<|Time|>", " 10.00 'o clock")
a =a.replace("<|Name|>", "Rahul")
a =a.replace("<|name|>", "WINZERA")


print(a)

