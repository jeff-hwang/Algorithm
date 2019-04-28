package main

import (
	"fmt"
)

var dp [1002]uint64

func main() {
	var data int
	fmt.Scanln(&data)
	/*
		dp[0] = 1
		dp[1] = 3
		dp[2] = 5
		for i := 3; i <= data; i++ {
			dp[i] = dp[i-1] + (2 * dp[i-2])
		}
		res := dp[data-1] % 10007
		fmt.Println(res)
	*/
	fmt.Println(fillTile(data) % 10007)
}

func fillTile(N int) uint64 {
	/*
		2xn 직사각형을 2*1 2*2 타일로 채우는 방법
	*/
	if dp[N-1] != 0 {
		return dp[N-1]
	}
	if N == 1 {
		dp[0] = 1
		return dp[0]
	} else if N == 2 {
		dp[1] = 3
		return dp[1]
	} else if N == 3 {
		dp[2] = 5
		return dp[2]
	}

	dp[N-1] = fillTile(N-2)*2 + fillTile(N-1)

	return dp[N-1]
}
