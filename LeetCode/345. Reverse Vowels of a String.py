class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        sCopy = list(s)
        
        data = ['a','e','i','o','u','A','E','I','O','U']
        left = []
        right = []
        for i in range(length//2):
            if sCopy[i] in data:
                left.insert(0,sCopy[i])
            if sCopy[length-1-i] in data:
                right.append(sCopy[length-1-i])
        if length % 2 != 0:
            if sCopy[length//2] in data:
                left.insert(0,sCopy[length//2])

        res = ""
        vowel = right+left
        for i in sCopy:
            if i in data:
                res += vowel.pop(0)
                continue
            res += i
        return res
            

print(Solution().reverseVowels("leetocode"))
            

            

        
        