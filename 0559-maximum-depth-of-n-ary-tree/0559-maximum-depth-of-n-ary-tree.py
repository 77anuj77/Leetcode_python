"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):

    def __init__(self):
        self.queue = []

    def maxDepth(self, root):
        if root is None:
            return 0

        depth = 0
        self.enqueue(root)
        while len(self.queue) > 0:
            l = len(self.queue)

            for i in range(l):
                node = self.dequeue()
                if node.children:
                    for child in node.children:
                        self.enqueue(child)
            depth += 1
        return depth

    def enqueue(self, root):
        if root is None:
            return

        queue = self.queue
        queue.append(root)

    def dequeue(self):
        v = self.queue[0]
        del self.queue[0]
        return v