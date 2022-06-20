# count no of elements having at least one element greater than itself
# finding the count of max number and subtracting from length
# a = [4, 5, 5, 5, 5]
# mx = a[0]
# c = 0
# for i in range(1, len(a)):
#     if mx < a[i]:
#         mx = a[i]
#         c = 1
#     elif mx == a[i]:
#         c += 1
# print(len(a)-c)

# reverse an array from a position to another position
def rev(a, i, j):
    """'i' is starting position and 'j' is ending position"""
    while i < j:
        s = a[i]
        a[i] = a[j]
        a[j] = s
        j -= 1
        i += 1
    return a

# rotate an array elements by k times from left to right
ar = [1, 2, 3, 4, 5, 6, 7, 8]
k = 9
k = k % len(ar)
# reverse the array
ar = rev(ar, 0, len(ar)-1)
# reverse the first k elements
ar = rev(ar, 0, k-1)
# reverse the elements after k
ar = rev(ar, k, len(ar)-1)

print(ar)
