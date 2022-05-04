PRIME = 2 ** 31 - 1


def search_lyrics(L, Q):
    """
    Input: L | an ASCII string 
    Input: Q | an ASCII string where |Q| < |L|
    
    Return `True` if Q appears inside the lyrics L and `False` otherwise.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    if not Q:
        return False

    x = len(L)
    y = len(Q)

    f = 128 ** y % PRIME

    hash_L = 0
    for i in range(y):
        hash_L += (ord(L[i])*(128**(y-i-1)))

    hash_L %= PRIME

    hash_Q = 0
    for i in range(y):
        hash_Q += (ord(Q[i])*(128**(y-i-1)))

    hash_Q %= PRIME
    if hash_L == hash_Q:
        return True


    for i in range(0, x-y):
        hash_L = (hash_L * 128 - ord(L[i]) * f + ord(L[y+i])) % PRIME


        if hash_L == hash_Q:
            if Q == L[i+1:i+y+1]:
                return True

    return False

