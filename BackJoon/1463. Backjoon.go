package main

import (
	"fmt"
	"strconv"
)

//var arr [10000001]int64
// 속도는 배열이 더 빠르나, map을 사용하여 풀어보겠습니다.

// key를 int64 타입 value를 int 로 가지는 map 변수를 선언합니다.
var arr map[int64]int = make(map[int64]int)

// 메인 함수 부분
func main() {

	// 키보드 입력을 받을 변수
	var inputData string
	// inputData에 키보드 입력값 대입
	fmt.Scanln(&inputData)
	// i 에 inputData 의 string을 int64 타입으로 변환하여 대입
	i, _ := strconv.ParseInt(inputData, 0, 64)
	// makeOne 호출 및 출력
	fmt.Println(makeOne(i))

}

/*
	점화식
	dp[n] = dp[n-1] + 1
	if n % 3 == 0 { return min(dp[n/3]+1, dp[n])}
	if n % 2 == 0 { return min(dp[n/2]+1, dp[n])}
	return dp[n]
*/

// Top-Down 방식
func makeOne(inData int64) int {

	// inData == 1 이면
	if inData == 1 {
		// arr[inData] 에 0 대입
		arr[inData] = 0
		return 0
	}

	/*
		if inData-1 > 0 && arr[inData-1] != 0 {
			return arr[inData-1]
		}
	*/

	// arr[inData] 값이 존재 한다면 바로 return 하여 메모리 절약
	if arr[inData] != 0 {
		return arr[inData]
	}

	// arr[inData] 점화식 대입
	arr[inData] = makeOne(inData-1) + 1

	// inData 가 3의 약수일 때 계산
	if inData%3 == 0 {
		// temp 임시 변수를 만들어 inData의 3으로 나눈 인덱스에 해당하는 값에 +1 을 저장
		temp := makeOne(int64(inData/3)) + 1

		// min 구현
		if temp < arr[inData] {
			arr[inData] = temp
			return temp
		}

		// arr[inData] 리턴
		return arr[inData]
	}

	// 2로 나누어떨어질 경우
	if inData%2 == 0 {
		temp := makeOne(int64(inData/2)) + 1

		if temp < arr[inData] {
			arr[inData] = temp
			return temp
		}

		return arr[inData]
	}

	// 2와 3으로 나누어 떨어지지 않는 경우 위 점화식에서 구한 값을 return
	return arr[inData]
}
