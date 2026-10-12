import random

choices = ["rock","paper","scissor"]

while True:
    print("---Rock Paper Scissors Game---")
    print("Choices :", choices)
    user_choice = input("Enter a Choice(write quit to exit)").lower()

    if user_choice == "quit":
        print("Game Over")
        break
    if user_choice not in choices:
        print("invalid choice, write another!!")
        continue

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        print(f"User Choice {user_choice} vs. Computer Choice {computer_choice} = Draw")
    elif(
        user_choice == "rock" and computer_choice == "scissor"
        or user_choice == "scissor" and computer_choice == "paper"
        or user_choice == "paper" and computer_choice == "rock"):
        print(f"User Choice {user_choice} vs. Computer Choice {computer_choice} = User Win")
    elif(
         user_choice == "scissor" and computer_choice == "rock"
        or user_choice == "paper" and computer_choice == "scissor"
        or user_choice == "rock" and computer_choice == "paper"):
        print(f"User Choice {user_choice} vs. Computer Choice {computer_choice} = Computer Win")
    
       


