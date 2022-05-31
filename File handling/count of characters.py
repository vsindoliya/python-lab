f=open("to the.txt",'r')
str=f.read()
str1=f.readlines()
count=0
count1=0
count2=0
x=str.split(' ')
for i in x:
    count+=1
for i in range(0,len(str)):
    count1+=1
for i in str1:
    count2+=1
print("Count of words")
print(count)
print("Count of characters")
print(count1)
print("Count of lines")
print(count2)
