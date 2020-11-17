"""
Iterate through the nums list and only append the current element to ans if we haven't seen it before (a.k.a it isn't in ans). Otherwise, remove that element from ans.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []

        for i in nums:
            if i not in ans:
                ans.append(i)
            else:
                ans.remove(i)
        
        return ans
