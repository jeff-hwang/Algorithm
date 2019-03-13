class MyStack(object):
    # stack 변수 선언
    stack = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # class 생성시 전역변수 stack 에 비어있는 List 대입
        self.stack = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        # push method 호출시 stack list 맨 뒤에 원소 추가
        self.stack.append(x)   


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        # pop method 실행시 stack 변수의 맨 뒤에 원소 꺼낸다. 
        return self.stack.pop()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        # top method 호출 시 stack list 의 맨 뒤의 원소 가리킴.
        return self.stack[-1]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        # stack의 길이가 0이면 True, 그렇지 않으면 False Return
        return len(self.stack) == 0
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()