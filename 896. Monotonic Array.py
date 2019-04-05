class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # A의 길이
        ln = len(A)

        # A의 길이가 1이면 무조건 True
        if ln == 1:
            return True

        # Decrease면 False, increase 면 True
        inDe = None

        # 1~ln-1 까지 반복
        for i in range(1, ln):
            # 처음 inDe 가 비어있는 것은 A[i-1] 과 A[i]는 같다는 것을 뜻함
            if inDe == None and A[i-1] != A[i]:
                # Decrease
                if A[i-1] > A[i]:
                    inDe = True
                # increase
                else:
                    inDe = False
                pass

            # Decrease 일 경우
            if inDe:
                if A[i-1] >= A[i]:
                    pass
                else:
                    return False

            # increase 일 경우
            else:
                if A[i-1] <= A[i]:
                    pass
                else:
                    return False

        # 무사히 통과하였을 경우 True 리턴
        return True


if __name__ == "__main__":
    inputData = []
    sl = Solution().isMonotonic(inputData)
