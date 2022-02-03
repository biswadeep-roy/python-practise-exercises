letter ='''Dear <|NAME|>
Greetings from VITian student. I am verry happy to tell you about your selection in our club
You are selecteed
Have a great day aheas!
Thanks and regards.
Bill
Date: <|DATE|>
'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")
letter=letter.replace("<|NAME|>", name)
letter=letter.replace("<|DATE|>", date)
print(letter)