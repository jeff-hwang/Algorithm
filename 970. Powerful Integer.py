class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """

        # 무조건 x가 y보다 작거나 같게 만듬
        temp = None
        if y < x:
            temp = x
            x = y
            y = temp

        i = 0
        j = 0
        result = []

        if x == 1 and y == 1:
            if bound >= 2:
                return [2]
            else:
                return []
        elif x == 1:
            while y**j + 1 <= bound:
                result.append(y**j + 1)
                j += 1
            return result

        switch = True
        while x**i + y**j <= bound or switch:
            switch = True
            num = self.calcPowerInt(x, i, y, j)
            if num < bound:
                result.append(num)
                #print("x^{} :: y^{}".format(i, j))
                i += 1
                pass
            elif num == bound:
                result.append(num)
                #print("x^{} :: y^{}".format(i, j))
                j += 1
                i = 0
                pass
            else:
                j += 1
                i = 0
                switch = False
        return list(set(result))

    def calcPowerInt(self, x, i, y, j):
        return x**i + y**j


if __name__ == '__main__':
    x = 1
    y = 2
    bount = 100
    sl = Solution().powerfulIntegers(x, y, bount)
    print(sl)
