package main

import (
	"fmt"
)

// 문제의 조건에서 정수가 최대 11 까지라고 제시
// 0 ~ 11 까지 1, 2, 3 으로 표시할 수 있는 경우를 저장하는 배열변수
var array [12]int

func main() {
	var len int
	fmt.Scanln(&len)

	// 표현 할 수 있는 숫자가 1, 2, 3 뿐 이므로
	// 점화식 dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

	/* 0~3 까지 표현할 수 있는 방법 수*/
	array[0] = 0
	array[1] = 1
	array[2] = 2
	array[3] = 4

	// 콘솔 입력을 받기 위한 배열
	var num []int = make([]int, len)

	for i := 0; i < len; i++ {
		fmt.Scanln(&num[i])
	}

	// num[0:len] 까지의 표현할 수 있는 경우를 출력한다.
	for i := 0; i < len; i++ {
		fmt.Println(sumOneTwoThree(num[i]))
	}
}

// Top-Down 방식
func sumOneTwoThree(num int) int {

	// 만약 array[num] 에 데이터가 존재한다면 바로 리턴
	if array[num] != 0 {
		return array[num]
	}
	// num 이 3보다 작으면 미리 등록해놓은 array에서 바로 리턴
	if num <= 3 {
		return array[num]
	} else {
		// 그렇지 않다면 점화식을 사용한 top-down 방식으로 구함
		array[num] = sumOneTwoThree(num-1) + sumOneTwoThree(num-2) + sumOneTwoThree(num-3)
		// 계산한 array[num] return
		return array[num]
	}
}
