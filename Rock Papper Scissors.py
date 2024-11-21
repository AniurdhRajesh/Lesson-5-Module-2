import random
while True:
 def play_rock_paper_scissors():
     options = ["rock", "paper", "scissors"]
     computer_choice = random.choice(options)
     
     user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
     
     if user_choice not in options:
         print("Invalid choice! Please try again.")
         return
     
     print(f"Computer chose: {computer_choice}")
     
     if user_choice == computer_choice:
         print("It's a tie!")
     elif (user_choice == "rock" and computer_choice == "scissors") or \
          (user_choice == "paper" and computer_choice == "rock") or \
          (user_choice == "scissors" and computer_choice == "paper"):
         print("You win!") 
     else:
         print("You lose!")

 play_rock_paper_scissors()
