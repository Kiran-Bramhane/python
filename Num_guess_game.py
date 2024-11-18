# import random

# # Generate a random number between 1 and 10
# win_num = random.randint(1, 10)

# print("Hey bro, welcome to the number win game!")
# for i in range(4):  # Allow the user 4 attempts
#     guess = int(input(f"Attempt {i+1}/4 - Guess the number (1 to 10): "))
#     if guess == win_num:
#         print("Congratulations! You won! 🎉")
#         break
#     elif guess > win_num:
#         print("Too high, try again!")
#     else:
#         print("Too low, try again!")
# else:
#     print(f"Sorry, you've used all your attempts. The correct number was {win_num}. Better luck next time!")



import random

# Generate a random number between 1 and 10
win_num = random.randint(1, 100)

print("Hey bro, welcome to the number win game!")
for i in range(6):  # Allow the user 4 attempts
    try:
        guess = input(f"Attempt {i+1}/6 - Guess the number (1 to 100): ").strip()

        # Check for empty input
        if not guess:
            print("Invalid input. Please enter a number.")
            continue

        # Convert input to integer
        guess = int(guess)

        # Check if the number is in range
        if not (1 <= guess <= 100):
            print("Invalid number. Please guess a number between 1 and 100.")
            continue

        # Check the guess
        if guess == win_num:
            print("Congratulations! You won! 🎉")
            break
        elif guess > win_num:
            print("Too high, try again!")
        else:
            print("Too low, try again!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
else:
    print(f"Sorry, you've used all your attempts. The correct number was {win_num}. Better luck next time!")
