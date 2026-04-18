#Task 1
class Animal:
    """ANIMAL MODEL"""
    def __init__(self, name,gender,classes,sound):
        self.name = name
        self.gender = gender
        self.classes = classes
        self.sound = sound
    """Method to describe the animal"""
    #Task 3
    def describe(self):
        return f"This animal called {self.name}, belongs to a class of {self.classes}.This is a {self.gender}"
    def can_speak(self):
        """This method describe the sound it makes"""
        return f"This {self.name} makes a {self.sound} sound"
    
animal = Animal('Parrot', 'Male', 'Bird', 'gurles & Whistles')
print(animal.name, animal.gender, animal.classes, animal.sound)
print (animal.describe())
print (animal.can_speak())

#Task 2
"""This is a subclass called Dog that will inherit the superclass"""
class Dog(Animal):
    """This model the subclass called Dog"""
    def __init__(self, name, gender, classes, sound):
        super().__init__(name, gender, classes, sound)
    """This method is to tell the sound the suclass Dog make"""
    def can_speak(self):
        return super().can_speak()
    #Task 3
    def info(self):
        """This gives an extra info on this subclass"""
        return f"This animal {self.name} is a loyal animal"

dog = Dog('Bunny', 'Female', 'Mammal', 'Woolf')

print(dog.name, dog.gender,dog.classes, dog.sound)
print(dog.can_speak())
print(dog.info())

# Task 2
"""This is a subclass called Dog that will inherit the superclass"""
class Cat(Animal):
    """This model the subclass Cat that will takes parameters from the Parent class"""
    def __init__(self, name, gender, classes, sound):
        super().__init__(name, gender, classes, sound)
        """This method is about the sublcass class named Cat"""
    def can_speak(self):
        return super().can_speak()
    
    def info(self):
        """This gives an extra info on this subclass"""
        return f"This animal {self.name} is an independent animal"

cat = Cat('Perry', 'Male', 'Mammal', 'Meow')
print(cat.name, cat.gender, cat.classes, cat.sound)
print(cat.can_speak())
print(cat.info())

#Task 4
"""This is Polymorphism. One of the OOP principles"""

def animal_sound(animal):
    """This is a functiona that takesm an object as an argument and calls the can_speak method on it"""
    print(animal.can_speak())


animal_sound(dog) 
animal_sound(cat)  
animal_sound(animal)  

