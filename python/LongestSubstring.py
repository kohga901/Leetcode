class Solution(object):
    def lengthOfLongestSubstring(self, s):
        def check_for_dup_char(str):
            if (len(str) == 0):
                return False
            last_char = str[len(str) - 1]
            if last_char in str[0 : len(str) - 1]:
                return True
            return False
        
        if (len(s) == 0):
            return 0
        
        if (len(s) == 1):
            return 1
        
        longest_substring = ""
        first_index = 0
        while first_index < len(s):
            second_index = first_index + 1
            while second_index < len(s) + 1:
                substring = s[first_index : second_index]
                does_contain_dup = check_for_dup_char(substring)
                if (does_contain_dup):
                    break
                if(len(substring) > len(longest_substring)):
                    longest_substring = substring
                second_index += 1
            first_index += 1
            if (len(longest_substring) >= (len(s) - first_index)):
                break

        
        return len(longest_substring)
    
    
sol = Solution()
print(sol.lengthOfLongestSubstring("au"))  
  
            




            