
"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
x = 1
while x < 11:
    print(x)
    x+=1
#i made a variable with the value 1 and then made a while loop that would print x and add one while x is lower than 11.
"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
y = 10
while y > 0:
    print(y)
    y-=1

#i first made a variable and set it as 10 and then made a while loop while y is greater than 0, print y and then subtract 1
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
#i first made an input that would take a number input
num = int(input("Enter a number: "))
#i then set fac to 1
fac = 1
#i then made a while loop so that i can iterate the factorials
while num > 1:
    #i made fac update so that fac would become the result
    fac = fac * num
    #i would then print it out
    print(fac)
    #then i would subtract 1 from num
    num -= 1


        
"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
#i first set a password to nothing so the while loop will run
password = ""

#i made a while loop that will running until password is equal to guess
while password != "guess":
    #i made the variable guess where it would take an input from the user to try and guess the password
    guess = input("guess the password: ")
    #i made an if statement that would see if the input is right and if not then itll give a try again message and continue but if its correct then itll say nice and then break
    if guess == "guess":
        print('nice u got it')
    else:
        print("wrong try again")
        print("")
        continue

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""