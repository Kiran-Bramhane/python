# user input
#  input function always take string in the input
name = input("please enter your name: ")
print("Hello "+ name)

age = input("Please enter your age: ")
print("this is the age you "+ age)

# int function
num = int(input("Please enter a number: "))
print("this is the number you ", num)

# float function
f_num = float(input("Please enter your number: "))
print("this is the float number you ", f_num)


# Takin two inputs at once 
name , age = input("Please enter your name and age: ").split("+")
print("this is the name", name , age)

name , age = input("Please enter your name and age: ").split(" ")
print("this is the name", name , age)


a, b, c= map(int,(input("Enter the numers: ")).split(","))
print(f"this is the average of these numbers {(a+b+c)/3}")

# In Python, the statement `name, age = "sana", 19` is an example of **multiple assignment**, 
# also known as **tuple unpacking** or **sequence unpacking**. 
# This feature allows you to assign multiple values to multiple variables in a single line. 
# In this case, the string `"sana"` is assigned to the variable `name`, and the integer `19` is assigned to the variable `age`.  

name , age = "kiran", 19
print(name)
print(age)


# The statement a = b = c = 1 is an example of chained assignment, 
# where the value 1 is assigned to variables a, b, and c simultaneously. 
a = b = c = 1
print(a+b+c)