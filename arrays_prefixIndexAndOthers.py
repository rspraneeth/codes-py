A1 = [5, -2, 3, 1, 2]

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
    """returning the prefix sum(pf) array/list, pf is sum of array elements up to the particular index.
    where prefix[i] denotes sum of elements from index [0,i] """
    pf_sum = [0] * len(A)
    pf_sum[0] = A[0]
    for i in range(1, len(A)):
        pf_sum[i] = pf_sum[i-1] + A[i]
    return pf_sum

def sf(A):
    """returning the suffix sum(sf) array/list, where sf[i] denotes sum of elements from index [i,N-1] """
    sf_sum = [0] * len(A)
    sf_sum[len(A)-1] = A[len(A)-1]  # last element of sf_sum equals last element of array
    for i in range(len(A)-2, -1, -1):
        sf_sum[i] = sf_sum[i+1] + A[i]
    return sf_sum

def pfeven_pfodd(A):
    """combining pfodd(returns an array of size len(A), with sum of odd indices values up to the index)
    and pfeven(returns an array of size len(A), with sum of even indices values up to the index)"""
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

def pickBothSides(A):
    """You are given an integer array A of size N. You have to pick B elements in total.
    Some (possibly 0) elements from left end of array A and some (possibly 0) from the
    right end of array A to get the maximum sum. Find and return this maximum possible sum."""
    B = 3
    n = len(A)
    pref = pf(A)
    suff = sf(A)
    ans = max(suff[n - B], pref[B - 1])
    for i in range(B - 1):
        val = pref[i] + suff[n - B + i + 1]
        ans = max(val, ans)
    return ans

def rangeSum(A):
    """You are given an integer array A of length N. You are also given a 2D integer array B
    with dimensions M x 2, where each row denotes a [L, R] query. For each query, you have to
    find the sum of all elements from L to R indices in A
    Input: A = [1, 2, 3, 4, 5] B = [[1, 4], [2, 3]], Output: [10, 5]"""
    B = [[1, 4], [2, 3]]
    n = len(A)
    prf = [0] * n
    prf[0] = A[0]
    for i in range(1, n):
        prf[i] = A[i] + prf[i - 1]
    for p in range(len(B)):
        ls = B[p]
        i, j = ls[0] - 1, ls[1] - 1
        if i == 0:
            B[p] = prf[j]
        else:
            B[p] = prf[j] - prf[i - 1]
    return B
