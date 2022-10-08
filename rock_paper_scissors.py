import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____) <-- Rock
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______) <-- Paper
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________) <-- Scissors
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]


while True:
  user_selection = input("Pick 0 for rock, 1 for paper, and 2 for scissors: ")
  if user_selection.isdigit():
    user_selection = int(user_selection)
    if 0 <= + user_selection <= 2:
      break
    elif user_selection > 2:
      print("You cant pick more than the number 2")
  else:
    print("Please enter a number")
    
print("you selected:")
print(game_images[user_selection])


computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_selection == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_selection == 2:
  print("You lose")
elif computer_choice > user_selection:
  print("You lose")
elif user_selection > computer_choice:
  print("You win!")
elif computer_choice == user_selection:
  print("It's a draw") 
