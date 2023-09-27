'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
x = int(input("Enter a number: "))
#I first made a variable input with x and set it as an integer
if x % 2 == 0 and x > 10:
    print("True")
else:
    print("False")

#I then made a if statement that says if the remainder of x equals 0 and x is greater than 10 then print true else print false.

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''

age = int(input("Enter your age: "))
status = input("Enter student or not student: ")
#i made two variables which would get the age and status
print("")
if age < 18 or status == "student":
    print("The ticket price is 10$")
else:
    print("The ticket price is 20$")
#i made a if statement to check if either they are a student or they are under the age of 18 then it would cost 10$ for the ticket otherwise it would cost 20
'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
fruitlist = ("apple", "banana", "dragonfruit", "watermelon", "pineapple")
#i first made a list of fruits
fruit = input("Enter a fruit name: ")
#i then prompted for a fruit name input
print("")
if fruit in fruitlist:
    print("yes, that fruit is in the list")
else:
    print("No, that fruit is not in the list")

#i then made a if statement to check if fruit was in fruitlist and if it is i would print out "yes. that fruit is in the lst"
'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
year = int(input("Enter a year: "))
# i first made an input that checked for the year
if year % 100 == 0 and year % 4 == 0:
    print("it is a century leap year")
else:
    print("false")
#i then made a if statement that checked if the remainder for both conditionals is equal to zero it would be a century leap year

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

zone = input("Pick between zone A or zone B: ")
weight = int(input("Enter the weight of your package in kg as a integer: "))
#i first made 2 inputs asking for the zone and the weight

if zone == "A":
    if weight > 0:
        print(weight * 5)
    else:
        print("please enter a number greater than 0")
elif zone == "B":
    if weight > 0:
        print(weight * 7)
    else:
        print("please enter a number greater than 0")
else:
    print("Please select a valid zone")
#i made a if statement with nested if statement to check if weight is under 0 and if it is then it would print out an error message and if not then itll print out the product of weight and cost of the zone.

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''

side1 = float(input("Enter sidelength for side 1: "))
side2 = float(input("Enter sidelength for side 2: "))
side3 = float(input("Enter sidelength for side 3: "))
#i made 3 side inputs for the length of the side

if side1 == side2 and side1 == side3:
    print("it is a equilateral triangle")
elif side1 == side2 and side1 != side3 or side2 == side3 and side2 != side1:
    print("It is an isosceles triangle")
elif side1 != side2 or side1 != side3:
    print("This is a scalene triangle")
else: 
    print("not a triangle")

#i made if statement with elifs that checks the lengths of the sides and if 2 sides are the same then its isosceles or if 3 sides are the same then its equilateral or if none of the sides are the same
#then it is a scalene triangle and if none of these apply then it isnt a triangle