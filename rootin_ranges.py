"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
#i wrote a for loop using the range function so that it would start from 1 and end at 10 since 11 is non inclusive
for x in range(1,11):
    print(x)


"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
#i made a for loop using the range function that starts at 900 and ends at 1000 and then increases by increments of 10
for y in range(900,1001,10):
    print(y)


"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
#i made a for loop using the range function that would start at 1 and ends at 100 since 101 is non inclusive and 
# also goes by increments of 9
for z in range(1,101,9):
    print(z)


"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
#i first made the sum equal to 0 outside of the loop so it wont reset
sum = 0
#i then made a for loop with the range 11 which means it would go from 0-10 and 
# then it would add the sum and the current number in the loop and print it out.
for a in range(11):
    sum = sum + a
    print(sum)

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5

for i in range(rows):
    for j in range(i+1):
        print('*', end=' ')
    print()


#the output was * which increases by 1 every iteration

#first rows is set to 5. The first for loop just tells how many iterations it does and in this case it starts from 0-4
# The second for loop is for how many times the star is printed and the range just tells you how many to print because
# i starts off as 0 and when you add 1 that would mean it starts off with 1 star instead of 0. The print statement is part of the for loop and tells the for loop what to print
# the reason i changes is because the loop is iterating everytime the first loop iterates which means i would always increase.    