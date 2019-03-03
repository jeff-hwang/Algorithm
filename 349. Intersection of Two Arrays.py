class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # 문제 소개
        '''
        두 개의 배열이 주어지는데, 배열의 교집합을 구하는 funtion을 작성하라
        '''

        # 초기 접근법
        '''
        1. 저느 딕셔너리를 선호하기 때문에 배열 안의 원소를 key 값을 가지고,
          그 원소가 겹친다면 True 인 딕셔너리 변수를 만들어 교집합을 만들 것이라 설계를 한다.

        2. 반복문을 불가피하게 돌려야 되는데 이왕이면 딕셔너리가 적게 만들어지는 쪽을 판단하는 것이 좋겠다는 생각이 든다.
           배열의 길이를 비교 한뒤 적은 쪽을 딕셔너리로 만든다.
        '''
    
        # 첫 번째 파라미터 nums1의 길이
        lenNums1 = len(nums1)
        # 두 번째 파라미터 nums2의 길이
        lenNums2 = len(nums2)
        # 첫번째 파라미터의 배열의 길이가 항상 두 번째 보다 길도록 swap을 해준다.
        # Swap 하기 위하여 temp 변수를 선언
        temp = None

        # nums1 의 길이가 nums2 의 길이보다 크거나 같으면 건너뛰고
        if lenNums1 >= lenNums2:
            pass
        # 그렇지 않으면 Swap 해준다.
        else:
            temp = lenNums1
            lenNums1 = lenNums2
            lenNums2 = temp

        # 딕셔너리 정보를 가질 리스트를 선언한다.
        chkLst = []
        
        # 길이가 짧은 nums2 를 반복문을 돌린다.
        for i in nums2:
            # nums 안의 원소가 중복 되어 여러번 딕셔너리가 append 될 수 있어
            # 그것을 체크해주는 boolean type 변수를 선언해준다.
            chk = False
            # 키값을 nums2의 원소, 교집합인지 체크해주는 것을 가지는 dic 변수를 만든다.
            chkDic = {'num': None, 'chk': False}

            # 리스트 안의 딕셔너리를 반복문을 돌려 딕셔너리의 'num' 키의 value 가 nums2 의 원소일 때
            # 이미 정보를 가지고 있으므로 chk 변수를 True 로 변경하고 중복을 방지한다.
            for j in chkLst:
                if j['num'] == i:
                    chk = True
                    continue
            # 중복을 체크 하였고 chkDic['num'] 에 nums2 의 원소 i 값을 대입한다.
            chkDic['num'] = i
            # 만약 chkLst 에서 처음 나온 것이라면 append 시켜준다.
            if chk== False:
                chkLst.append(chkDic)

        # 이제 chkLst nums2의 원소 정보를 가지고 있는 dic 형태가 담겨져있다
        # 반복문을 돌려 num1 의 원소 와 비교하여 존재한다면 chkLst의 원소의 chk 값을 True 변경하면
        # 교집합을 구할 수있다.

        for i in chkLst:
            for j in nums1:
                if i['num'] == j:
                    i['chk'] = True
        # 비어있는 일차원 리스트를 변수로 선언하여 결과값을 리턴 시킬 것이다.
        rst = []

        # chkLst 의 원소의 chk value가 True 인 것은 이 method의 파라미터의
        # 원소들이 교차 되었다는 것을 뜻하기에 True 인 num value를 
        # rst 에 append 시켜 최종적으로 return 시켜준다.
        for i in chkLst:
            if i['chk'] == True:
                rst.append(i['num'])

        return rst

if __name__ == '__main__':
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    sl = Solution().intersection(nums1, nums2)
    print(sl)
