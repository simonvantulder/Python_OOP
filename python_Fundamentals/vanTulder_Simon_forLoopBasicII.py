#1
list1=[37,2,1,-9]
#list1= [-1,3,5,-2]
def biggySize(list1):
    for x in range(0,len(list1)):
        if list1[x]>0:
            list1[x]="big"
    return list1
#print(biggySize(list1))

#2
#fruits=[-1,2,4,3,10]
def CountPositives(fruits):
    count=0
    for x in range(len(fruits)):
        if fruits[x]>0:
            count+=1
    fruits[len(fruits)-1]=count
    return fruits
#print(CountPositives(fruits))

#3
#list1=[1,2,3,4,5]
def sum_total(list1):
    sum=0
    for x in range(len(list1)):
        sum+=list1[x]
    return sum
#print(sum_total(list1))

#4
#list1=[1,2,3,4,5]
def average(list1):
    count=sum=0
    
    for x in range(len(list1)):
        sum+=list1[x]
    return sum/len(list1)
#print(average(list1))

#5
#list1=[1,2,3,4,5]
def length(list1):
    length1=len(list1)
    return length1
#print(length(list1))

#6
#list1=[1,0,3,-3,5]
def Miin(list1):
    if len(list1)<1:
        return False
    min=list1[0]
    for x in range(len(list1)):
        if list1[x] <min:
            min=list1[x]
    return min
#print(Miin(list1))

#7
#list1=[]
def Maax(list1):
    if len(list1)==0:
        return False
    max=list1[0]
    for x in range(len(list1)):
        if list1[x] >max:
            max=list1[x]
    return max
#print(Maax(list1))

#8 Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
list1=[1,2,3,4,5]

def ultimate_analysis(list1):
    my_dict={
        'sumTotal': sum_total(list1), 
        'average': average(list1), 
        'minimum': Miin(list1), 
        'maximum': Maax(list1), 
        'length': length(list1)
    }
    return my_dict
print(ultimate_analysis(list1))

list1=[1,2,3,4,5]

#9

def reverse_do(list1):

    #intializing pointers
    left = 0
    right = len(list1)-1

    #condition for termination
    while left<right:

        #swapping
        temp = list1[left]
        list1[left] = list1[right]
        list1[right] = temp

        #updating pointers
        left += 1
        right -= 1

    return list1

print(reverse_do(list1))

list1=[1,2,3,4,5]
def reverse_alt(list1):
    for x in range(len(list1)):
        for y in range(len(list1)-x-1):
            temp = list1[y]
            list1[y] = list1[y+1]
            list1[y+1] = temp
    return list1

print(reverse_alt(list1))