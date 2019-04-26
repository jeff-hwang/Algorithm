class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        
        for i, v in enumerate(A):
            A[i] = self.convertImage(v)

        return A
        
    def convertImage(self, ele):
        
        lst = []

        for i in reversed(ele):
            if i == 1:
                lst.append(0)
            else :
                lst.append(1)

        return lst
                
if __name__ == "__main__":
    A = [[1,1,0],[1,0,1],[0,0,0]]
    sl = Solution().flipAndInvertImage(A)
    print(sl)