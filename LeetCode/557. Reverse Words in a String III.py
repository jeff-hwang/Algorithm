class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return 변수
        answer = ""
        # 문자를 띄어쓰기로 나누어 list로 변환
        data = s.split(" ")
        # data 의 길이 구함
        lnData = len(data)
        
        # data 를 for 문을 돌림
        for i, v in enumerate(data):
            # 띄어쓰기 원소를 list로 변환
            ls = list(v)
            # reverse
            ls = ls[::-1]

            # ls를 다시 String 형태로 변환
            answer += "".join(ls)
            
            # i가 마지막 index가 아니면 answer에 " "를 더함
            if i != lnData-1:
                answer += " "
            # 종료
            else :
                break
            
        return answer
        


inpt = "Let's take LeetCode contest"

print(Solution().reverseWords(inpt))