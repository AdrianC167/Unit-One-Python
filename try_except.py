#i put the whole code inside a try and except function to account for the errors
try:
    age = int(input('Enter your age: '))

    faveNum = int(input('What is your favorite number: '))

    if age <= 21:
        print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')

    print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)
#the first except would be for the zerodivision error and when that happens, it would run the code thats inside the except function.
except ZeroDivisionError:
    print("please enter a favorite number other than 0 since you cannot divide by 0")
#same thing here except it would be a value error which means wrong data type and when that happens, the print function would run.
except ValueError:
    print("please enter a your number as an integer like 18 and not eighteen")