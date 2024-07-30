import random as r

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


game = [rock,paper,scissors]


print("Welcome to our game rock paper and scissors")
print("0 for rock, 1 for paper and 2 for scissors")
user_index = int(input("your turn please choice 0,1 and 2\n"))
user = game[user_index]
print(f"{user}")

print("Compuer turn\n")

computer_index = r.randint(0,2)
computer = game[computer_index]

print(f"{computer}")


if user_index == 0 and computer_index == 1:
    print("Computer win!")
elif user_index == 0 and computer_index == 2:
    print("User win!")
elif user_index == 1 and computer_index == 0:
    print("User win!")
elif user_index == 1 and computer_index == 2:
    print("computer win!")
elif user_index == 2 and computer_index == 0:
    print("Computer win!")
elif user_index == 2 and computer_index == 1:
    print("User win!")
else:
    print("drop round")


