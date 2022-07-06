for i in range(5):
    print(i)

cakes = ["chocolate", "vanilla", "strawberry", "tuxedo"]

for i in range(len(cakes)):
    print(f"{i+1}) {cakes[i]}")

list_num = 1
for cake in cakes:
    print(f"{list_num}) {cake}")
    list_num += 1


# looping over dictionary
student = {
    "name": "Pablo",
    "awesomeness": 9001
}

for key in student:
    print(f"{key} : {student[key]}")

if "name" in student:
    print("Student has a name")
else:
    print("Who?")

num = 1
while num < 10:
    print(num)
    num+=1
# while loops are good for when you don't know when they'll end or when you're checking a condition


# functions

def add(num1, num2):
    x = num1 + num2
    # print(x)
    return x

print(add(2,3))

def add(num1, num2):
    x = num1 + num2
    print(x)
    # return x

print(add(2,3)) # 5 None because no return


def add_three(num1, num2=3):
    print(num1)
    print(num2)
    return num1 + num2

print(add_three(5))

print(add_three(8,4))

print(add_three(num1=8, num2=4))


# debugging

def multiply(num_list, num):
    # print(num_list, num)
    for i in range(len(num_list)):
        x = num_list[i]
        x *= num
        num_list[i] = x
        # print(num_list)
    return num_list
a = [2,4,10,16,8]
b = multiply(a, 5)

def emptyfunction():
    pass


student = {
    "first_name" : "Alex",
    "last_name" : "Hillier",
    "age" : 20,
    "grade" : 9.6,
    "stick" : "Python/Flask",
    "passed" : True,
    "class" : {
        "subject" : "math",
        "instructor" : "Pablo",
    }
    "number" : [1,2,3,4,5],

}

print(student["class"]["subject"])
print(student["number"][2])


# notes

def be_cheerful(name="Honey", repeat=2):
    print(f"Good morning {name}\n" * repeat)        # \n makes a new line in the terminal!

be_cheerful("Misty")
be_cheerful()
be_cheerful(repeat=4, name="Billy Bob")