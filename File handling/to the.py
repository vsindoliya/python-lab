count=0
count1=0
f=open("to the.txt",'r')
str=f.read()
f.close()
x=str.split(' ')
for i in x:
    if (i.lower()=='to'): 
        count+=1 
    elif (i.lower()=='the'):
        count1+=1

print("Count of To:")
print(count)
print("Count of The:")
print(count1)
