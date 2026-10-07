"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):

    def __init__(self):
       pass

    def maxDepth(self, root):
        if root is None:
            return 0
        
        max_=0
        for child in root.children: 
                max_=max(max_, self.maxDepth(child))
        return 1+ max_
        