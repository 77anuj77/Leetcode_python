# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        pass

    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        i=0
        arr=[]
        def inorder(root, arr):
            if root is None:
                return 
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)
        inorder(root, arr)
        minimum= float('inf')
        for i in range(1, len(arr)):
            minimum= min(minimum, abs(arr[i]-arr[i-1]))

        return minimum
    
    def min(self, a, b):
        if a>b:
            return b
        else:
            return a