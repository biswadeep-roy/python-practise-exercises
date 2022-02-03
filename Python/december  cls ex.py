numlist = [] 
number = int(input("please enter the total no of list elements: "))
for i in range (1, number+1):
    value = int(input("please enter the value of %d element: " %i))
    numlist.append (value)

i = 0
while (i<number): 
    j=i+1
    while (j<number):
        if (numlist[i]>numlist[j]):
            temp = numlist[i]
            numlist[i] = numlist [j]
            numlist[j] = temp
        j = j + 1
    i = i + 1

print("element after sorting list in ascending order is : ", numlist)