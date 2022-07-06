# 1. Update Values in Dictionaries and Lists
"""
1) Change the value 10 in x to 15.
2) Change the last_name of the first student from 'Jordan' to 'Bryant
3) In the sports_directory, change 'Messi' to 'Andres'
4) Change the value 20 in z to 30
"""

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
# print(x)
students[0]['last_name'] = 'Bryant'
# print(students)
sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)
z[0]['y'] = 30
# print(z)

# 2. Iterate Through a List of Dictionaries
"""
Create a funtion that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.
"""

characters = [
    {'first_name': 'Harry', 'last_name': 'Potter'},
    {'first_name': 'Hermione', 'last_name': 'Granger'},
    {'first_name': 'Ron', 'last_name': 'Weasley'}
]

def iterateDictionary(some_list):
    for i in range(len(some_list)):
        emptyStr = ""
        for k,v in some_list[i].items():
            emptyStr += f" {k} - {v}"
        print(emptyStr)

iterateDictionary(characters)
    #iterate through the array
    # get into each dictionary
    #get the key in that dictionary
    # for i in range(len(some_list)):
        # print(i) <- printed the indexes
        # print(some_list[i]) <- printed each dictionary
        # print(some_list[i]["first_name"]) <- printed the first names only
        # for key in some_list:  <- this & below printed out each dictionary * 3
        #     print(key)
        # for key in some_list[i]: # <- this & below printed out each key in each dictionary
            # print(key)
            # print(some_list[i][key], some_list[i]["first_name"], some_list[i]["last_name"])
            # print(key)
            # print(some_list[i]["last_name"])
            # print(f"(key) ")
            # for val in some_list[i]:
            #     print(val)
    # for i in range(len(data)):

        # for i, j in characters.items(): <- This works for dictionaries
        #     print(i, j)



# def iterateDictionary(some_list):
# def iterateDictionary(some_list):
#     for i in range(len(some_list)):
#         for value in some_list[i]

    # Kayla's Help
# def iterateDictionary(data):
#     for entry in data:
#         for key, value in entry.items():
#             print(key, "-", value)

# iterateDictionary(characters)

    # Google Help
# def iterateDictionary(some_list):
#     for i in range(len(characters)):
#         print(i)
#         print('\n'.join("{}: {}".format(k, v) for k, v in characters[i].items()))

# print(iterateDictionary(characters))


# def iterateDictionary(some_list):
#     list_num = 0
#     for character in characters:
#         print(f"{list_num} {character}")
#         list_num += 1

# print(iterateDictionary(characters))

    # for i in range(len(some_list)):
    #     for value in some_list[i]:
    #         for y in some_list[i]:
    #             print("first_name"+ " - "+ some_list[i]["first_name"]+", "+ "last_name"+" - "+ some_list[i]["last_name"])

    # for dic in characters:
    #     for val in dic.values():
    #         print(val)
    # for i in range(len(characters)):
    #     for key in characters[i]:
    #         print(characters[i][key])
    #         for val in characters[i]:
    #             print(characters[i][val])
    # for dic in characters:
    #     for key in dic:
    #         print(dic[key])







    # for i in range(0, len(characters)):
    #     for key in characters[i]:
    #         print(key)
    #         for val in characters[i]:
    #             print(val)
        # print(['first-name'])
        # print(characters[i])
        # print(characters[i]['last_name'])
        # print(str("-"))
#     for key, val in characters.items():
#         


# 3. Get Values From a List of Dictionaries
"""
Create a function that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.
"""
friends = [
    {'first_name': 'Kenia', 'last_name': 'Reveria'},
    {'first_name': 'Tom', 'last_name': 'Harris'},
    {'first_name': 'Elijah', 'last_name': 'Hendrickson'},
]



def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(friends[i][key_name])
        # for val in dict.values:
        #     print()

print(iterateDictionary2('first_name', friends))
print(iterateDictionary2('last_name', friends))



# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. 

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for each_key in some_dict:
        # print(len(each_key), each_key)
        print(f"{len(some_dict[each_key])} {each_key.upper()}")
        for val in some_dict[each_key]:
            print(val)
        # for i in range(len(each_key)):
        #     print(["locations"][i])

printInfo(dojo)


# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

