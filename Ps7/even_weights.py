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
    path_lengths2 = {}
    neighbors = {}




    for n in graph.keys():
        neighbors[n] = {}


    for n in graph.keys():
        for m in graph[n]:
            neighbors[m][n] = graph[n][m]


    for n in graph.keys():
        path_lengths2[n] = odd(graph, s, n, neighbors)
        path_lengths[n] = even(graph, s, n, neighbors)

    #print("*", path_lengths2)
    #print("&", neighbors)
    #print("^", path_lengths_even, path_lengths_odd)

    path_lengths_even[s] = 0
    path_lengths_odd[s] = 99999




    for n in graph.keys():
        num_even_paths[n] = num_even(graph, s, n, neighbors)

    return num_even_paths


def num_even(graph, s, u, neighbors):
    global path_lengths_even, path_lengths_odd
    if s==u:
        return 1
    num_even_paths = 0
    for n in neighbors[u]:

        if neighbors[u][n] % 2 == 0 and path_lengths_even[n] + neighbors[u][n] == path_lengths_even[u]:

            num_even_paths += num_even(graph, s, n, neighbors)

        if neighbors[u][n] % 2 == 1 and path_lengths_odd[n] + neighbors[u][n] == path_lengths_even[u]:

            num_even_paths += num_odd(graph, s, n, neighbors)
    return num_even_paths



def num_odd(graph, s, u, neighbors):
    global path_lengths_even, path_lengths_odd
    if s==u:
        return 1
    num_odd_paths = 0
    for n in neighbors[u]:

        if neighbors[u][n] % 2 == 1 and path_lengths_even[n] + neighbors[u][n] == path_lengths_odd[u]:
                num_odd_paths += num_even(graph, s, n, neighbors)
        if neighbors[u][n] % 2 == 0 and path_lengths_odd[n] + neighbors[u][n] == path_lengths_odd[u]:
                num_odd_paths += num_odd(graph, s, n, neighbors)

    return num_odd_paths





def even(graph, s, u, neighbors):
    global path_lengths_even

    if u in graph[s] and graph[s][u] % 2 == 0:
        x = graph[s][u]
        path_lengths_even[u] = x
        return x

    paths = set()
    if u in path_lengths_even.keys():
        return path_lengths_even[u]


    for n in neighbors[u]:

        if neighbors[u][n] % 2 == 0:
            paths.add(even(graph, s, n, neighbors) + neighbors[u][n])


        if neighbors[u][n] % 2 == 1:

            paths.add(odd(graph, s, n, neighbors) + neighbors[u][n])





    if paths:
        x = min(paths)
        path_lengths_even[u] = x
        return x
    else:

        return 0


def odd(graph, s, u, neighbors):
    global path_lengths_odd

    if u in graph[s] and graph[s][u] % 2 == 1:
        x = graph[s][u]
        path_lengths_odd[u] = x
        return x
    paths = set()
    if u in path_lengths_odd.keys():
        return path_lengths_odd[u]

    for n in neighbors[u]:

        if neighbors[u][n] % 2 == 1:
            paths.add(even(graph, s, n, neighbors) + neighbors[u][n])

        if neighbors[u][n] % 2 == 0:
            paths.add(odd(graph, s, n, neighbors) + neighbors[u][n])



    if paths:
        x = min(paths)
        path_lengths_odd[u] = x
        return x
    else:

        return float("inf")




if __name__ == "__main__":
    # print(num_opt_even_weight_paths({"a":{"b":3, "c":5}, "b":{"c":3}, "c":{}}, "a"))
    # should return {"a":1, "b":0, "c":1}

    print(num_opt_even_weight_paths({"a":{"b":3, "c":5, "d":2}, "b":{"c":3}, "d":{"c":4}, "c":{}}, "a"))
    # should return {"a":1, "b":0, "c":2}

    # print(even({"a":{"b":3, "c":5}, "b":{"c":3}, "c":{}}, "a", "c"))

