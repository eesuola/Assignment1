# #Task1

# #Create a list called fruits with at least 5 different frtuits

# fruits = ["Apple", "Watermelon", "Orange", "Banana","Paw paw"] 

# #print the first fruit
# #print the last fruit
# #print the third fruit

# print(fruits[1])
# print(fruits[4])
# print(fruits[3])

# #Task 2

# numbers =  [10,20,30,40,50,60,70]
# #Print the first 3 numbers
# #Print the last 3 numbers
# #Print everything except the first and last number
# print(numbers[:3])
# print(numbers[4:])
# print(numbers[1:6])

# #Task 3 Create a list

# color = ["red", 'blue', "green"]
# #Add "Yellow" to the end
# #insert "Purple" at index 1
# #Change "green" to "black"

# color.append("Yellow")
# print(color)
# color.insert(1, "Purple")
# print(color)

# if "green" in color:
#     index = color.index("green")
#     color[index] = "Black"

# print(color)

# #Task 4 Removing
# animals =["dog", "cat","rabbit", "lion", "cat"]
# # #remove the first "Cat"
# # animals.pop(0)
# # print(animals)
# # #remove "lion" using a method
# # animals.remove('lion')
# # print(animals)
# # #remove the last item in the list
# animals.pop(4)
# print(animals)

# # Task 5 Create a kist of numbers

scores = [50,20,80,40,90]

#Sort the list in ascending order
# scores.sort(reverse=False)
# print(scores)

# #Sort the list in descending order
# scores.sort(reverse=True)
# print(scores)

#Reverse the list
scores.reverse()
print(scores)
