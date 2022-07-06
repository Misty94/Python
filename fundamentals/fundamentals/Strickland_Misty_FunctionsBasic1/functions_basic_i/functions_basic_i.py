#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# My prediction was 5, and I was right!


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# This one confused me, but I predicted that it would get an error, and I was right; it got an undefined error.


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# I predicted the output would be 5, and I was right!

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# I predicted the output would be 5, and I was right!


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# My prediction was that the output would be 5, 5, and I was halfway right. The real output is 5, None. This is because when a function does not return anything, the output for it is None.


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# My prediction was 3,5,8, and the 3 and 5 did print, but then there was a TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'. After googling this error, I think it means you can't add a string with an integer or vice versa.


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# This one, I predicted 7 and I was completely wrong. It outputted 25, because when it said that the b and c were strings and to add them together, it just put the strings together making the number 25. (So no math for that one.)


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# I predicted the output to be 100 and 10, and I was right!


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# My prediction was 7, 14, 21, and I was right!


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# My prediction was 8, and I was right!


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# My prediction was 500, 500, 300, 500, and I was right!


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# My prediction was 500, 500, 300, 500, and I was right, but when I was writing down my predictions, I did go back and change it after seeing #13.


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# My prediction was 500, 500, 300, 300, and I was right!


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# My prediction was 1, 2, but the real output was 1, 3, 2. I wasn't sure if it would recognize bar() because the function is below the area where it's called. But now I know that the function can be called above the written out function.


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# My prediction was 1, 10, but the actual output was 1, 3, 5, 10. Now I know that the function still works, even if it's being called above where the function is written. I now understand that.