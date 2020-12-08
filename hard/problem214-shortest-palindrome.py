"""
See https://ashwins-code.github.io/posts/leetcode-214/ for explanation
"""
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if self.palindromic(s):
            return s
        
        prefix = ""
        idx = len(s) - 1
        palindrome = s
        
        while self.palindromic(palindrome) == False:
            prefix += s[idx]
            
            palindrome = prefix + s
            idx -= 1
            
        return palindrome
    
    def palindromic(self, s):
        return s == s[::-1]
