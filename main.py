#Assignment

#Task 1 Declare three variables to hold the names of cars.

car1 = "Ford"
car2 = "Benz"
car3 = "Toyota"

#Task 2 Print all three variables
print(car1)
print(car2)
print(car3)

#Task 3 Declare anothe variable to combine the values of the previous three variables
cars = car1 + " " + car2 + " " + car3

#Task 4 Print the content of the single variable in question 3  
print(cars)
#Task 5 Use help()function to discover methods of the str class
print(help(str))

#Task 6 Show examples of five other string methods besides the ones we used in class

#Str method 1: It check if the variable is a number
numbers = "0.9032"

num = numbers.isdecimal()

print(num)

#Str method 2
num = "50"
result = num.zfill(10)
print(result)

#Str method 3
# ASCII are alphabet and numbers" and it checks it the variable is ASCII
name = "opeyemiEesuola010"

my_name = name.isascii()

print(my_name)

#Str method 4: isprintable: It check if the text in the variable can be printed
message1 = "Hi, my name is Opeyemi 	\x0A Eesuola"
message = "Hi, my name is Opeyemi Eesuola"
message2 = "Hi, my name is Opeyemi \n Eesuola"
x = message2.isprintable()
print(x)

#Str method 5: replace: It replace a value in a variable
favorite= "I like reading docs"

x = favorite.replace("docs", "books")

print(x)