f=open("update address.txt",'r')
str=f.read()
lst=str.split()
print(lst)
m=len(lst[0])
for i in lst:
    print(i)
    a=len(i)
    if(a>m):
        m=i
        #print(lst)
print(m)
