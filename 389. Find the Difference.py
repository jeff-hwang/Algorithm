
class Solution(object):
    def findTheDifference(self, s, t):

        # s의 알파벳을 key, 알파벳 수를 value 로 가지는 딕셔너리
        dicS = {}
        # t의 알파벳을 key, 알파벳 수를 value 로 가지는 딕셔너리
        dicT = {}

        # 시간 복잡도 O(N)
        # 공간 복잡도 O(N)
        for i in s:
            # 문자하나 카운트하여 dicS 에 대입
            self.dicCount(dicS, i)

        # 시간 복잡도 O(M)
        for i in t:
            # 문자하나 카운트하여 dicT 에 대입
            self.dicCount(dicT, i)

        # 시간 복잡도 O(M)
        for key, val in dicT.items():
            try:
                # value가 dicS[key]의 value가 같은 때는 문제 없음
                # 다를 때 그 key를 return 하면 문제 해결
                if val == dicS[key]:
                    pass
                else:
                    return key
            except:
                return key

        # 시간 복잡도 O(N+M)
        # 공간 복잡도 O(N+M)

    def dicCount(self, dic, key):
        try:
            dic[key] += 1
        except:
            dic[key] = 1
