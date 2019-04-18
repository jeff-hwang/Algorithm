class Solution(object):
    def maxCount(self, m, n, ops):
        
        if len(ops)!= 0:
            x = min([i[0] for i in ops])
            y = min([j[1] for j in ops])
            return x*y
        else :
            return m*n