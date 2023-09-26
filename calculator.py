# i first put everything inside a try and except valuerror command so that i can tell the user when the input is not of the right type. 
try:

# i then made 2 inputs and named them num and num2 and also made them as floats in case a decimal is inputed.

    num = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))


# I then added some blank spaces to make it look better on the eyes at mr forlenzas requests

    print("")
    print("")
    print("")

# i then created a list(as in ordered list) of the choices and added a number before it

    print("pick an operation from the list below:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Exponents")
    print("7. Remainder")
    print("")
    print("")


# i made a input so that they can select a choice from the list
    choice = int(input("Pick your number from the list: "))

# i then made a if statement with many elifs matching the number to the operation they chose in the input i just made before the if statements.
# i then under every if statement i would use the right operator in the print function.
# i finally added a else statement incase they choose an invalid option from the list.
    if choice == 1: 
        print(num + num2)
    elif choice == 2:
        print(num - num2)
    elif choice == 3:
        print(num * num2)
    elif choice == 4:
    # with division i made a if statement under the elif so that i could give out a different response in case 0 is the denominator.
        if num2 == 0:
            print("I cannot calculate that")
        else:
            print(num / num2)
    elif choice == 5:
        print(num // num2)
    elif choice == 6:
        print(pow(num,num2))
    elif choice == 3:
        print(num % num2)
    else:
        print("Please select a valid number from the list")


# i then finished off the  program using except valueerror and then printing out to enter a valid number incase the inproper input was given.
except ValueError:
    print("Please enter a valid number not a letter")

