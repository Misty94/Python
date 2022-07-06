# print("Hello World!")

# x = "Hello Python"
# print(x)
# y = 42
# print(y)

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
pizza_toppings.append('Mushrooms')
# print(pizza_toppings[1])
pizza_toppings.pop()
pizza_toppings.pop(1)
print(pizza_toppings)


fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))
print(fruit[2])


person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
person['name'] = 'George'
print(person['name'])
person['eye_color'] = 'blue'
print(person)
person.pop('eye_color')
print(person)

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)


x = 0
while(x < 5):
# this is a while loop -> While x is less than 5
    print(x)
# print x each time 
    x += 1
# x increments by 1 each time