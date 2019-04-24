class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # 배열을 3개의 합으로 나누려면
        # 합은 3X 가 되어야 한다

        # 리스트의 합을 구하고 3으로 나눈다.
        s = sum(A)/3
        # part1 합
        part1 = 0
        # part2 합
        part2 = 0
        # part3 합
        part3 = 0
        for i in A:
            # part1 가 3 분의 1이 아니면 part1 에 i를 더함
            if part1 != s :
                part1 += i
            # part2 가 3 분의 1이 아니면 part1 에 i를 더함
            elif part2 != s :
                part2 += i
            # part3 이 합의 3 분의 1이 아니면 part1 에 i를 더함
            elif part3 != s :
                part3 += i
        
        # 맨 마지막 파티션이 s 가 아닌지만 확인해도 된다.
        # 그 이유는 part1 과 part2 가 이미 완성되어야 part3 가
        # 연산되기 떄문
        if part3 == s:
            return True
        else :
            return False


    
if __name__ == "__main__":
    inData = [0,2,1,-6,6,-7,9,1,2,0,1]
    sl = Solution().canThreePartsEqualSum(inData)
    print(sl)