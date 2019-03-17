'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

class MinStack(object):

    li = None

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.li = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.li.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.li.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.li[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.li)

sl = MinStack()

sl.push(-2)
sl.push(0)
sl.push(-3)
print(sl.getMin())