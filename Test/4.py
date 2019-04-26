class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        try:
            float(s)
            return True

        except:
            # 마이너스 or 플러스 다음 숫자가 아닐 때
            if s[0] == "-" or s[0] == "+" :
                try:
                    int(s[1])
                    pass

                except:
                    return False
                


            # e를 포함할 때
            if 'e' in s:
                cntE = 0
                for i in s:
                    self.countE(i, cntE)
                
                if cntE>1:
                    return False

                
                sList = s.split('e')
                # sList[0]
                                
                try:
                    if len(sList[0].split(" ")) >= 2:
                        return False                    

                    if float(sList[0]):
                        # sList[1] 검사
                        pass

                    else:
                        return False

                    # sList[1] = 10^n
                    try:
                        if int(sList[1]):
                            return True
                        else:
                            return False
                        
                    except:
                        # null 일 때도 False
                        return False

                except:
                    return False
            
            # 마지막으로 e가 아닌 문자를 포함 할 때 위에서 다 정제하였기에 return False
            return False

    def countE(self, ch, cnt):
        if ch == "e":
            cnt+=1
            

        
    

if __name__ == "__main__":
    
    sl = Solution().isNumber("96 e5")
    print(sl)
    

    