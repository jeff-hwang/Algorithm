class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        # 문제 설명
        '''
        3차원 배열이 주어진다.
        면 안에 2차원 배열을 r행 * c열 배열로 형태로 재구성하고
        3차원 형태로 return 시켜라.
        원하던 배열로 재구성이 되지 않았으면
        input 배열 그대로 return 시켜라.
        '''

        # 결과 값을 리턴할 비어있는 list
        rst = []
        
        # nums 안에 있는 원소들을 1차원 형태로 재배치하려 이용할 list
        itList = []
        for i in nums:
            for j in i:
                itList.append(j)

        # itList 에 1차원 배열로 정렬됨
        
        # 행을 구성하기 위하여 1 ~ r 까지 반복을 돌림
        for i in range(1, r+1):
            # 행을 구성할 list
            lst = [] 

            # 열을 구성하기 위해 c 번 반복을 돌림
            for j in range(c):
                # 원소가 있으면 0번째 원소를 꺼내 lst에 append
                if len(itList) != 0:
                    a = itList.pop(0)
                    lst.append(a)
            
            # 행을 구성한 원소의 크기가 c와 같지 않으면
            # 원래의 nums를 리턴
            if len(lst) != c:
                return nums
            # rst 에 lst를 append
            rst.append(lst)
        # 재구성한 rst를 return
        return rst

if __name__ == '__main__':

    nums = [
        [1,2],
        [3,4]
    ]
    r = 1
    c = 4
    sl = Solution().matrixReshape(nums, r, c)
    print(sl)