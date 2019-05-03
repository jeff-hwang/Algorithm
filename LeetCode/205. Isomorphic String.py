class Solution(object):
    

    def isIsomorphic(self, s, t):
        # 문자열 길이
        lnS = len(s)
        lnT = len(t)
        
        # s와 t의 길이가 다르면 return False
        if lnS != lnT:
            return False
        
        # 문자열을 list로 형변환한다.
        liS = list(s)
        liT = list(t)

        # 딕셔너리 변수를 2개 만든다.

        # key = s, value = t
        dic = {}
        # key = t, value = s
        dic1 = {}

        # 0 ~ lnS 까지 반복문을 돌린다.
        for i in range(lnS):
            # key = s, value = t 를 매개변수로 넣어 True 이면 무사 통과
            if self.dicEle(dic, liS[i], liT[i]) == True and \
                self.dicEle(dic1, liT[i], liS[i]): # key = t, value = s 를 매개변수로 넣어 True 이면 무사 통과
                pass
            # 리턴 값이 False 인 경우 False 로 마무리한다.
            else :
                return False
        # 반복문을 무사 통과하면 return True
        return True

    # 원소로 딕셔너리 생성하는 함수
    def dicEle(self, dic, key, val):
        try :
            if dic[key] != val:
                return False
            else :
                return True

        except:
            dic[key] = val
            return True
    
    '''
    def test(self, s, t):
        # 다른사람의 풀이
        print(set(zip(s, t)))
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
    '''

if __name__ == "__main__":
    sl = Solution().isIsomorphic('ab','aa')
    print(sl)
    