class Solution(object):
    def lengthOfLastWord(self, s):
        res = 0
        resList = []
        
        btn = False
        for i in s:
            if i.isspace() and btn == True:
                btn = False
                resList.append(res)
                res = 0
                continue
            if i.isalpha():
                btn = True
                res+=1
        if res != 0:
            resList.append(res)
            
        if resList == []:
            return 0
        else :
            return resList[-1]


if __name__ == "__main__":
    s = Solution().lengthOfLastWord("")
    print(s)


    
    