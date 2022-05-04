import unittest
from flix_chill import FlixChillManager

class TestCases(unittest.TestCase):
    def test_01(self):
        f = FlixChillManager()
        f.insert(1, 100, 50)
        f.insert(2, 101, 40)
        f.insert(3, 102, 1)
        self.assertTrue(f.highest(10) == 1)

    def test_02(self):
        f = FlixChillManager()
        f.insert(1, 100, 50)
        f.insert(2, 101, 40)
        f.insert(3, 102, 1)
        self.assertTrue(f.highest(101) == 2)


    def test_03(self):
        f = FlixChillManager()
        f.insert(1, 100, 50)
        f.insert(2, 101, 40)
        f.insert(3, 102, 1)
        print(f.highest(102))
        self.assertTrue(f.highest(102) == 3)

    def test_04(self):
        f = FlixChillManager()
        f.insert(1000, 228, 99)
        f.insert(1001, 229, 49)
        f.insert(1002, 130, 34)
        self.assertTrue(f.highest(200) == 1000)

    def test_05(self):
        f = FlixChillManager()
        f.insert(1000, 228, 99)
        f.insert(1001, 229, 49)
        f.insert(1002, 130, 340)
        self.assertTrue(f.highest(100) == 1002)

if __name__ == "__main__":
    res = unittest.main(verbosity=3, exit=False)