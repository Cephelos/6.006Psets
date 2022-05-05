global num_even_paths, path_lengths_odd, path_lengths_even, neighbors

path_lengths_odd = {}
path_lengths_even = {}

def num_opt_even_weight_paths(graph, s):
    global path_lengths_odd, path_lengths_even
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




    for n in graph.keys():
        path_lengths[n] = even(graph, s, n)
        neighbors[n] = {}
        path_lengths_odd[n] = {}
        path_lengths_even[n] = {}


    print("paht lengths", path_lengths)


    for n in graph.keys():
        for m in graph[n]:
            neighbors[m][n] = graph[n][m]

            path_lengths_odd[n][m] = 0.1
            path_lengths_even[n][m] = 0.1




    for n in graph.keys():
        num_even_paths[n] = num_even(graph, s, n, neighbors)

    return num_even_paths


def num_even(graph, s, u, neighbors):
    global path_lengths_even, path_lengths_odd
    if s==u:
        return 1
    num_even_paths = 0
    for n in neighbors[u]:
        print('~~~~~~~~~~~debug', path_lengths_odd[s])
        if neighbors[u][n] % 2 == 0 and path_lengths_even[s][n] + neighbors[u][n] == path_lengths_even[s][u]:
            print("nodes", s, u)
            num_even_paths += num_even(graph, s, n, neighbors)

        if neighbors[u][n] % 2 == 1 and path_lengths_odd[s][n] + neighbors[u][n] == path_lengths_even[s][u]:
            print("nodes", s, u)
            num_even_paths += num_odd(graph, s, n, neighbors)
    return num_even_paths



def num_odd(graph, s, u, neighbors):
    global path_lengths_even, path_lengths_odd
    if s==u:
        return 1
    num_odd_paths = 0
    for n in neighbors[u]:

        if neighbors[u][n] % 2 == 1:
            if path_lengths_even[s][n] + neighbors[u][n] == path_lengths_odd[s][u]:
                num_odd_paths += num_even(graph, s, n, neighbors)
        if neighbors[u][n] % 2 == 0:
            if path_lengths_odd[s][n] + neighbors[u][n] == path_lengths_odd[s][u]:
                num_odd_paths += num_odd(graph, s, n, neighbors)

    return num_odd_paths





def even(graph, s, u):
    global path_lengths_even

    if u in graph[s] and graph[s][u] % 2 == 0:
        print('shortcut', graph[s][u])
        return graph[s][u]
    if graph[s] == {}: return 0.1
    paths = set()
    if s in path_lengths_even.keys() and u in path_lengths_even[s].keys():
        return path_lengths_even[s][u]
    for n in graph[s]:
        print("pEven", path_lengths_even)

        if graph[s][n] % 2 == 0:
            x = graph[s][n] + even(graph, n, u)
            print('result', x)
            paths.add(x)

        else:
            x = graph[s][n] + odd(graph, n, u)
            print('result2', x)
            paths.add(x)


    finalpaths = set()

    for p in paths:
        if p % 2 == 0:
            finalpaths.add(p)
    print("even", paths, s, u)
    if finalpaths:
        print("finalE", finalpaths)
        x = min(finalpaths)
        if s not in path_lengths_even.keys():
            path_lengths_even[s] = {}

        path_lengths_even[s][u] = x

        return x
    else:
        print('helpE')
        return 0.1




def odd(graph, s, u):
    global path_lengths_odd

    if u in graph[s] and graph[s][u] % 2 == 1: return graph[s][u]
    if graph[s] == {}: return 0.1
    paths = set()
    if s in path_lengths_odd.keys() and u in path_lengths_odd[s].keys():
        return path_lengths_odd[s][u]

    for n in graph[s]:
        print("pOdd", path_lengths_odd)
        if graph[s][n] % 2 == 0:
            paths.add(graph[s][n] + even(graph, n, u))
        else:
            paths.add(graph[s][n] + odd(graph, n, u))


    finalpaths = set()
    for p in paths:
        if p % 2 == 1:
            finalpaths.add(p)
    print("odd", paths, s, u)
    if finalpaths:
        print("finalO", finalpaths)
        x = min(finalpaths)
        if s not in path_lengths_odd.keys():
            path_lengths_odd[s] = {}

        path_lengths_odd[s][u] = x

        return x
    else:
        print('helpO')
        return 0.1




if __name__ == "__main__":
     print(num_opt_even_weight_paths({"a":{"b":3, "c":5}, "b":{"c":3}, "c":{}}, "a"))
    # should return {"a":1, "b":0, "c":1}

    # print(num_opt_even_weight_paths({"a":{"b":3, "c":5, "d":2}, "b":{"c":3}, "d":{"c":4}, "c":{}}, "a"))
    # should return {"a":1, "b":0, "c":2}

    # print(even({"a":{"b":3, "c":5}, "b":{"c":3}, "c":{}}, "a", "c"))

