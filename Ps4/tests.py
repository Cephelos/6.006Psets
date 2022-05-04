import unittest
from node_way_home import find_meeting_point

class TestCases(unittest.TestCase):
    def test_01(self):
        adj = [[1,2],[2],[]]
        expected = [2]
        self.assertTrue(find_meeting_point(adj) in expected)

    def test_02(self):
        adj = [[1,2],[2],[1]]
        expected = [2, 1]
        self.assertTrue(find_meeting_point(adj) in expected)

    def test_03(self):
        adj = [[1,2],[2],[1], []]
        expected = [None]
        self.assertTrue(find_meeting_point(adj) in expected)

    def test_04(self):
        adj = [[]]
        expected = [0]
        self.assertTrue(find_meeting_point(adj) in expected)

    def test_05(self):
        adj = [[1,2], [2,0], [0,1]]
        expected = [0,1,2]
        self.assertTrue(find_meeting_point(adj) in expected)

    def test_06(self):
        adj = [[1,2,3,4,5,6], [0,2,3,4,5,6], [0,1,3,4,5,6], [0,1,2,4,5,6], [0,1,2,3,5,6], [0,1,2,3,4,6], [0,1,2,3,4,5]]
        expected = [0,1,2,3,4,5,6]
        self.assertTrue(find_meeting_point(adj) in expected)

    def test_07(self):
        adj = [[1,2,3,4,5,6], [0,2,3,4,5,6], [0,1,3,4,5,6], [0,1,2,4,5,6], [5,6], [4,6], [4,5]]
        expected = [4,5,6]
        self.assertTrue(find_meeting_point(adj) in expected)

    def test_08(self):
        adj = [[1,2,3,4,5,6], [2,3], [1,3], [1,2], [5,6], [4,6], [4,5]]
        expected = [None]
        self.assertTrue(find_meeting_point(adj) in expected)

    def test_09(self):
        adj = [[1], [2], [3], [4], [5], [6], []]
        expected = [6]
        self.assertTrue(find_meeting_point(adj) in expected)


if __name__ == "__main__":
    res = unittest.main(verbosity=3, exit=False)