class Solution(object):
    def flipAndInvertImage(self, A):
        return [self.convertImage(i) for i in A]
        
    def convertImage(self, ele):
        addList = lambda x: 0 if x == 1 else 1
        return [addList(i) for i in reversed(ele)]