"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
#i first made a list with 4 different strings
lok = ["yes", "no", "maybe" , "report"]
#i then made a for loop which would print out each item in the list
for x in lok:
    print(x)

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
#i made a list with 3 numbers
calc = [1, 2, 3]
#i made a sum to keep track of the answer and it would start with 0
sum = 0
#i then made a for loop with the variable y
for y in calc:
    #i made sum equal to sum + y because that would refresh the variable everytime and + y then print it out so it would be adding it all up
    sum = sum + y
    print(sum)
   
print("")
print('')
"""
Exercise 3:
Write a program to find and print the length of each word in a sentence using a for loop and a list.
"""
#i first made a string
count = "adrian is here"
#i then made a variable where it would be equal to the split up count using the spaces in between
b = count.split(" ")
print(b)
#i then made a for loop which uses the len command to print out the characters in every string in the variable b
for yes in b:
    print(len(yes))

print("")
print("")

"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
#i made a dictonary with 4 key values
dict = { 1:"blah", 2:"hack", 3:"boom", 4:"lock"} 
#i then made a for loop that would iterate through dict
for ke in dict:
    print(ke)

#i just get the key and not the value and i was expecting to get the values instead of just the key since the key is just a label.