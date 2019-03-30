package main

import "fmt"

func main() {
	nums := []int{1, 1, 2}
	removeDuplicates(nums)
}

func removeDuplicates(nums []int) int {
	// nums 의 길이
	var ln int = len(nums)
	// nums 의 index 나타내는 변수
	var i int = 1

	// out of range exception 을 처리할 함수
	func() {
		// 예외가 발생할시 알림을 알리고 그 다음 문장을 실행
		rec := recover()
		fmt.Println(rec)
	}()

	// i가 nums의 길이보다 작을때까지 반복
	for i < ln {
		// nums[i] 와 nums[i-1] 이 같으면 nums에서 빼낸다
		if nums[i-1] != nums[i] {
			i++
		} else {
			// nums[0~i : i+1 ~ 끝까지] nums에 append 한다
			nums = append(nums[:i], nums[i+1:]...)
			// 원소 하나를 집어넣지 않았으므로 전체길이는 1이 감소
			ln--
		}
	}
	// return ln
	return ln
}
