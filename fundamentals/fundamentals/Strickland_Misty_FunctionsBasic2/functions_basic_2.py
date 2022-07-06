# 1) Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(num):
    new = []
    for i in range(num, -1, -1):
        new.append(i)
    return new

# print(countdown(5))
# print(countdown(10))   <- It works!
countdown(5)


# 2) Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def print_and_return(num1, num2):
    print(num1)
    return num2

print_and_return(8,4)
# answer = print_and_return(8,4)
# print(answer)     <- This was just to see if the return worked. It did!


# 3) First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

sum = 0
def first_plus_length(var):
    sum = var[0] + len(var)
    return sum

# print(first_plus_length([1,2,3,4,5]))
# print(first_plus_length([2,4,6,8]))  <- It works!
first_plus_length([2,4,6,8])


# 4) Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False.

def values_greater_than_second(lot):
    new = []
    count = 0
    for i in range(0, len(lot)):
        if len(lot) < 2:
            return False
        if lot[i] > lot[1]:
            new.append(lot[i])
            count += 1
    print(count)
    return new

# print(values_greater_than_second([3]))
# print(values_greater_than_second([5,2,3,2,1,4]))  <- It works!
values_greater_than_second([2,4,6,9,0,3,7])


# 5) This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def length_and_value(size, value):
    new = []
    len(new) == size
    for i in range(0, size):
        new.append(value)
    return new

length_and_value(3, 10)
# print(length_and_value(5,8))  <- It worked!
# print(length_and_value(4, 1))