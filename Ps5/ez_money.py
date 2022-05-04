import math


def ez_money(D):
    """Determine if there is a sequence of commodities to exchange
    to get more of some commodity than you started with.

    Args:
        D: A list of deals, where each is of the form (A, x, B, y),
           meaning that someone will give you y of B for x of A.
           'A' and 'B' are strings, and 'x' and 'y' are integers.

    Returns:
        True if such an opportunity exists, False otherwise.
    """

    V = set()
    E = set()
    for d in D:
        V.add(d[0])
        V.add(d[2])

    for d in D:
        E.add((d[0], d[2], -math.log2((d[3] / d[1]))))

    V = list(V)
    for i in V:
        result = BellmanFord(V, E, i)
        if type(result) == bool:
            return True
    return False




def BellmanFord(V, E, u):
    d = {}
    parent = {}
    visited = set()
    for v in V:
        d[v] = math.inf
        parent[v] = None
    d[u] = 0

    for i in range(len(V) - 1):
        for (v1, v2, w) in E:
            if d[v2] > d[v1] + w:
                d[v2] = d[v1] + w
                parent[v2] = v1
    # check for negative cycles
    for (v1, v2, w) in E:
        if d[v2] > d[v1] + w:

            return False

    return visited
