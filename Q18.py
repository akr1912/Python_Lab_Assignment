# Write a function intreverse(n) that takes as input a positive integer n and returns the integer obtained
# by reversing the digits in n.
#
# Here are some examples of how your function should work.
#
# >>> intreverse(783)
# 387
# >>> intreverse(242789)
# 987242
# >>> intreverse(3)
# 3

n = int(input("Enter a Number : "))
def intreverse(n):
    num1 = 0
    rev = 0
    while ( n > 0 ):
        num1 = n % 10
        n = n // 10
        rev = (rev * 10) + num1
    return(rev)
res = intreverse(n)
print("Reverse is: ", res)
