n=int(input())
lst=[]
tuplelst=[]
dict1={}
firstlst=[]
secondlst=[]
for i in range(n):
    ele=int(input())
    lst.append(ele)   
lst1=lst
for i in lst1:
    dict1[i]=lst.count(i)
for i,j in dict1.items():
    tuplelst.append((i,j))
    firstlst.append(i)
    secondlst.append(j)

print(lst)     
print(dict1)
print(tuplelst)
print(firstlst)
print(max(firstlst))
print(secondlst)
print(min(secondlst))

