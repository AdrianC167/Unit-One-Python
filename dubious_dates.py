#i first imported the datetime module
import datetime

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
#i then made a variable and set it to x then used the datetime.datetime.now to get the current time and set it to x
x = datetime.datetime.now()
#i then printed x which is equal to the time
print(x)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
#i first made a x variable and then used the x.strftime function to format the time into the standard month day and year format. 
#formats are shown using the %m and so on that are found on the module documentation
x = x.strftime("%H:%M:%S %m/%d/%Y")
#prints the new x
print(x)

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
#made 2 variables with 2 seperate dates and both set as strings
data = "12/15/3100"
data2 = "12/17/3100"
#created a format using month/day/year
format = "%m/%d/%Y"

#made time variable and set it equal to the datetime.strptime which takes data and puts it in the format variable i made the previous line
time = datetime.datetime.strptime(data, format)
#seperate variable for both datas since it wont work together
time2 = datetime.datetime.strptime(data2, format)
#print the difference of time2 and time
print(time2 - time)

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
#i first made an input value and set it to bday
bday = input("What is your birthday?(Enter in month/day/year format): ")
#made x and set it todatetime.datetime.now which gets the current time
x = datetime.datetime.now()
#created format and set as a variable
format = "%m/%d/%Y"
#used strptime to format bday into time
bday = datetime.datetime.strptime(bday, format)
#print out the difference between current time and bday and print out bday
print("you are currently" + str(x - bday)+ " hours old.")

