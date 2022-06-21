A1 = [2, 1, 6, 4]

def eq(A):
    """The equilibrium index of an array is an index such that the sum of elements at
    lower indexes is equal to the sum of elements at higher indexes."""
    # If there is no equilibrium index then return -1.
    # If there are more than one equilibrium indexes then return the minimum index.
    prf = pf(A)
    # prf_ind = []  # to save all the eq indices
    for i in range(len(prf)):
        if i == 0:
            left = 0
        else:
            left = prf[i-1]
        right = prf[len(prf)-1] - prf[i]
        if left == right:
            return i
            # prf_ind.append(i)  # returning the list of all equilibrium indices
            # return prf_ind

    return -1

def pf(A):
    """returning the prefix index(pf) array/list, pf is sum of array elements upto the particulr index"""
    pf = [0] * len(A)
    pf[0] = A[0]
    for i in range(1, len(A)):
        pf[i] = pf[i - 1] + A[i]
    return pf

def pfeven_pfodd(A):
    """combining pfodd(returns an array of size len(A), with sum of odd indices values upto the index)
    and pfeven(returns an array of size len(A), with sum of even indices values upto the index)"""
    pfeven = [0] * len(A)
    pfeven[0] = A[0]
    pfodd = [0] * len(A)
    pfodd[0] = 0
    for i in range(1, len(A)):
        if i % 2 == 1:
            pfeven[i] = pfeven[i-1]
            pfodd[i] = A[i] + pfodd[i - 1]
        else:
            pfeven[i] = A[i] + pfeven[i - 1]
            pfodd[i] = pfodd[i - 1]
    return pfeven, pfodd

def sumevenEqualsSumodd(A):
    """return the count of array indices such that removing an element from these
    indices makes the sum of even-indexed and odd-indexed array elements equal."""
    prfeven, prfodd = pfeven_pfodd(A)
    count = 0
    c_ind = []
    for i in range(len(A)):
        if i == 0:
            s_even = prfodd[len(A)-1]
            s_odd = prfeven[len(A)-1] - prfeven[0]
        else:
            s_even = prfeven[i-1] + prfodd[len(A)-1] - prfodd[i]
            s_odd = prfodd[i-1] + prfeven[len(A)-1] - prfeven[i]
        if s_even == s_odd:
            count += 1
            c_ind.append(i)
    return count, c_ind

print(sumevenEqualsSumodd(A1))
