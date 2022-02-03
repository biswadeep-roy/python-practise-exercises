# creating a tuple using ()
# () is known as parenthesis
t =  (1,2,4,5)
# printing values in tuple

# t1 = () # empty tupple

# t1 = (1)  # wrong way to declare tuple with single element
t1 = (1, )  # tuple with single element
print(t1)

# we can not update values is tuples
# tuples are immutable which means values of tuples can not be changed or updated
# t[0] = 34 throws an error
# print(t[0])

t2 = (1,2,4,6,1,1,2,3,1,2)
print(t2.count(1))
print(t2.index(6))