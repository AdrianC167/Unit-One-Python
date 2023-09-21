"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
list = [1,2,3,4]
print(list)

#i created a list and added 4 values inside it and then printed it

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
list.append(5)
print(list)

#i appended 5 to the list then i printed it
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
list.remove(5)
print(list)

#i removed 5 from the list then printed it
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
list[3] = 3
print(list)

# i first selected index number 3 in the list and then changed it to 3 and then printed it

"""
Task 5: Append Multiple Elements to the List
Append multiple elements to the end of the list. Print 
the updated list.
"""

list.append(4)
list.append(5)
list.append(6)
list.append(7)
list.append(8)
list3 = list
print(list3)


#i first made a new list and then made a third list that adds both them together and printed that new list
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
del list3[3]
print(list3)

# i first used the del command on list3 and removed the 3rd item in the list and then printed it
"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
list4 = list3[0:2]
print(list4)

#i made a new variable and made it equal to the first two items of list3 using the 0:2 command

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""

list5 = [9,10,11]
list6 = list3 + list5
print(list6)

#i made a 6th list and then added two list together.