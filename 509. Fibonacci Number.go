package main

import "fmt"

func main() {
	fmt.Println(fib(10))
}

// 길이가 31 인 int list 변수
var list [31]int

func fib(N int) int {
	// N이 0 이면 0
	if N == 0 {
		list[0] = 0
		return 0
	} else if N == 1 {
		// N이 1이면 1
		list[1] = 1
		return 1
	}
	//list[N] 이 0 이 아니면 계산했던 것이므로 바로 리턴
	if list[N] != 0 {
		return list[N]
	}
	// 그렇지 않으면 계산되지 않은 것이므로
	// N-1 피보나치 + N-2 피보나치 수열을 더해준다.
	list[N] = fib(N-1) + fib(N-2)
	// 계산한 list[N]을 리턴해준다.
	return list[N]
}
