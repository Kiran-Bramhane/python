child_input = input("Enter the name and age of the child (space-separated): ").strip()

while True:
    if child_input:  # Check if input is not empty
        try:
            child_name, age = child_input.split()
            
            # Check if age is numeric and a valid integer
            if age.isdigit():
                age = int(age)
                if age <= 0:
                    print("Invalid age. Age must be a positive number.")
                elif 14 <= age <= 16:
                    print(f"Hey {child_name}, you can play this game 🤩🤩")
                    break  # Exit the loop as input is valid
                else:
                    print(f"Hey {child_name}, sorry, you are not eligible to play this game 😵😵")
                    break
            else:
                print("Invalid age input 🙅🙅. Please enter a valid whole number for age.")
        except ValueError:
            print("Invalid input. Please provide both name and age, separated by a space.")
    else:
        print("No input provided. Please enter both name and age.")
    
    # Prompt for input again only if the previous input was invalid
    child_input = input("Please, enter the name and age of the child (space-separated): ").strip()


# pass statement
a=18 
if a >= 14 and a <= 16:
    pass
else:
    print("not passed")



# Exercise
# Input from user
while True:
    user_input = input("Enter the name and age of the user (space-separated): ").strip()

    if user_input:  # Check if input is not empty
        try:
            # Split the input
            u_name, u_age = user_input.split()

            # Check if age is numeric and positive
            if u_age.isnumeric() and int(u_age) > 0:
                u_age = int(u_age)

                # Validate the name
                if not u_name.isalpha():
                    print("Invalid name. Names should only contain alphabetic characters.")
                elif u_name.lower().startswith('a') and u_age > 10:
                    print(f"Hello {u_name}, you are welcome to the party 🎉🎉")
                    break
                else:
                    print(f"Sorry {u_name}, you cannot come to the party 😵😵")
                    break
            else:
                print("Invalid age input. Please enter a valid positive integer for age.")
        except ValueError:
            print("Invalid input. Please provide exactly two values: name and age.")
    else:
        print("No input provided. Please enter both name and age.")

    # Prompt for input again only if the previous input was invalid
    child_input = input("Please, enter the name and age of the child (space-separated): ").strip()

