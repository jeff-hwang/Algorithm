class Solution(object):
    def wordPattern(self, pattern, st):
        
        # st 파라미터를 빈 칸으로 split 해준다.
        strList = st.split(' ')

        # pattern 문자의 길이와 split 한 배열의 길이가 같지 않으면 return False
        if len(pattern) != len(strList):
            return False

        # {pattern id : st[index]}
        # 형태의 dic
        dic = {}

        # pattern 문자를 enumerate 를 사용하여 반복문을 돌린다.
        for i, v in enumerate(pattern):
            # patternDic 의 return 값이 False 이면 return False
            if self.patternDic(dic, v, strList[i]) != True :
                return False
            
        # 키 값을 중복되지 않게 ln에 list 형태로 구성
        ln = list(set(pattern))

        # ln 의 길이 1이상 일 때
        if len(ln) != 1:
            if dic[ln[0]] != dic[ln[1]] :
                return True
            else :
                return False
        # ln의 길이가 1이면 무조건 True
        else:
            return True
            
    def patternDic(self, dic, key, val):
        try:
            # key 값을 가지고 있는지 없는지 체크
            # 없다면 exception 을 처리함
            if dic[key]==True:
                # 실질적으로 이 문장은 실행이 되지 않음
                print('goto Except')
            else:
                # 기존에 있던 키의 value 와 val 이 같지 않으면 False
                # 같으면 True
                if dic[key] == val :
                    return True
                else :
                    return False
        except:
            # 존재하지 않는 키이면 새로운 value를 삽입
            dic[key] = val
            return True

if __name__ == "__main__":
    pattern = "abab"
    st = "dog dog dog dog"
    sl = Solution().wordPattern(pattern, st)
    print(sl)
        
            