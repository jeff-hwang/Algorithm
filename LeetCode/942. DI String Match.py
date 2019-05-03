import numpy as np

class Solution(object):
    '''
    Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

    Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

    If S[i] == "I", then A[i] < A[i+1]
    If S[i] == "D", then A[i] > A[i+1]
    '''
    def diStringMatch(self, S):

        # S의 길이를 구한다.
        ln = len(S)
        
        #li = list(np.arange(ln+1))  <- numpy의 arrange로도 배열 생성가능

        # 0 ~ S.length 까지 일차원 배열로 생성
        li = [i for i in range(ln+1)]
        
        # 결과값 저장
        res = []
        
        # S를 하나하나 분석하여
        # I인지 D 인지 판단
        for i in S:
            # I 이면 현재 가지고 있는 list에서 가장 작은 것을 pop
            if i == "I":
                res.append(self.getI(li))
            # D 이면 list에서 가장 큰 원소를 pop()
            else :
                res.append(self.getD(li))
        
        # S 길이보다 list의 길이가 더 길으므로 남은 마지막
        # 원소 대입
        res.append(li[0])
        
        # 결과값 return
        return res


    def getI(self, li):
        return li.pop(0)

    def getD(self, li):
        return li.pop()

        
if __name__ == "__main__":
    inData = "IDID"
    print(Solution().diStringMatch(inData))
