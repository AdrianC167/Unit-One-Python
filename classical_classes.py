"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""

class People():
     def __init__(self, name, age):
          self.name = name
          self.age = age

me = People("Adrian", 201989765435678987654678908765467890876546789087654678909876546786684763852874532745234328747691267892189789738973498737378389749684398349843843893984389438979074894798047865899083427834527854389463249783926749230865438265789326485364863249862348375626)
print(me.name)
print("im " + str(me.age) + " years old")



"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""

class Animal():
    def speak(self):
         print()

class Dog(Animal):
     def speak(self):
         print("woof")

speak = Dog()
speak.speak()
         
class Cat(Animal):
     def speak(self):
         print("meow")
speak = Cat()
speak.speak()




"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

class BankAccount():
    def __init__(self,balance,owner):
          self.balance = balance
          self.owner = owner
    
    def deposit(self, amount):
        self.balance = self.balance + amount 
    def withdraw(self, amount):
        self.balance = self.balance - amount      

bank  = BankAccount(499,"me")     

bank.deposit(7777)

bank.deposit(322)



