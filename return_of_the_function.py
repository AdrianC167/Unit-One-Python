"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
#made a function named square using num as the parameter
def square(num):
    #returns num times num
    return num * num

#prints the returned value of 3 squared
print(square(3))
print("")

"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
#created a function named rectangle using length and width as the parameter
def rectangle(length,width):
    #returns length times width
    return length * width
#prints the value of rectangle using the parameter 4 and 7
print(rectangle(4,7))

print("")
"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
#creates a function named fanhrenheit using the temp parameter
def fahrenheit(temp):
    #returns the fahreheit of the celsius using the conversion formula
    return temp * (9/5) + 32
#prints out the fanhrenheit conversion of 2 celsius
print(fahrenheit(2))


"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""
print("")
#creates average function using a as the parameter
def average(a):
    #makes tot equal to the sum of a, which is the parameter
    tot = sum(a)
    #returns tot divided by len of a which tells you how many items are in the list and returns the average
    return tot/len(a)
#prints average while a contains a list value shown by the brackets
print(average([3,4,3,4,9]))
