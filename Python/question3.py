list1=[100, 50, 200, 150]
def sort(list1):
    for j in range (len(list1)-1):
        for i in range (len(list1)-1):
            if list1[i]>list1[i+1]:
                 list1[i],list1[i+1]=list1[i+1],list1[i]
    print(list1)
sort(list1)
