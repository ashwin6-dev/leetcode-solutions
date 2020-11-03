"""
ALGORITHM EXPLAINED

for every query in queries we do the following

pointer = 0
s = ""
go through each character of query
  is character upper case? 
    if pointer is less than query.length - 1
      is character == query[pointer]?
        pointer += 1 (so that we know which character we need to match next)
      else
        stop going through our query string (since we know that it doesn't match the pattern)
    s += character (since we always need to add capital letters)
  if character not upper case
    is character == query[pointer]?
      pointer += 1 (so that we know which character we need to match next)
      s += character
    else
      stop going through our query string (since we know that it doesn't match the pattern)

add s == pattern to the answer array
"""

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []
        for i in queries:
            pattern_ptr = 0
            s = ""
            for j in i:
                if j.isupper():
                    if pattern_ptr < len(pattern):
                        if j == pattern[pattern_ptr]:
                            pattern_ptr += 1
                        else:
                            break
                    s += j
                elif pattern_ptr < len(pattern):
                    if j == pattern[pattern_ptr]:
                        s += j
                        pattern_ptr += 1

            ans.append(s == pattern)
        
        return ans
