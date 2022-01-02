
# Write a program in python to find the palindrome in a list where the list of strings is entered by user.

# string = input("Enter the string :")
# if string == string[::-1]:
#     print("Given String is Pallindrome : ", string)
# else:
#     print("Given String is not pallindrome : ", string)
n = int(input("Enter range : "))
list = []
for ele in range(0, n):

    ele = input("Enter the string : ")
    list.append(ele)
print(list)
for i in list:
    if i == i[::-1]:
        print("Pallindrome Found : ", i)
    else:
        print("Given String is not pallindrome : ", i)