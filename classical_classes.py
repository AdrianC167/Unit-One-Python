"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
#creates a class named people
class People():
     #uses a method which creates the object and also functions name and age
     def __init__(self, name, age):
          #creates the two variables name and age using the self. which tells the computer its talking about itself
          self.name = name
          self.age = age
#calls the people class with the name and age values inside the parameter and sets it equal to me
me = People("Adrian", 201989765435678987654678908765467890876546789087654678909876546786684763852874532745234328747691267892189789738973498737378389749684398349843843893984389438979074894798047865899083427834527854389463249783926749230865438265789326485364863249862348375626)
#prints out name from the me variable
print(me.name)
#prints out a string including the me.age which will pull self.age from the people class.
print("im " + str(me.age) + " years old")



"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""

#creates a class named animal
class Animal():
    #creates a method containing nothing and the print is just a placeholder
    def speak(self):
         print()
#creates dog as a child class of the animal class
class Dog(Animal):
     #creates a method that would print out woof
     def speak(self):
         print("woof")
#calls the fuction dog and sets it to speak
speak = Dog()
#calls out the function here and that runs the print function within the method
speak.speak()

#creates cat as a child class of animal class         
class Cat(Animal):
     def speak(self):
         print("meow")
#calls the fuction cat and sets it to speak         
speak = Cat()
#calls out the function here and that runs the print function within the method
speak.speak()




"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
#creates a class named BankAccount
class BankAccount():
    #creates a method using the init function which creates the objects balance and owner
    def __init__(self,balance,owner):
          #attributes are created so later can be called and modified accorrdingly 
          self.balance = balance
          self.owner = owner
    #creates method for deposits with amount as a parameter
    def deposit(self, amount):
        #resets attribute balance to current balance + new amount
        self.balance = self.balance + amount 
    #creates a withdraw method with amount as attribute again
    def withdraw(self, amount):
        #calls the balance attribute and resets it to current balance subtracting the withdraw amount
        self.balance = self.balance - amount      
#sets value for both attributes
bank  = BankAccount(499,"me")     
#deposits 777 into bankaccount
bank.deposit(7777)
#withdraws 322 from bankaccount
bank.withdraw(322)



