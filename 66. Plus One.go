package main

import "fmt"

func main() {
	a := []int{9, 9, 9}
	fmt.Println(plusOne(a))
}

func plusOne(digits []int) []int {

	// 캐리 변수
	var carry int = 1
	// digits의 길이
	var ln int = len(digits)

	// 결과값 Slice 변수
	var result []int

	// digits를 마지막 인덱스부터 0번까지 반복
	for i := ln - 1; i >= 0; i-- {
		// carry와 digits[i]를 더함
		dig := digits[i] + carry
		// dig를 10으로 나눈 몫을 digits[i] 에 대입
		digits[i] = dig % 10

		// 10으로 나누어 캐리가 발생하면 1 그렇지 않으면 0
		carry = dig / 10
	}

	// 맨마지막 캐리가 없으면 digits를 return
	// 있다면 맨앞에 1을 추가해준다.
	if carry != 0 {
		result = append([]int{1}, digits...)
	} else {
		result = digits
	}

	return result
}
