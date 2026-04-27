import random

choices = ["stone", "paper", "scissor"]

def start_game():
    print("\n----Game Started----")

    user_choice = input("Enter your choice: ").lower()
    if user_choice not in choices:
        print("Invalid choice")
        return
    
    computer_choice = random.choice(choices)
    print(f"Computer choice: {computer_choice}")

    if user_choice == computer_choice:
        print("Match Tied")
    elif (user_choice == "stone" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "stone") or \
         (user_choice == "scissor" and computer_choice == "paper") :
        print("You Win")
    else:
        print("You Lose!")

while True:
    start_game()
    again = input("\n Do you want to play again : yes or no ").lower()

    if again != "yes" :
        print("Thanks for playing")
        break
start_game()