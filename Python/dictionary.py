myDict = {
    "Fast": "In a Quick Manner",
    "biebs": "A pagal",
    "Marks": [1, 2, 5],
    "anotherdict": {'harry': 'Player'}
}

myDict['Fast'][5]='A'
print(myDict['Fast'][5])
# print(myDict['Harry'])
myDict['Marks'][1]=10
print(myDict)
print(myDict['Marks'][0])
print(myDict['anotherdict']['harry'])

for key in myDict:
    print(myDict[key])

