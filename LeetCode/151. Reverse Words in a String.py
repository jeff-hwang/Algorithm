
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return 할 변수
        answer = ""
        # 빈 공간으로 단어를 구분하여 words 라는 리스트 변수에 대입
        words = s.split(" ")
        # list에서 "" 문자를 제거하여 다시 word 에 대입
        words = [i for i in words if i!=""]
        
        # words 의 길이
        ln = len(words)
        
        # index 마지막부터 0번까지 반복문을 돌림
        for i in range(ln-1, -1, -1):
            # index 값이 마지막이 아니면 words[i] + " " 을
            # 그렇지 않으면 answer에 words[i]를 추가
            if i != 0:
                answer += (words[i]+" ")
            else :
                answer += words[i]
        
        return answer

if __name__ == "__main__":
    s = "  hello world!  "
    sl = Solution().reverseWords(s)
    print(sl)