# Define a Python function "descending(l)" that returns True if each element in its input list is at most as big as the one before it
#
# For instance:
#
# >>> descending([])
# True
#
# >>> descending([4,4,3])
# True
#
# >>> descending([19,17,18,7])
# False

def descending(l):
    answer = True
    if l == []:
        return True
    for element in range(0, len(l) - 1):
        if l[element] < l[element + 1]:
            answer = False
            break
    return answer
print(descending([4,4,3]))
print(descending([19,17,18,7]))
