def num_opt_even_weight_paths(graph, s):
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
    path_lengths = {}


    for n in graph.keys():
        path_lengths[n] = even(graph, s, n)

    for n in graph.keys():
        if True:
            if n in num_even_paths.keys():
                num_even_paths[n] += 1
            else:
                num_even_paths[n] = 1

    num_even_paths[s] = 1

    return num_even_paths





def even(graph, s, u):
    if u in graph[s] and graph[s][u] % 2 == 0: return graph[s][u]
    if graph[s] == {}: return 0.1
    paths = set()
    for n in graph[s]:
        if graph[s][n] % 2 == 0:
            paths.add(graph[s][n] + even(graph, n, u))
        else:
            paths.add(graph[s][n] + odd(graph, n, u))

    finalpaths = set()
    for p in paths:
        if p % 2 == 0:
            finalpaths.add(p)

    if finalpaths:
        return min(finalpaths)
    else:
        return 0




def odd(graph, s, u):
    if u in graph[s] and graph[s][u] % 2 == 1: return graph[s][u]
    if graph[s] == {}: return 0.1
    paths = set()
    for n in graph[s]:
        if graph[s][n] % 2 == 0:
            paths.add(graph[s][n] + even(graph, n, u))
        else:
            paths.add(graph[s][n] + odd(graph, n, u))
    finalpaths = set()
    for p in paths:
        if p % 2 == 1:
            finalpaths.add(p)

    if finalpaths:
        return min(finalpaths)
    else: return 0




if __name__ == "__main__":
    print(num_opt_even_weight_paths({"a":{"b":3, "c":5}, "b":{"c":3}, "c":{}}, "a"))
    # should return {"a":1, "b":0, "c":1}

    # num_opt_even_weight_paths({"a":{"b":3, "c":5, "d":2}, "b":{"c":3}, "d":{"c":4}, "c":{}}, "a")
    # should return {"a":1, "b":0, "c":2}

    # print(even({"a":{"b":3, "c":5, "d":2}, "b":{"c":3}, "d":{"c":4}, "c":{}}, "a", "d"))

