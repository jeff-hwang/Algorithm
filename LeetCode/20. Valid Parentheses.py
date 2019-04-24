class Solution(object):
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # stack 변수
        stack = []
        # 괄호 정보 딕셔너리
        bracket = {'{' : '}',
                   '[' : ']',
                   '(': ')'}

        # string 을 문자 하나하나 반복한다.
        for i in s:
            # i 가 괄호 시작이면 stack 에 추가한다.
            if i == '{' or i =='[' or i=='(':
                stack.append(i)
            # 괄호 끝이면 stack 에서 pop 한다.
            else:

                # 딕셔너리 정보에 없으면 return False 한다.
                try:
                    # data 변수에 stack의 맨 뒤 원소를 pop 한 후 저장
                    data = stack.pop()
                    
                    # i 의 정보와 다르다면 return False
                    if i != bracket[data]:
                        return False
                    # 같으면 반복문을 넘김
                    else :
                        continue
                # 키 정보가 없으면 return False
                except:
                    return False
        
        # stack 의 길이가 0 이면 return True
        if len(stack)==0:
            return True
        # 그렇지 않으면 return False
        else :
            return False
        

if __name__ == "__main__":
    data =  "]"
    sl = Solution()
    print(sl.isValid(data))
    