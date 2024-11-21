import random
while True:
 def guess_the_number():
     random_number = random.randint(1, 100)
     
     print("Welcome to the Guess the Number Game!")
     print("I have selected a random number between 1 and 100.")
     
     guess = None
     while guess != random_number:
         try:
             guess = int(input("Enter your guess: "))
 
             if guess < 1 or guess > 100:
                 print("Please guess a number within the range of 1 to 100.")
             elif guess < random_number:
                 print("Too low! Try again.")
             elif guess > random_number:
                 print("Too high! Try again.")
             else:
                 print(f"Congratulations! You've guessed the number: {random_number}")
         except ValueError:
             print("Please enter a valid integer.")
 
 guess_the_number()
