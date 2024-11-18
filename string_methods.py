person_name = "Kiran Bramhane"

# len() function gives the length of the string
print(len(person_name))

# upper() method converts the string to uppercase
print(person_name.upper())

# lower() method converts the string to lowercase
print(person_name.lower())

# title() method converts the first character of each word to uppercase
print(person_name.title())

# count() method counts the number of characters
print(person_name.count("a"))

# strip() method removes the leading and trailing whitespaces
language_name = "      Py thon    "
separator_dots = ".................."
print(language_name)
print(language_name.strip() + separator_dots)
print(language_name.lstrip() + separator_dots)
print(language_name.rstrip() + separator_dots)

# replace() method replaces a character with another
print(language_name.replace(" ", "") + separator_dots)
programming_lang = "C"
print(programming_lang.replace("C", "Javascript"))

description_text = "She is a coder as well as dancer"
print(description_text.replace("as", "V"))
print(description_text.replace("as", "V", 1))

# find() method finds the first occurrence of a character 
first_occurrence = description_text.find("as")
second_occurrence = description_text.find("as", first_occurrence + 1)
print(f"First occurrence of 'as' is at position {first_occurrence}")
print(f"Second occurrence of 'as' is at position {second_occurrence}")

# startswith() method checks if the string starts with a specific character
print(person_name.startswith("K"))

# endswith() method checks if the string ends with a specific character
print(person_name.endswith("n"))

# split() method splits the string into a list of words
print(person_name.split())

# join() method joins the elements of a list into a string
word_list = ["She", "is", "a", "coder", "as", "well", "as", "dancer"]
print(" ".join(word_list))

# format() method formats the string
user_name = "ritvik"
user_age = 21
print(f"Hello {user_name}, your age is {user_age}")

# isalpha() method checks if the string contains only alphabetic characters
print(user_name.isalpha())

# isdigit() method checks if the string contains only digits
print(str(user_age).isdigit())

# isupper() method checks if the string contains only uppercase characters
print(user_name.isupper())

# islower() method checks if the string contains only lowercase characters
print(user_name.islower())

# isalnum() method checks if the string contains only alphanumeric characters
print(user_name.isalnum())

# isspace() method checks if the string contains only whitespace characters
print(user_name.isspace())

# isnumeric() method checks if the string contains only numeric characters
print(str(user_age).isnumeric())

# isidentifier() method checks if the string is a valid identifier
print(user_name.isidentifier())

# isprintable() method checks if the string contains only printable characters
print(user_name.isprintable())

# center() method keep string to center and add we can add right and left characters
print(person_name.center(30, "*"))  # string length + how many star we want that count

# Input for length and character count
input_name, input_char = input("Please enter your name and a character which exists in the name: ").split(",")
print(f"Length of the name is {len(input_name.strip())}")
print(f"Character count is: {input_name.strip().lower().count(input_char.strip().lower())}")
