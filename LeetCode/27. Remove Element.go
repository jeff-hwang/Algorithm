package main

func main() {
	var nums = []int{3, 2, 2, 3}
	var val int = 3
	removeElement(nums, val)
}
func removeElement(nums []int, val int) int {
	ln := len(nums)
	var pivot int = 0
	for ln > pivot {
		if nums[pivot] == val {
			nums = append(nums[0:pivot], nums[pivot+1:]...)
			ln--
			continue
		}
		pivot += 1
	}
	return ln
}
