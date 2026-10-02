class Solution(object):
    def __init__(self):
        self.queue = []

    def levelOrder(self, root):
        if root is None:
            return []
        result = []
        self.enqueue(root)
        while len(self.queue) > 0:
            level = []
            for i in range(len(self.queue)):
                e=self.dequeue()
                level.append(e.val)
                if e.children is not None:
                    for child in e.children:
                        self.enqueue(child)
            result.append(level)
        return result

    def enqueue(self, root):
        return self.queue.append(root)

    def dequeue(self):
        if not self.queue:
            return None

        v=self.queue[0]
        del self.queue[0]
        return v
