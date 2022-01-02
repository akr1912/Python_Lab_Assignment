# Write a program in python to check the occurrences of each element of a string using dictionary.
# A space separated string of elements will be provided by user.

dictionary = {}
string = input("Enter the string\n")
for element in string:
    if element in dictionary:
        dictionary[element] += 1
    else:
        dictionary.update({element: 1})
print("The Occurences are : ", dictionary)