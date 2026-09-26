class Solution(object):
    def averageOfLevels(self, root):
        self.queue = []
        result = []

        self.enqueue(root)
        while len(self.queue) > 0:
            level_sum = 0
            nums_in_level = len(self.queue)
            for i in range(nums_in_level):
                e = self.dequeue()
                level_sum += e.val
                if e.left is not None:
                    self.enqueue(e.left)
                if e.right is not None:
                    self.enqueue(e.right)
            avg_level = float(level_sum) / nums_in_level
            result.append(avg_level)
        return result

    def enqueue(self, node=None):
        self.queue.append(node)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        val = self.queue[0]
        del self.queue[0]
        return val

