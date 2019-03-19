class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = ""
        words = s.split(" ")
        words = [i for i in words if i!=""]
        ln = len(words)
        
        for i in range(ln-1, -1, -1):
            if i!=0:
                answer += (words[i]+" ")
            else :
                answer += words[i]
        
        return answer

if __name__ == "__main__":
    s = "  hello world!  "
    sl = Solution().reverseWords(s)
    print(sl)