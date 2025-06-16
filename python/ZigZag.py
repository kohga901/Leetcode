import unittest

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        array = [''] * numRows
        index = 0
        step = 1
        for char in s:
            array[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(array)
                
    
class tests_EVER(unittest.TestCase):
    global sol
    sol = Solution()
    
    def test_basic_row_1(self):
        self.assertEqual("EVER", sol.convert("EVER", 1))
    def test_basic_row_2(self):
        self.assertEqual("EEVR", sol.convert("EVER", 2))
    def test_basic_row_3(self):
        self.assertEqual("EVRE", sol.convert("EVER", 3))
    def test_basic_row_4(self):
        self.assertEqual("EVRE", sol.convert("EVER", 3))
        
class tests_EVERGARDEN(unittest.TestCase):
    global sol
    sol = Solution()
    
    def test_basic_row_1(self):
        self.assertEqual("EVERGARDEN", sol.convert("EVERGARDEN", 1))
    def test_basic_row_2(self):
        self.assertEqual("EEGREVRADN", sol.convert("EVERGARDEN", 2))
    def test_basic_row_3(self):
        self.assertEqual("EGEVRADNER", sol.convert("EVERGARDEN", 3))
    def test_basic_row_4(self):
        self.assertEqual("ERVADEGERN", sol.convert("EVERGARDEN", 4))
    def test_basic_row_5(self):
        self.assertEqual("EEVDNERRAG", sol.convert("EVERGARDEN", 5))
    def test_basic_row_6(self):
        self.assertEqual("EVNEERDGRA", sol.convert("EVERGARDEN", 6))
    def test_basic_row_7(self):
        self.assertEqual("EVERNGEADR", sol.convert("EVERGARDEN", 7))

class tests_VIOLET(unittest.TestCase):
    global sol
    sol = Solution()
    
    def test_basic_row_1(self):
        self.assertEqual("VIOLET", sol.convert("VIOLET", 1))
    def test_basic_row_2(self):
        self.assertEqual("VOEILT", sol.convert("VIOLET", 2))
    def test_basic_row_3(self):
        self.assertEqual("VEILTO", sol.convert("VIOLET", 3))
    def test_basic_row_4(self):
        self.assertEqual("VITOEL", sol.convert("VIOLET", 4))
    def test_basic_row_5(self):
        self.assertEqual("VIOLTE", sol.convert("VIOLET", 5))
    def test_basic_row_6(self):
        self.assertEqual("VIOLET", sol.convert("VIOLET", 6))
    def test_basic_row_7(self):
        self.assertEqual("VIOLET", sol.convert("VIOLET", 7))

class tests_edge_cases(unittest.TestCase):
    global sol
    sol = Solution()
    
    def test_edge_case_1_letter_1_row(self):
        self.assertEqual("E", sol.convert("E", 1))
    def test_edge_case_1_letter_2_row(self):
        self.assertEqual("E", sol.convert("E", 2))
    def test_edge_case_1_letter_3_row(self):
        self.assertEqual("E", sol.convert("E", 3))
    def test_edge_case_1_letter_4_row(self):
        self.assertEqual("E", sol.convert("E", 4))
    def test_edge_case_empty_1_row(self):
        self.assertEqual("", sol.convert("", 1))
    def test_edge_case_empty_2_row(self):
        self.assertEqual("", sol.convert("", 2))
    def test_edge_case_empty_3_row(self):
        self.assertEqual("", sol.convert("", 3))
    def test_edge_case_empty_4_row(self):
        self.assertEqual("", sol.convert("", 4))
    def test_edge_case_2_letters_1_row(self):
        self.assertEqual("AB", sol.convert("AB", 1))
    def test_edge_case_2_letters_2_row(self):
        self.assertEqual("AB", sol.convert("AB", 2))
    def test_edge_case_2_letters_3_row(self):
        self.assertEqual("AB", sol.convert("AB", 3))
    def test_edge_case_2_letters_4_row(self):
        self.assertEqual("AB", sol.convert("AB", 4))
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
