# A1 is an array which is list of integers
# B1 is number of times elements in A1 has to shift/rotate
A1 = [1, 2, 3, 4, 5]
B1 = [2, 3]
def solve(A, B):
    C = ' '.join(str(i) for i in A)  # taking the array and converting to string
    D = []
    for k in B:
        A = C.split()
        A = [int(i) for i in A]  # changing the string to int array, doing this because arr A is changing
        # independent of a new variable assigning to A and using new variable
        k = len(A) - k
        rev(A, 0, len(A) - 1)
        rev(A, 0, k-1)
        rev(A, k, len(A) - 1)
        D.append(A)

    return D

def rev(a, i, j):
    """'i' is starting position and 'j' is ending position, reversing based on given indices"""
    while i < j:
        s = a[i]
        a[i] = a[j]
        a[j] = s
        j -= 1
        i += 1
    return a

print(solve(A1, B1))
