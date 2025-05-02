import random
stone = '''
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


game_images = [stone, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Stone, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

Bot_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[Bot_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and Bot_choice == 2:
  print("You win!")
elif Bot_choice == 0 and user_choice == 2:
  print("You lose")
elif Bot_choice > user_choice:
  print("You lose")
elif user_choice > Bot_choice:
  print("You win!")
elif Bot_choice == user_choice:
  print("It's a draw")
