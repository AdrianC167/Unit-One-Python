"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
num = 4.2
num2 = int(num)
print(num)
print(num2)

# made a random float and called it num then made another var and called it num2 then made it equal to int(num) which would convert the float to integer and then i printed both.


"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
x = int(input("give me a number "))

if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")
    
# i first made a var that requested an input and coverted it with the int command so it was an integer then i made an else if that would print negative if it was less than zero and positive if it was greater than 0 and anything else would be zero.


"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
num3_1 = (int(input("enter a whole number ")))
num3_2 = (float(input("enter a decimal number ")))
print(num3_1 * num3_2)
print(num3_1 + num3_2)
print(num3_1 - num3_2)
print(num3_1/num3_2)

# i first made two inputs where one was converted into a int while the other was a float and then i printed every single one out with their respective math signs and result.

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""

fruits = { 

'watermelon': 3,
'pineapple': 4,
'apples': 320

}

print(fruits["apples"])

# i first made a dictionary called fruits and made 3 keys and assigned a value to all 3 then i printed out the value of fruits

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

ognum = "1.2.3.4.6.8.7.9.10"
newnum = ognum.split(".")

print(ognum)
print(newnum)