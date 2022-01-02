# Write a program in python to calculate the sum of the digits of the number 240


# Function to get sum of digits
def CalculateSum(number):
    sumofdigits = 0
    for digits in str(number):
        sumofdigits += int(digits)
    return sumofdigits


number = 2**40
print(CalculateSum(number))
