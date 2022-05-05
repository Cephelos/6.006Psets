global num_even_paths, path_num_odd, path_num_even, neighbors
def num_opt_even_weight_paths(graph, s):
    global path_num_odd, path_num_even
    '''
    The num_opt_even_weight_paths function should return a dictionary mapping node v to the number of optimal
    paths of even weight from s to v.

    graph - an adjacency list of a DAG in the form {u: {v:w(u,v)} mapping nodes to a dictionary 
            where the keys are their adjacencies and the values are the edge weights
            graph[u][v] would be equal to the weight of the edge u to v.
            you may assume that graph.keys() represents all nodes present
    s - start node

    return: a dictionary mapping node v to the number of optimal paths of even weight from s to v. 
            optimal[s] should be 1.
    '''

    num_even_paths = {}
    num_odd_paths = {}
    path_lengths = {}
    neighbors = {}
    path_num_odd = {}
    path_num_even = {}


    for n in graph.keys():
        path_lengths[n] = even(graph, s, n)
        neighbors[n] = {}

    for n in graph.keys():
        for m in graph[n]:
            neighbors[m][n] = graph[n][m]

    for n in graph.keys():
        num_even_paths[n] = num_even(graph, s, n, neighbors)

    return num_even_paths


def num_even(graph, s, u, neighbors):
    if s==u:
        return 1
    num_even_paths = 0
    for n in neighbors[u]:

        if neighbors[u][n] % 2 == 0 and even(graph, s, n) + neighbors[u][n] == even(graph, s, u):

            num_even_paths += num_even(graph, s, n, neighbors)
        if neighbors[u][n] % 2 == 1 and odd(graph, s, n) + neighbors[u][n] == even(graph, s, u):

            num_even_paths += num_odd(graph, s, n, neighbors)
    return num_even_paths



def num_odd(graph, s, u, neighbors):

    if s==u:
        return 1
    num_odd_paths = 0
    for n in neighbors[u]:

        if neighbors[u][n] % 2 == 1:
            if even(graph, s, n) + neighbors[u][n] == odd(graph, s, u):
                num_odd_paths += num_even(graph, s, n, neighbors)
        if neighbors[u][n] % 2 == 0:
            if odd(graph, s, n) + neighbors[u][n] == odd(graph, s, u):
                num_odd_paths += num_odd(graph, s, n, neighbors)

    return num_odd_paths





def even(graph, s, u):
    global path_num_even
    if u in graph[s] and graph[s][u] % 2 == 0: return graph[s][u]
    if graph[s] == {}: return 0.1
    paths = set()
    for n in graph[s]:
        if s in path_num_even.keys() and n in path_num_even[s].keys():
            paths.add(path_num_even[s][n])
        elif graph[s][n] % 2 == 0:
            paths.add(graph[s][n] + even(graph, n, u))
        else:
            paths.add(graph[s][n] + odd(graph, n, u))

    finalpaths = set()
    for p in paths:
        if p % 2 == 0:
            finalpaths.add(p)

    if finalpaths:
        x = min(finalpaths)
        if s not in path_num_even.keys():
            path_num_even[s] = {}
        path_num_even[s][n] = x
        return x
    else:
        return 0




def odd(graph, s, u):
    global path_num_odd

    if u in graph[s] and graph[s][u] % 2 == 1: return graph[s][u]
    if graph[s] == {}: return 0.1
    paths = set()
    for n in graph[s]:
        if s in path_num_odd.keys() and n in path_num_odd[s].keys():
            paths.add(path_num_odd[s][n])

        elif graph[s][n] % 2 == 0:
            paths.add(graph[s][n] + even(graph, n, u))
        else:
            paths.add(graph[s][n] + odd(graph, n, u))
    finalpaths = set()
    for p in paths:
        if p % 2 == 1:
            finalpaths.add(p)

    if finalpaths:
        x = min(finalpaths)
        if s not in path_num_odd.keys():
            path_num_odd[s] = {}
        path_num_odd[s][n] = x
        return x
    else: return 0




if __name__ == "__main__":
    print(num_opt_even_weight_paths({"a":{"b":3, "c":5}, "b":{"c":3}, "c":{}}, "a"))
    # should return {"a":1, "b":0, "c":1}

    # num_opt_even_weight_paths({"a":{"b":3, "c":5, "d":2}, "b":{"c":3}, "d":{"c":4}, "c":{}}, "a")
    # should return {"a":1, "b":0, "c":2}

    # print(even({"a":{"b":3, "c":5, "d":2}, "b":{"c":3}, "d":{"c":4}, "c":{}}, "a", "d"))

