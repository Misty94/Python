num1 = 42 
# variable declaration of a number data type
num2 = 2.3
# variable declaration of a float number data type
boolean = True 
# variable declaration of a boolean data type
string = 'Hello World'
# variable declaration of a string data type
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# this is a list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# this is a dictionary
fruit = ('blueberry', 'strawberry', 'banana')
# this is a tuple
print(type(fruit))
# this is a type check & confirms that it is a tuple
print(pizza_toppings[1])
# this prints 'Sausage' which is located at the first index
pizza_toppings.append('Mushrooms')
# this adds the value 'Mushrooms' to the end of the pizza_toppings array
print(person['name'])
# this prints John which is the value of the key 'name'
person['name'] = 'George'
# this changes the value of the key 'name' to 'George'
person['eye_color'] = 'blue'
# this adds a key-value pair to the end of the dictionary person
print(fruit[2])
# this prints 'banana' which is located at the second index of the tuple fruit

if num1 > 45:
    print("It's greater")
# this is a conditional if statement that says if num1 is greater than 45, then print the string "It's greater"
else:
    print("It's lower")
# this is a conditional else statement that says if the if statement above wasn't true, then print the string "It's lower"

if len(string) < 5:
# this is asking if the length of string is less than 5
    print("It's a short word!")
# if the length of string is less than 5, print "It's a short word!"
elif len(string) > 15:
# this is an Else If statement that says if the If statement above wasn't true and the length of string is greater than 15 than...
    print("It's a long word!")
# print "It's a long word!"
else:
# if both the If statement and the If Else statement were untrue, then
    print("Just right!")
# print "Just right!"

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
# variable declaration
while(x < 5):
# this is a while loop -> While x is less than 5
    print(x)
# print x each time 
    x += 1
# x increments by 1 each time & goes back through the loop

pizza_toppings.pop()
# this deletes the last value of the array, which is 'Mushrooms'
pizza_toppings.pop(1)
# this deletes the value at the first index of the array, which is 'Sausage'

print(person)
# this prints the entire dictionary of person
person.pop('eye_color')
# this deletes the key-value pair of eye_color: blue
print(person)
# this prints the entire dictionary of person, which no longer has the key-value pair of eye_color: blue

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)