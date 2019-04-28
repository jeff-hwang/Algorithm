class Solution(object):
    def removeElement(self, nums, val):
        ln = len(nums) # nums 의 길이
        pivot = 0 # pivot index
        self.removeNums(nums, pivot, val, ln)
        return ln
    
    def removeNums(self, nums, pivot, val, ln):
        while ln > pivot: # pivot이 nums의 길이보다 작을 때
            if nums[pivot]==val: # nums의 pivot 번째 element가 val과 같을 때
                del nums[pivot] # pivot 번째 제거
                ln-=1 # nums의 길이 1 감소
                continue # 반복문 건너뜀
            pivot+=1 # 그렇지 않을 경우 pivot 증가