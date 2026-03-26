#Assignemnt for week 4

#Task 1
#write a program that check if a number is positive, negative and zero. 
# Your program should output 'positive number' for positive number, 
# 'Negavtive number' for negative number and 'zero' for zero. 
# Hint: Use the input function to accept numbers

# number = float(input("Enter a number: ")) # Float is to wrap the value to prevent error when decimal number is being used
# if number > 0:
#     print ("Positive number")    
# elif  (number) < 0:
#     print("Negative number")    
# else:
#     print("zero")

# Task 2
#Using  a for loop, print numbers 1 to 50, and skip only the number 34

# for number in range (51):
#     if number == 34:
#         continue
#     else:
#         print(number)

# Task 3
# Using a while loop, print 'I am backend engineer' 10 times. Set a time delay of 2 seconds after each print

import time
counter = 0
while counter < 10:
    print("I am a backend engineer")
    counter += 1
    time.sleep(2)
