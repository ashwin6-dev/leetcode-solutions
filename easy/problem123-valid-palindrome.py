"""
ALGORITHM EXPLAINED

Build a string from "s" ignoring case and non alphanumeric characters

Check if this string is the same as it is reversed
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "abcdefghijklmnopqrstuvwxyz1234567890"
        check = ""
        
        for c in s:
            if c.lower() in a:
                check += c.lower()
        
        return check == check[::-1]
