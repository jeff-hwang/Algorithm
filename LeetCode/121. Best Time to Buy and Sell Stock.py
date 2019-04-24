class Solution(object):
    '''
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ln = len(prices)
        maxVal = None

        for i in range(ln-1):
            for j in range(i+1, ln):
                if prices[i] > prices[j]:
                    continue
                else:
                    if maxVal == None:
                        maxVal = prices[j] - prices[i]
                        continue
                    maxVal = self.getMax(maxVal, prices[j]-prices[i])

        if maxVal == None:
            return 0
        else:
            return maxVal

    def getMax(self, maxVal, val):
        if maxVal > val:
            return maxVal
        else:
            return val

    '''

    def maxProfit(self, prices):
        ln = len(prices)
        if ln == 0:
            return 0
        minPrice = prices[0]
        maxVal = 0
        for p in prices:
            if minPrice > p:
                minPrice = p
            if maxVal < p-minPrice:
                maxVal = p-minPrice

        return maxVal


if __name__ == "__main__":
    inputData = [6, 4, 8, 2, 5]
    sl = Solution().maxProfit(inputData)
    print(sl)
