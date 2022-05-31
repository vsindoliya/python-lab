count = 0
f=open("filname.txt",'r')
str=f.read()
print(str)
for i in str:
    if(i.isupper()==True):
        count+=1
print(count)
f.close()
