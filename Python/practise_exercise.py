string1="Hi py"
lst=[]
lst = string1.split()
print(lst)
count=0
for i in string1:
    count+=1
print(count)
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=l1+l2
print(l3)
lst1=[1,2,3,4]
n=int(input("Enter the n :"))
print(lst1*n)
list4=['x','y']
print(list4*2)
list5=[1,2,3,4,5]
list5.remove(list5[4])
print(list5)
list6=[1,2,6,7,2,4,1,8,10,4,3,7,10,11,40]
sorted_list6=list6.sort()
print(list6)
list7=[1,2,6,7,2,14,1,8,10,4,3,7,19,11,40]
list7.pop(4)
list7.pop()
print(list7)
