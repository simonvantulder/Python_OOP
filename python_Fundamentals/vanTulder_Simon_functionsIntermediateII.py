# person = {
#     "name": "Shawn",
#     "age": 27,
#     "interests": ["music", "coding", "video games"],
#     "address": {
#         "street": "123 Shawn St",
#         "state": "CA",
#         "city": "San Jose"
#     }
# }


# for variable in person:
#     print(person[variable])
# print("****************************************************************")
# for key, value in person.items():
#     print("%s and %s" %(key,value)) #modulus "s" for string "d" for digit  first one for key second for value close quotes modulus sign key,value
#     # print("-------")
#     # print(f"{key} and {value}")





# person[1][2] # for lists/arrays in python or other use [index] for index of desired list then use [index] of sublist
# person["interests"][1] # for python dictionaries use [""] for the key (dont forget the quotes"") then use the index of the value desired if within a list

# #1
# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# # Change the last_name of the first student from 'Jordan' to 'Bryant'
# # In the sports_directory, change 'Messi' to 'Andres'
# # Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 
students = [{'first_name':  'Michael', 'last_name' : 'Jordan'}, {'first_name' : 'John', 'last_name' : 'Rosales'}]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Shilton', 'Ronaldo', 'Rooney','Messi']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x)


students[1]["last_name"]="Bryant"
print(students)

sports_directory["soccer"][0]="Hazard"
sports_directory["soccer"][1]="Debruyne"
sports_directory["soccer"][2]="Kompany"
sports_directory["soccer"][3]="Lukaku"
print(sports_directory)

z[0]["y"]=30
print(z)


#2   Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:


students = [
        {'first_name':  'Michael', 'last_name': 'Jordan'}, 
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
#iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterate_dictionary(some_list):


    
    for x in some_list:
        for key, value in x.items():
            print("{} - {}".format(key, value))

iterate_dictionary(students)

#3  Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
students = [
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name': 'John', 'last_name' : 'Rosales'},
    {'first_name': 'Mark', 'last_name' : 'Guillen'},
    {'first_name': 'KB', 'last_name' : 'Tonel'}
    ]
#x=students[0]["first_name"]
# print(x)
def iterate_dictionary2(key_name, some_list):
    for student in some_list:
        if key_name in student:
            print(student[key_name])
        else:
            print("Key not found in dictionary")

key_name = 'frog'
iterate_dictionary2(key_name, students)


#4   Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

def print_info(some_dict):
    for x in some_dict:
        # print("%d %s" %(len(x), x)
        # print("%s" %(some_dict[x]))
        print("%d %s %s" %(len(some_dict[x]), x, some_dict[x]))
        for y in range(len(some_dict[x])):
            print("{}".format(some_dict[x][y]))


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print_info(dojo)


