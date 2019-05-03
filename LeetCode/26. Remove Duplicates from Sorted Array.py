class Solution(object):
    def removeDuplicates(self, nums):
        # nms의 길이
        ln = len(nums)
        # index 변수
        i = 1

        # 문제에서 새로운 array 를 생성하지 말고
        # nums를 활용하라고 함
        # try-catch 문으로 처리하여
        # out of range exception 이 발생할 상황을 예방
        try:
            # i가 nums의 길이보다 작을 때까지 반복
            while i < ln:
                # nums i 가 이전 원소와 같다면
                # i 번째 원소를 pop 한다
                if nums[i] == nums[i-1]:
                    nums.pop(i)
                    # pop을 하였으니 nums 의 길이는 1 작아진다
                    ln -= 1
                    # 밑에 부분을 실행하지않고 반복문의 처음으로 간다.
                    continue
                # 이전 원소와 같지 않다면 인덱스를 증가
                i += 1
        except:
            # out of range exception 이 발생시 ln을 리턴
            return ln
        # 무사히 반복문을 빠져나오면 ln 리턴
        return ln
