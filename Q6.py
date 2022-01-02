

# Write a program in python to find the sum of three numbers, entered by user, with the condition that if one of the
# value is the same as another of the values, it does not count towards the sum.
num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))
if(num1 == num2 or num1 == num3):
    sum = num2 + num3
    print(sum)
elif(num2 == num1 or num2 == num3):
    sum = num1 + num3
    print(sum)
elif(num3 == num1 or num3 == num2):
    sum = num1 + num2
    print(sum)
elif(num1 != num2 or num1 != num3 or num2 != num3):
    sum = num1 + num2 + num3
    print(sum)