#1
for x in range(1,151,1):
    print(x)

#2
for x in range(5,1001,5):
    print(x)
#3
for x in range(1,101):
    if(x%10==0):
        print("Coding Dojo")
    elif(x%5==0):
        print("Coding")
    else:
        print(x)
#4
sum=0
for x in range(1,500000,2):
    sum+=x
print(sum)
#5

for x in range(2018,0,-4):
    print(x)

#6
lowNum=2
highNum=9
mult=3
for x in range(lowNum,highNum+1):
    if(x%mult==0):
        print(x)
    else:
        x+=1

# alt soln

for x in range(mult,highNum+1,mult):
    if(x>lowNum):
        print(x)

