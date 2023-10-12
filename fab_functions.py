# Task 1: Greeting Function
# Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".

#created function named greet with name argument which can be called later in the print function
def greet(name):
    print("Hello " + name)
#calls the function and prints booby the great as the name argument
print("")
greet("bobby the great")
print("")
print("")

# Task 2: Sum of Two Numbers
# Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.

#created function sum numbers with 2 arguments which can later be used as inputs or replaced by a value
def sum_numbers(a,b):
    #prints a and b mentioned early in argument and adds them together
    print(int(a+b))
#calls the function with 5 and 6 as the argument
sum_numbers(5,6)
print("")
print("")

# Task 3: Calculate Factorial
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.

#creates a function named factorial that uses the argument n
def factorial(n):
    #i first made an input that would take a number input
    num = n
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
#calls the function and uses 4 as an argument
factorial(4)
print("")
print("")

# Task 4: Check Even or Odd
# Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.

#created a function with num as an argument
def is_even(num):
    #created if statement which checks if the remainder of num is equal to 0 and if not it will print odd. If true then itll be even
    if num // 2 == 0:
        print("even")
    else:
        print("odd")

#calls function and 9 is used as argument
is_even(9)

# Task 5: Calculate Area of a Rectangle
# Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.

#creates a calculate area function with the arguments length and width
def calculate_area(length,width):
    #prints length and width's product which is the area of a rectangle
    print(str(int(length) * int(width)) + " is the area of the rectangle")
#calls the function using the parameter 8 and 9 and returns the area of the rectangle
calculate_area(8,9)
print("")