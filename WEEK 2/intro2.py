# Variables hold data
from operator import is_


age = 55         # int (integer)
height = 5.75      # float (decimal)
name = "Kasongo"   # str (string)
is_a_liar = True  # bool (boolean)

# Printing out the values
print("Name:", name)          # Outputs: Name: Charlie
print("Age:", age)            # Outputs: Age: 25
print("Height:", height)      # Outputs: Height: 5.75
print("Is a liar?", is_a_liar)  # Outputs: Is a liar? true
# check data types
print(type(name))        # Outputs: <class 'str'>
print(type(age))         # Outputs: <class 'int'>
print(type(height))      # Outputs: <class 'float'>
print(type(is_a_liar))   # Outputs: <class 'bool'>

# Dynamic typing:
age = 24
print (age) # Outputs: 24
age = "Now I'm 24 years"
print (age) # Outputs: string

temperature = 26
if temperature > 25:
    print("It's a hot day")
else:
    print("It's a cool day")
# Outputs: It's a hot day

marks = 99
if marks > 90:
    print("Grade A")
elif marks > 70:
    print("Grade B")
else:
    print("Grade C")