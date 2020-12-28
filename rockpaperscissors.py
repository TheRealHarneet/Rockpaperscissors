import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
again = True

while again == True:
    choices = [rock, paper, scissors]
    # Player Choice

    my_choice = int(input("What do you Choose? Type 0 for Rock, 1 for   Paper, or 2 for Scissors"))
    picture = choices[my_choice]

    print("You Chose:", picture)

    # Computer Choice
    computer_choice = random.randint(0, 2)
    computer_picture = choices[computer_choice]

    print("The Computer Chose:\n", computer_picture)
    if my_choice >= 3 or my_choice < 0:
        print("Invalid Number You Lose!")
    elif my_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and my_choice == 2:
        print("You Lose!")
    elif computer_choice > my_choice:
        print("You Lose!")
    elif my_choice > computer_choice:
        print("You win\n!")
    elif computer_choice == my_choice:
        print("It's a Draw!\n")
    again = str(input("Play Again?Type yes or no\n "))
    if again == 'no':
        print("Hope You Enjoyed the Game <3 -H ")




