# Write a program in python using regular expression to find the sequence of
# one uppercase letter followed by lower case letter

import re
def sequence(string):
        expression = '[A-Z]+[a-z]+$'
        if re.search(expression, string):
                return 'Sequence Found'
        else:
                return('Sequence Not Found')
print(sequence(input("Enter a string")))

