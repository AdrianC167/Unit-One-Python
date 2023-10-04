#i first made a list with no value inside to be the todo list
todos = []
#i imported sleep so i can use later on for delay on the else statement
import time
t = 2



#notes:i tried the first time but it didnt work since i needed a variable to make it easier and i also needed to make it a string since it didnt work

#now i will make a while loop that will always run which means i will have to set it to while true
while True:
    #i now made a print statement which will call the todos that we have currently and print it and after that i made some empty space prints
    print("Your current todos are: ")
    #the x variable is set to zero so that it resets every loop
    x = 0
    #i made a for loop which would display every todo in its own line with a number before that which is what the x variable is for
    for list in todos:
        x = x + 1
        print(str(x) + ". " + list)
    print("")
    print("")
    #im now making an input which would ask for a user input to tell you whether you want to add or remove
    func = input("Would you like to add or remove? ")
    #im now making a if function that would say if the input is equal to add then it would take an input from the user
    #asking for the new input then append it to the list
    if func == "add":
        new = input("what is your new todo? ")
        todos.append(new)
        print("")
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
    #im an elif for when function is equal to remove so i can then delete stuff from the list.
    elif func == "remove":
        print("")
        #i made a variable so that i could ask for a integer input of the number they wish to remove.
        delete = int(input("Please select the number you wish to delete: "))
        #i made a if statement which will check if the number inputted is less than 0 or equal to it and if it is then it give return an error
        if delete <= 0:
               print("")
               print("please enter a whole number greater than 0")
               print("")
               print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
               time.sleep(t)
        else:
            index = int(delete - 1)
            #i then delete the input they put in and add 2 empty spaces
            del todos[index] 
            print("")
            print("")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("")
    #the else statement is just for when someone enters the wrong inputs
    else:
        print("")
        #i made the error print more specific
        print('please enter a valid choice(pick between "add" or "remove")')
        #i added a delay before the next loop runs to give the user time to read
        time.sleep(2)
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")

    
