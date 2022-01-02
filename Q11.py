


# Write a program in python to find all missing numbers in the list containing a series of 1 to 100.

number_Series = list(range(1, 100, 2))
print("Series containg random numbers from 1 to 100 are :", number_Series)

def find_missing(number_Series):
    return [x for x in range(number_Series[0], number_Series[-1]+1)
                               if x not in number_Series]


print("Missing Numbers are :", find_missing(number_Series))
