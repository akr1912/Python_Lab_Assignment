# Write a function sumprimes(l) that takes as input a list of integers and returns the sum of all the prime numbers in l.
#
# Here are some examples to show how your function should work.
#
# >>> sumprimes([3,3,1,13])
# 19
# >>> sumprimes([2,4,6,9,11])
# 13
# >>> sumprimes([-3,1,6])
# 0

def sumprimes(I):
 # Function for check that the number is prime
  def check_prime(number):
 # Negative numbers and 1 are not simple
   if number < 2:
    return False
 # Check all dividers before sqrt(number)
   for i in range(2, int(number ** 0.5) + 1):
 # If the number has divisor it is not prime
    if not number % i:
     return False
   return True
 # Sum primes
  total = 0
 # Check all number in the list
  for i in I:
 # If number is prime add it to result
   if check_prime(i):
    total += i
  return total

print(sumprimes([3,3,1,13]))
print(sumprimes([2,4,6,9,11]))
print(sumprimes([-3,1,6]))
