class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        rst = False
        stack = []
        for i in bills:
            dic = {'coin' : None, 'cnt' : 0}
            change = i - 5
            # $5 일때
            if change == 0 :
                et = 0
                for j in stack:
                    if j['coin'] == 5:
                        j['cnt'] += 1
                        et = 1
                        break
                if et == 0:
                    dic['coin'] = 5
                    dic['cnt'] += 1
                    stack.append(dic)
                    self.revChange(stack)
            else :
                # 거스름돈 stack 에서 하나씩 꺼낸다
                for j in stack:
                    if j['coin']<=change and j['cnt']!=0:
                        change -= j['coin']
                        j['cnt'] -= 1
                    
                    if change == 0:
                        break

                if change != 0:
                    rst = False
                    return rst

        rst = True
        return rst
    
    def revChange(self, stack):
        stack = sorted(stack, key = lambda k: k['coin'], reverse=True)
        return stack

if __name__ == "__main__":
    bills = [5,5,5,10,20]
    sl = Solution().lemonadeChange(bills)
    print(sl)