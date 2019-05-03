package main

// 메인 함수
func main() {
	println(isPowerOfFour(4))
}

func isPowerOfFour(num int) bool {
	// num > 4 일 때까지 반복
	for num > 4 {
		// 4로 나눈 나머지가 0 이 아닌 경우 return false
		if num%4 != 0 {
			return false
		}
		// num 을 4로 나누어준다.
		num /= 4
	}
	// 반복문이 종료되면 num 이 1 or 4 이면 true 그렇지 않으면 false
	if num == 1 || num == 4 {
		return true
	} else {
		return false
	}
}
