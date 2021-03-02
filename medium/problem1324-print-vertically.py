class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        max_len = max([len(word) for word in words])
        result = []
        
        for i in range(max_len):
            result.append("")
            for j in words:
                if i < len(j):
                    result[i] += j[i]
                else:
                    result[i] += " "
            result[i] = result[i].rstrip()
        return result
