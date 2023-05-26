import random
CHOICES = ['rock', 'paper', 'scissors']
print("Make your throw")
while True:
    user_choice = input("Type rock, paper or scissors: ")
    if user_choice in CHOICES :
        computer_choice = random.choice(CHOICES)
        print(
        f"\n You threw '{user_choice}', the computer threw '{computer_choice}'"
        )
    else :
        print(f"\n You typed '{user_choice}', which isn't a valid choice")