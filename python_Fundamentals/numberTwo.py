
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
        #print("%s and %s" %(key,value))
        print("first_name - {}, last_name - {} ".format(first_name[x], last_name[x]))

    # for x in range(len(some_list)):
    #     print(students[x])

iterate_dictionary(students)

first_name="Simon"
last_name="van Tulder"
age=24
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
