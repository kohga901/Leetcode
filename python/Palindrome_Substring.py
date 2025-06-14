class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_Palindrome(center):
            palindrome = ""
            if (center == 0):
                return s[0]
            # if center is between two characters
            if (center % 1.0 == 0.5):
                index_left = center - 0.5
                index_right = center + 0.5
            else:
                index_left = center - 1
                index_right = center + 1
            index_left = int(index_left)
            index_right = int(index_right)
            while index_left >= 0 and index_right <= len(s) - 1:
                if (s[index_left] == s[index_right]):
                    palindrome = s[index_left : index_right + 1]
                    index_left -= 1
                    index_right += 1
                else:
                    break
            return palindrome
        if (len(s) <= 1):
            return s
        
        longest_substring = ""
        center = 0
        while center <= (len(s) - 1):
            substring = check_Palindrome(center)
            if (len(substring) > len(longest_substring)):
                longest_substring = substring
            center += 0.5
        return longest_substring

    
import unittest
class Longest_Palindrome_Tests(unittest.TestCase):
    def test_general_case_1(self):
        sol = Solution()
        answer = sol.longestPalindrome("hipop")
        self.assertEqual(answer, "pop")
        answer = sol.longestPalindrome("apple")
        self.assertEqual(answer, "pp")
        answer = sol.longestPalindrome("bb")
        self.assertEqual(answer, "bb")
        answer = sol.longestPalindrome("konichiwalol")
        self.assertEqual(answer, "lol")
    def test_edge_case_1(self):
        sol = Solution()
        answer = sol.longestPalindrome("popopop")
        self.assertEqual(answer, "popopop")
        answer = sol.longestPalindrome("hellothiscontainsapalindromecalled123321andalso12345654321")
        self.assertEqual(answer, "12345654321")
        answer = sol.longestPalindrome("a")
        self.assertEqual(answer, "a")
        answer = sol.longestPalindrome("")
        self.assertEqual(answer, "")
        answer = sol.longestPalindrome("ab")
        self.assertEqual(answer, "a")
        answer = sol.longestPalindrome("bb")
        self.assertEqual(answer, "bb")
        
        
if __name__ == '__main__':
    unittest.main()