import unittest
from random import randint

class TestBinarySearch(unittest.TestCase):

    def binary_search(self, input_array, value):
        start = 0
        end = len(input_array)-1
        while(start<=end):
            m = int((start+end)/2)
            if (value>input_array[m]):
                start = m+1
            elif (value<input_array[m]):
                end = m-1
            else:
                return m
        return -1

    def binary_search2(self, input_array, value):
        """Your code goes here."""
        start = 0
        end = len(input_array)-1
        m = int((start+end)/2)
        while(end-start > 0):
            if (value>input_array[m]):
                start = m
                m = int((start+end)/2)
            elif (value<input_array[m]):
                end = m
                m = int((start+end)/2)
            else:
                return m
        return -1

    def test_search(self):
        s = list(set([randint(0,100) for x in range(0,100)]))
        s.sort()
        print(s)
        for i in range(0,20):
            with self.subTest(i=i):
                r = randint(0,len(s)-1)
                self.assertEqual(self.binary_search2(s,s[r]), r)

if __name__ == '__main__':
    unittest.main()



