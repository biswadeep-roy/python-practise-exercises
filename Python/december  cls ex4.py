a = [3, 8, 5, 1, 8, 9, 4, 9, 6, 4, 3, 7] 
b = list (set (a))
for i in range (len(b)): 
    for j in range (i+1,len (b)): 
        if b[i]>b[j]:
            b[i] , b[j] = b[j], b[i]
print (b)