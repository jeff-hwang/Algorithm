# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
class Sort(object):
    def quickSort(self, arr, start=None, end=None):
        if start==None:
            self.quickSort(arr, 0, len(arr)-1)
        else :
            part = self.partition(arr, start, end)

            if start < part:
                self.quickSort(arr, start, part-1)
            if part < end:
                self.quickSort(arr, part, end)

    def partition(self, arr, start, end):
        pivot = arr[start]

        while start < end:
            while arr[start] < pivot : start+=1
            while arr[end] > pivot : end-=1
            
            if start<=end:
                temp = arr[start]
                arr[start] = arr[end]
                arr[end] = temp
                start+=1
                end-=1

        return start

if __name__ == "__main__":
    st = Sort()
    N = int(input()) # 입력받을 숫자
    nums = [int(input()) for i in range(N)]
    #quickSort(nums)
    st.quickSort(nums)
    for i in nums: print(i)

