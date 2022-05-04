def dfs(Adj, s, parent = None, order = None):
    if parent is None:
        parent = [None for v in Adj]
        order = []
        parent[s] = s
    for v in Adj[s]:
        if parent[v] is None:
            parent[v] = s
            dfs(Adj, v, parent, order)
    order.append(s)
    return parent, order

def full_dfs(Adj):
    parent = [None for v in Adj]
    order = []
    for v in range(len(Adj)):
        if parent[v] is None:
            parent[v] = v
            dfs(Adj, v, parent, order)
    return parent, order

def find_meeting_point(Adj):
    '''
    inputs:
        Adj - an adjacency list such as [[1,2], [2], []]
    return a meeting point or None if no meeting points exist
    '''

    Adj = reverse_edges(Adj)
    meeting_point = full_dfs(Adj)[1][-1]

    if len(dfs(Adj, meeting_point)[1]) == len(Adj):
        return meeting_point
    return None

def reverse_edges(Adj):
    r_list = [[] for l in Adj]
    for index, l in enumerate(Adj):
        for v in l:
            r_list[v].append(index)

    return r_list