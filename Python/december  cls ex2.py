array = [7, 2, 4, 9, 1]; 
temp = 0;
print ("Elements of original array: "); 
for i in range (0, len(array)): 
    print (array[i]), 
for i in range (0, len (array)): 
    for j in range (i+1, len(array)): 
        if(array[i] < array[j]):
            temp = array[i]; 
            array[i] = array[j];
            array[j] = temp;
print ();
print ("Elements of array sorted in descending order: "); 
for i in range (0, len(array)): 
    print (array[i]),