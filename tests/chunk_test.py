import unittest
from pyutil.chunk import chunk

class Chunk_Tests(unittest.TestCase):
    def test_chunk(self):
        lst = [1, 2, 3, 4, 5]
        actual = list(chunk(lst, 2))
        expected = [[1, 2], [3, 4], [5]]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

