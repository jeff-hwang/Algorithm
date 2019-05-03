class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        # input A 의 길이
        ln = len(A)
        # input B 의 길이
        lnB = len(B)

        # input data가 "" 이면 True
        if ln == lnB == 0:
            return True

        # 길이가 같지 않으면 False
        if ln != lnB:
            return False

        # 0 ~ ln-1 까지 반복
        for i in range(ln):
            # A[i~ln-1] + A[0~i] 가 B 와 같으면 True
            if A[i::]+A[:i] == B:
                return True
        # 반복문을 무사 통과하면 return False
        return False


if __name__ == "__main__":
    A = "abcde"
    B = "cdeab"
    sl = Solution().rotateString(A,B)
    print(sl)
        
        