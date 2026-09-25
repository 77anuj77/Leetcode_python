class MyStack(object):

    def __init__(self):
        self.q=[]
        self.q1=[]

    def push(self, x):
        while self.q:
            self.q1.append(self.q.pop(0))
        self.q.append(x)
        while self.q1:
            self.q.append(self.q1.pop(0))
        
    def pop(self):
        if not self.q:
            return -1
        value= self.q[0]
        del self.q[0]
        return value

    def top(self):
        if not self.q[0]:
            return -1
        value =self.q[0]
        return value
        

    def empty(self):
        return self.q==[]
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()