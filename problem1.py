#Interactive Calculator Menu

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD = "\033[1m"

BACKGROUNDBLUE = "\033[46m"

while True:
    print("")
   
    print(BOLD+ BACKGROUNDBLUE+ "=" * 10 + " CALCULATOR "+ "=" * 10  + RESET)
    print( "1. Addition" )
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power") 
    print("6. Exit")
    print( BOLD+BACKGROUNDBLUE + "=" * 32 + RESET )

    option = input("Choose an option (1-6): ")
    

    if option =="1" or option=="2" or option == "3" or option =="4" or option =="5":
        number1 = input("Enter first number : ")
        number2 = input("Enter second number : ")

        if number1.isdigit() and number2.isdigit():
            num1 = int(number1)
            num2 = int(number2)

        
            if option == "1":
                result = num1 + num2
                print( GREEN + "Result:", num1, "+", num2, "=", result , RESET)
            elif option == "2":
                result = num1 - num2
                print( GREEN +"Result:", num1, "-", num2, "=", result , RESET)
            elif option == "3":
                result = num1 * num2
                print(GREEN +"Result:", num1, "*", num2, "=", result , RESET)
            elif option == "4":
                if num2 == 0:
                    print( RED + "Error: Cannot divide by zero!" , RESET)
                else:
                    result = num1 / num2
                    print(GREEN +"Result:", num1, "/", num2, "=", result , RESET)
            elif option == "5":  
                result = num1 ** num2
                print(GREEN + "Result:", num1, "raised to the power of", num2, "=", result , RESET)
        else:
            print( RED + "Error: Please enter valid whole numbers." , RESET)

    elif option == "6":
        print(GREEN + "Thank you for using the calculator. Goodbye!" , RESET)
        break

    else:
        print( BOLD+RED + "Invalid option. Please choose a number from 1 to 6." , RESET)

    

    