a = [1, 7, 6, 4, 8, 9, 5]
for i in range (len (a)) :
    for j in range (i+1,len (a)): 
        if a [i]>a[j]: 
            a[i], a[j] = a[j], a[i]
print (a)