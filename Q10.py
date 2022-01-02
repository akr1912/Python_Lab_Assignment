# Write a program in python using regular expression to retrieve all words having at least 4 character length.
# The text file name containing words is given by user.

import re
text = input("Enter Text : ")
print(re.findall(r"\b\w{4,}\b", text))
