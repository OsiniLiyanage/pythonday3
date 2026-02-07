#hanced Guessing Game

import random


while True:

    print("")
    print("")
    print("===== NUMBER GUESSING GAME =====")
    print("Choose difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")
    
    choice = input("Your choice: ")


    if choice == "1":
        min_num = 1
        max_num = 50
        max_attempts = 10
        print("Great! I'm thinking of a number between", min_num, "and", max_num)
        print("You have", max_attempts, "attempts. Good luck!")

    elif choice == "2":
        min_num = 1
        max_num = 100
        max_attempts = 7
        print("Great! I'm thinking of a number between", min_num, "and", max_num)
        print("You have", max_attempts, "attempts. Good luck!")
    elif choice == "3":
        min_num = 1
        max_num = 200
        max_attempts = 5
        print("Great! I'm thinking of a number between", min_num, "and", max_num)
        print("You have", max_attempts, "attempts. Good luck!")
    else:
        print("Invalid choice.Please choose level 1 to 3.")
        
    
    correctnumber = random.randint(min_num, max_num)
    attempt = 1
    guessed_correctly = False

   
    
    while attempt <= max_attempts and not guessed_correctly:
        guessnumber = input("Attempt " + str(attempt) + "/" + str(max_attempts) + " - Enter your guess: ")
        
        
        if guessnumber.isdigit():
            guess = int(guessnumber)
            
            
            if guess < min_num or guess > max_num:
                print("Please enter a number between", min_num, "and", max_num)
            else:
                
                if guess == correctnumber:
                    print("")
                    print("  \\o/  YOU WIN!   \\o/")
                    print("   |    Great job! |")
                    print("  / \\             / \\")
                    print("")
                    print("You guessed it in", attempt, "attempts!")
                    guessed_correctly = True
                elif guess > correctnumber:
                    print("Too high! Try again.")
                    
                    if guess - correctnumber <= 5:
                        print("But you're getting close!")
                else:  
                    print("Too low! Try again.")
                    
                    if correctnumber - guess <= 5:
                        print("But you're getting close!")
                
                attempt = attempt + 1
        else:
            print("Error: Please enter a valid whole number.")
          
            continue  



    if not guessed_correctly:
        print("")
        print("  --- GAME OVER ---")
        print("You ran out of attempts!")
        print("The number was:", correctnumber)
        print("  -----------------")
        print("")

    
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break