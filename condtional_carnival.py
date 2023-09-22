'''
TASK 1 Even or Odd
Determine if a number is even or odd.
'''
num = int(input("Enter a number: "))
numres = num % 2

if numres > 0:
    print("your number is odd")
else:
    print("your number is even")

#i first a variable that requested a input and set it as a integer so i could do math with it then i made another variable and used the remainder function to determine whether its even or not. if it has a remainder while being
#divided by two then it is odd.
'''
TASK 2 Positive, Negative, or Zero:
Determine if a number is positive, negative, or zero.

EXTRA CREDIT: Tell the user if they did not enter a valid number
'''


try: 
    num2_1 = float(input("enter a number: "))
    if num2_1 < 0:
        print("Negative")
    elif num2_1 > 0:
        print("Positive")
    else:
        print("Zero")

except ValueError:
    print("Please enter a valid number")




#i first made a input value with the int command and then made a if function which checked whether the number is greater or less than 0 or equal to zero. I first put it in a try and except clause and if an error occured it would be overwritten by the except value error clause and come back as please enter a value number.

'''
TASK 3: Largest of Three
Find and print the largest of three numbers.
'''
x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))
z = int(input("Enter a value for z: "))

print(max(x,y,z))

#i first made 3 inputs while making them integers then i printed it out while using the max function to determine the highest of x,y,z
'''
TASK 4: Leap Year
Determine if a year is a leap year or not.
'''
days = int(input("enter the days in this year: "))

if days == 365:
    print("It is not a leap year")
elif days < 365: 
    print("It is not a leap year")
else: 
    print("It is a leap year")

#i first made a variable and set it to 365 days then if the days if equal to 365 then it is not a leap year and if its not then its a leap year.
'''
TASK 5: Vowel or Consonant:
Identify if a character is a vowel or consonant.

EXTRA CREDIT: Tell the user if they did not enter a valid letter
'''


character = input("enter a character: ")
  

if character == "a" or character == "e" or character == "i" or character =="u" or character == "o" or character == "A" or character == "E" or character == "I" or character =="U" or character == "O":
    print("Vowel")
elif character == "b" or character == "c" or  character == "d" or  character == "f" or  character == "g" or  character == "h" or  character == "j" or  character == "k" or  character == "l" or  character == "m" or  character == "n" or character == "p" or  character == "q" or  character == "r" or  character == "s" or  character == "t" or  character == "v" or  character == "w" or  character == "x" or  character == "y" or  character == "z" or character == "B" or character == "C" or  character == "D" or  character == "F" or  character == "G" or  character == "H" or  character == "J" or  character == "K" or  character == "L" or  character == "M" or  character == "N" or character == "P" or  character == "Q" or  character == "R" or  character == "S" or  character == "T" or  character == "V" or  character == "W" or  character == "X" or  character == "Y" or  character == "Z":
    print("Consonant")
else:
    print("Please enter a valid letter")

#i first made a input as a string the i made a if statement then i individually added a character == letter and combine them all with a or condtion and then i added all the letters and anything else would not work. I added capitals just in case as well.