import unittest
from even_weights import num_opt_even_weight_paths

tests = [
    (
        {"a":{"b":3, "c":5}, "b":{"c":3}, "c":{}}, 
        "a",
        {'a': 1, 'b': 0, 'c': 1}
    ),
    (
        {"a":{"b":3, "c":5, "d":2}, "b":{"c":3}, "d":{"c":4}, "c":{}}, 
        "a",
        {'a': 1, 'b': 0, 'd': 1, 'c': 2}
    ),
    (
        {"a":{"b":3, "c":5, "d":2}, "b":{"c":3}, "d":{"c":4, "e":6}, "c":{"e":2}, "e":{}}, 
        "a",
        {'a': 1, 'b': 0, 'd': 1, 'c': 2, 'e':3}
    ),
    (
        {"a":{"b":3, "c":5, "d":2, "e":8}, "b":{"c":3, "e":5}, "d":{"c":4, "e":6}, "c":{"e":2}, "e":{}}, 
        "a",
        {'a': 1, 'b': 0, 'd': 1, 'c': 2, 'e':5}
    ),
    (
        {"a":{"b":3, "c":5, "d":2, "e":1}, "b":{"c":3, "e":5}, "d":{"c":4, "e":6}, "c":{"e":2}, "e":{}}, 
        "a",
        {'a': 1, 'b': 0, 'd': 1, 'c': 2, 'e':4}
    ),
    (
        {"a":{"b":1, "c":1, "d":1, "e":1}, "b":{"c":1, "d":1, "e":1}, "c": {"d":1, "e":1}, "d":{"e":1}, "e":{}},
        "a",
        {'a': 1, 'b': 0, 'c': 1, 'd': 2, 'e':3}
    ),
    (
        {"a":{"b":1, "c":1, "d":1}, "b":{"c":1, "d":1, "e":2}, "c": {"d":1, "e":2}, "d":{"e":2}, "e":{}},
        "a",
        {'a': 1, 'b': 0, 'c': 1, 'd': 2, 'e':3}
    ),
]

# Test 7 - large test, should run in about a second
N = 1000
graph = {u:{} for u in range(N)}
for u in graph:
    for v in range(u+1, N):
        graph[u][v] = 1
solution = {i:i-1 for i in range(1,N)}
solution[0] = 1
tests.append((graph, 0, solution))

# Test 8 - large test, should run in about a second
N = 1000
graph = {u:{} for u in range(N)}
for u in graph:
    for v in range(u+1, N):
        graph[u][v] = v-u
solution = {0:1}
for i in range(1, N):
    solution[i] = 0
    if i % 2 == 0:
        solution[i] = 2**(i-1)
tests.append((graph, 0, solution))


class TestCases(unittest.TestCase):
    def test_00(self):
        graph, start, solution = tests[0]
        self.assertEqual(num_opt_even_weight_paths(graph, start), solution)

    def test_01(self):
        graph, start, solution = tests[1]
        self.assertEqual(num_opt_even_weight_paths(graph, start), solution)

    def test_02(self):
        graph, start, solution = tests[2]
        self.assertEqual(num_opt_even_weight_paths(graph, start), solution)

    def test_03(self):
        graph, start, solution = tests[3]
        self.assertEqual(num_opt_even_weight_paths(graph, start), solution)

    def test_04(self):
        graph, start, solution = tests[4]
        self.assertEqual(num_opt_even_weight_paths(graph, start), solution)

    def test_05(self):
        graph, start, solution = tests[5]
        self.assertEqual(num_opt_even_weight_paths(graph, start), solution)

    def test_06(self):
        graph, start, solution = tests[6]
        self.assertEqual(num_opt_even_weight_paths(graph, start), solution)

    def test_07(self):
        graph, start, solution = tests[7]
        self.assertEqual(num_opt_even_weight_paths(graph, start), solution)

    def test_08(self):
        graph, start, solution = tests[8]
        self.assertEqual(num_opt_even_weight_paths(graph, start), solution)

if __name__ == "__main__":
    res = unittest.main(verbosity=3, exit=False)
