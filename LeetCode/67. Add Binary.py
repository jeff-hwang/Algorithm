class Solution(object):
    def addBinary(self, a, b):
        return self.cvtDemToBin(self.cvtBinToDem(a)+self.cvtBinToDem(b))

    def cvtBinToDem(self, str):
        length = len(str) # str 길이
        li = list(map(int, str))
        res = 0
        for i, v in enumerate(li):
            res += v*(2**(length-i-1))
        return res
    
    def cvtDemToBin(self, num):
        li = []
        if num == 0:
            return "0"
        while num>0:
            li.insert(0, str(num%2))
            num//=2
        res = ""
        for i in li:res+=i
        return res
            
        

if __name__ == "__main__":
    sl = Solution()
    print(sl.addBinary('1010', '1011'))
    

    
            
        