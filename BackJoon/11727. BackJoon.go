package main

import (
	"fmt"
)

func main() {
	var data int
	fmt.Scanln(&data)
	fmt.Println(fillTile(data))
}

var dp [1000]int

func fillTile(N int) int {
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
	} else if N == 4 {
		dp[3] = 11
	}

	if (N+1)%2 == 0 {
		dp[N-1] = fillTile(N-1) + fillTile(N-2) + 3
	} else {
		dp[N-1] = fillTile(N-1) + fillTile(N-2) + 1
	}

	return dp[N-1]
}
