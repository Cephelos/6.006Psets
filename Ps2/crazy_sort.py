
import math

def crazy_sort(A, i, j):
    '''
    Sorts in place the sub-array A[i:j].
    '''
    n = j-i
    if n <= 1:
        return
    if n == 2:
        A[i], A[j - 1] = min(A[i:j]), max(A[i:j])
        return
    m = math.ceil(2.0 * n / 3.0)
    print('---')
    print(i)
    print(j)
    print('---')
    crazy_sort(A, i, i + m) # sort A[i : i+m]
    crazy_sort(A, j - m, j) # sort A[j-m : j]
    crazy_sort(A, i, i + m) # sort A[i : i+m]

p = [5,4,3,2,1]
crazy_sort(p, 0, 5)
print(p)