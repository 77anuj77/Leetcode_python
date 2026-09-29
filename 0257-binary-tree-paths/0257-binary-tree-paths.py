# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result=[]
        def dfs(root, output):
            if root is None :
                return

            output+=str(root.val)
            if root.left is None and root.right is None:
                result.append(output)
                return
            output+="->"
            dfs(root.left, output)
            dfs(root.right, output)

        dfs(root, "")
        return result