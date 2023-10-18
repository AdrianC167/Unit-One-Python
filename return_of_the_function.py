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

#i put the asserts inside a try and except assertionerror function which will print in a easier to read message when the function
#isnt working as intended.
try:
    #assert function of the square with parameter 3 and if it isnt equal to 9 then return assertionerror
    assert square(3) == 1
    #same assert exception square will have a parameter of 4 instead and should equal to 16
    assert square(4) == 16
except AssertionError:
    print("The square function is not working as intended please check it again.")

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

#asserts the rectangle function with parameters 2 and 3 and should return 6
assert rectangle(2,3) == 6 
#asserts the rectangle function with the parameter 4 and 3 and should return the product of 12
assert rectangle(4,3) == 12


"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
#creates a function named fanhrenheit using the temp parameter
def fahrenheitconvert(temp):
    #returns the fahreheit of the celsius using the conversion formula
    return temp * (9/5) + 32
#prints out the fanhrenheit conversion of 2 celsius
print(fahrenheitconvert(2))

#assert the fahrenheit function with the parameter of 0 which should return 32 fahrenheit
assert fahrenheitconvert(0) == 32
#asserts the function with the parameter of 1 and should return 33.8
assert fahrenheitconvert(1) == 33.8
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

#asserts the average function with the parameters of 3,4,5,2 and that should return 3.5
assert average([3,4,2,5]) == 3.5
#asserts the average function with the parameters of 1,2,3,4 and should return 2.5
assert average([1,2,3,4]) == 2.5
