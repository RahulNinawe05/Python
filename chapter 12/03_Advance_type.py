from typing import List, Dict, Tuple, Union

#               list of integer
number: list[int] = [1,2,3,4,5,6,]
print(number)

#         Tuple of string and an interger
person : Tuple[str, int] = ("Rahhul",34)

#              dict of str and an int
file: dict[str, int] = {"Rahul":5, "rahul":34}

#         dict of str and an float
file: dict[str, float] = {"Rahul":5.4, "rahul":3.4}

#             Union type for variables that can hold multiple types 
identifier: Union[int, str] = "ID123" 
identifier = 12345 # Also valid

#####               new
number : tuple[int] = [3,"rahul", 23.4,4,5,64, 6]
print(number)