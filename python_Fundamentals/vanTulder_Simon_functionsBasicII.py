#1
num = 7
def countDown(num):
    list1=[]
    for x in range(num, -1, -1):
        list1.append(x)
    return list1
print(countDown(num))

#2
num1 = 8
num2 = 3
def printReturn(x,y):
    print(x)
    return y
printReturn(num1, num2)

#3
list1 = [1,2,3,4,5]
def firstLength(list1):
    sum=list1[0]+len(list1)
    print(sum)

firstLength(list1)

#4
list1 = [1,2,3,4,5]
def biggySecond(list1):
    list2=[]
    if len(list1)<2:
        return False
    for x in list1:
        if x> list1[1]:
            list2.append(x)
    print(list1[1])
    return list2

print(biggySecond(list1))

#5
num1=4
num2=7

def lengthValue(num1, num2):
    list1 = []
    for x in range(0, num1):
        list1.append(num2)
    return list1
print(lengthValue(num1, num2))