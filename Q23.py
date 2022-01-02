# Define a Python function "alternating(l)" that returns True if the values in the input list alternately go up and down (in a strict manner).
#
# For instance:
#
# >>> alternating([])
# True
#
# >>> alternating([1,3,2,3,1,5])
# True
#
# >>> alternating([3,2,3,1,5])
# True
#
# >>> alternating([3,2,2,1,5])
# False
#
# >>> alternating([3,2,1,3,5])
# False


def descending(li):
    l=len(li)
    if l==0 or l==1:
        return True
    else:
        for i in range(1,l):
            if li[i]>li[i-1]:
                return False
        return True

def alternating(li):
    l = len(li)
    if l == 0 or l == 1:
        return True
    if li[0] == li[1]:
        return False
    elif li[0] > li[1]:
        for i in range(2, l):
            if i%2 == 0:
                if li[i] <= li[i-1]:
                    return False
            else:
                if li[i] >= li[i-1]:
                    return False
        return True
    elif li[0] < li[1]:
        for i in range(2, l):
            if i%2 == 0:
                if li[i] >= li[i-1]:
                    return False
            else:
                if li[i] <= li[i-1]:
                    return False
        return True

print(alternating([]))
print(alternating([1,3,2,3,1,5]))