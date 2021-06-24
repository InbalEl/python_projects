import random

def get_user_input():
    return input("guess a number between 1 and 9: ")

user_input = get_user_input()

while user_input != "exit":
    user_input = int(user_input)
    rand_num = random.randint(1, 9)
    answer =  "You did it!" if user_input == rand_num else ("A bit too high" if user_input > rand_num else "A bit too low")
    print(f"Did you guess correctly? {answer}")
    user_input = get_user_input()

print("Thanks for playing!")