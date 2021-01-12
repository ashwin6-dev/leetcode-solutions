"""
See https://ashwins-code.github.io/posts/leetcode-71/ for explanation
"""

class Solution:
  def simplifyPath(path) :
    stack = []
    folders = path.split("/")

    for folder in folders:
      if folder != "..":
        if folder != "." and folder != "":
          stack.append(folder)
      else:
        if stack != []:
          stack.pop()


    return "/" + "/".join(stack)
