# Sum of two numbers
def sum_of_numbers(num1, num2):
    return num1 + num2

num_a = int(input("Enter first number for sum: "))
num_b = int(input("Enter second number for sum: "))

print("Sum of numbers: ", sum_of_numbers(num_a, num_b))


# Multiply two numbers
def multiply_numbers(num1, num2):
    print("Product of numbers: ", num1 * num2)

num_x = int(input("Enter first number for multiplication: "))
num_y = int(input("Enter second number for multiplication: "))
multiply_numbers(num_x, num_y)


# Get the last character of a string
def get_last_char(input_string):
    return input_string[-1]

user_string = input("Enter a string: ")
print("Last character of the string: ", get_last_char(user_string))


# Check if a number is odd or even
def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

odd_even_num = int(input("Enter a number to check Odd/Even: "))
print(f"The number is {check_odd_even(odd_even_num)}.")


# Check if a number is even
def is_even_number(number):
    return number % 2 == 0

even_check_num = int(input("Enter a number to check if it's even: "))
print(f"Is the number even? {is_even_number(even_check_num)}")


# Song function
def favorite_song():
    return "Cinderella is dead now...."

print(favorite_song())


# Find maximum of two numbers
def find_maximum(num1, num2):
    if num1 > num2:
        return num1
    return num2

max_num1 = int(input("Enter first number to find maximum: "))
max_num2 = int(input("Enter second number to find maximum: "))

print("Maximum number: ", find_maximum(max_num1, max_num2))


# Find the greatest of three numbers using find_maximum
def find_greatest_of_three(num1, num2, num3):
    greatest_two = find_maximum(num1, num2)
    return find_maximum(greatest_two, num3)

great_num1, great_num2, great_num3 = map(int, input("Enter three numbers separated by spaces: ").split())

print("Greatest number: ", find_greatest_of_three(great_num1, great_num2, great_num3))


# Max in three numbers
def greater(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    return c

a, b, c = map(int,input("enter a number: ").split())

print("Greater number: ", greater(a, b, c))


# Find palindrome number
def is_palindrome(number):
    return number == number[::-1]

palindrome_num = input("Enter a number to check if it's a palindrome: ")

if is_palindrome(palindrome_num):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")


def fibonacci(num):
    if num <= 0:
        return "Wrong input number"
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    
    a, b = 0, 1  # Initialize the first two Fibonacci numbers
    print(f"The 1st Fibonacci number is: {a}")
    print(f"The 2nd Fibonacci number is: {b}")
    
    for i in range(3, num + 1):  # Start from the 3rd number
        a, b = b, a + b  # Update a and b
        print(f"The {i}th Fibonacci number is: {b}")


# Input from the user
n = int(input("Enter a number to find its Fibonacci number: "))

# Call the function and display results
print("Fibonacci sequence:")
result = fibonacci(n)



#  default parameters
def greet(name="User", age=20):
    print(f"Hello, {name}! You are {age} years old.")

greet("John Doe")
greet(age=30)
greet()

# function scope
x = 10  # Global variable
print(x)

def change_value():
    a = 90 # local scope
    global x  # Accessing and modifying the global variable
    x = 20
    print("Inside function:", x)

change_value()
print("Outside function:", x)

# print(a) # can't acces local scope outside the function