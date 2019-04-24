package main

import "fmt"

func main() {
	a := []int{1, 7, 3, 6, 5, 6}
	fmt.Println(pivotIndex(a))
}

func pivotIndex(nums []int) int {
	// nums의 길이
	var numsLen int = len(nums)
	// nums 원소들의 총 합
	sumNums := 0

	// sumNums를 구하기위한 반복문
	for _, ele := range nums {
		// _ index 사용 x
		// ele = nums의 원소
		sumNums += ele
	}

	// 왼쪽 집합의 합
	var sumLeft int = 0

	// 0부터 numsLen까지 반복
	for i := 0; i < numsLen; i++ {
		//pivot 은 nums[i]
		pivot := nums[i]

		// 만약 왼쪽의 합이 오른쪽의 합과 같지 않으면
		// pivot을 오른쪽으로 한칸 옮긴다.
		if sumLeft != sumNums-sumLeft-pivot {
			sumLeft += pivot
		} else {
			// 같다면 pivot의 index 리턴
			return i
		}
	}
	// 반복문을 무사히 나오면 pivot이 없으므로
	// return -1
	return -1
}
