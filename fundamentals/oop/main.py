# from package_name (folder) import module/variable/function/class
# from classes.animal import name, gretting <- this one didn't work, but teacher's worked

# print(name)

# gretting()

# from classes import animal

# print(animal.name)

# animal.greeting()

from classes.animal import Animal 
from classes.dog import Dog
from classes.cat import Cat

# first_name = input( "Please give me your first name: " )
# print(f"It's nice to meet you {first_name}")
# input the name in the terminal


# from classes import animal, dog, cat

# from classes import animal

# max = animal.Animal("Max", "Alex", "Labrador")
# max.print_info()

# jagger = dog.Dog("Jagger", "Alfredo", "Golden Retriever", "Golden")
# jagger.print_info()
# jagger.walk_animal()

# chester = cat.Cat("Chester", "Alfredo", "Yellow", 6)
# chester.print_info()
# chester.walk_animal()

print("****MENU OF OPTIONS*****")
print("0) EXIT this program")
print("1) Add a CAT")
print("2) Add a DOG")
print("3) Print all dogs")
print("4) Print all cats")
option = input("Select an option: ")

while option != "0":
    if option == "1":
        name = input("Name of your cat: ")
        owner = input("Who is the owner? ")
        breed = input ("What's the breed? ")
        age = input("Age of the cat: ")
        new_cat = Cat(name, owner, breed, age)
    elif option == "2":
        name = input("Name of your dog: ")
        owner = input("Who is the owner? ")
        breed = input ("What's the breed? ")
        color = input("What's the color? ")
        new_dog = Dog(name, owner, breed, color)
    elif option == "3":
        Dog.print_all_dogs()
    elif option == "4":
        Cat.print_all_cats()



    print("0) EXIT this program")
    print("1) Add a CAT")
    print("2) Add a DOG")
    option = input("Select an option: ")
