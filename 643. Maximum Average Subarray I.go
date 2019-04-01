package main

import "fmt"

func main() {
	var nums = []int{4, 2, 1, 3, 3}
	fmt.Println(findMaxAverage(nums, 2))

}
func findMaxAverage(nums []int, k int) float64 {
	// nums의 길이
	numsLen := len(nums)

	// k가 1이면 nums에서 가장 큰 원소 리턴
	if k == 1 {
		return float64(max(nums))
	}
	// 합의 최대값
	var mx int = sum(nums, 0, k-1)
	// 반복문 중 start부터 end 까지의 값
	var curSum int = mx

	// i를 numsLen-k 인덱스까지 이동시키며 합계를 구한다.
	for i := 1; i <= numsLen-k; i++ {
		// 현재 배열의 합은 이전 원소를 빼고 i+k-1 번째의 더하면 구할 수 있다.
		curSum = curSum - nums[i-1] + nums[i+k-1]

		// 현재 최대 값과 현재 배열의 합을 비교하여
		// 더 큰 값을 최대 값으로 변경
		if mx >= curSum {
			continue
		} else {
			mx = curSum
		}

	}
	// float64로 형변환 하여 평균을 리턴한다.
	return float64(mx) / float64(k)
}

// 배열의 최대값을 구하는 함수
func max(nums []int) int {
	ln := len(nums)
	mx := nums[0]
	if ln == 1 {
		return mx
	}

	for i := 1; i < ln; i++ {
		if mx >= nums[i] {
			continue
		} else {
			mx = nums[i]
		}

	}
	return mx
}

// 배열의 start~end 까지 합을 구하는 함수
func sum(nums []int, start int, end int) int {
	var result int = 0
	for i := start; i <= end; i++ {
		result += nums[i]
	}
	return result
}
