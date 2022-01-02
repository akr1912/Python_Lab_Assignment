

# Write a program in python that makes square of unique elements only for the list entered by user.

list = []
unique = []
unique_square = []
number = int(input("Enter number of elements : "))
for element in range(0, number):
    value = int(input())
    list.append(value)
print(list)
for i in list:
    if i not in unique:
        unique.append(i)
print(unique)

for j in unique:
    if j in unique:
        square = j**2
        unique_square.append(square)
print("Square of unique elements are : ", unique_square)
