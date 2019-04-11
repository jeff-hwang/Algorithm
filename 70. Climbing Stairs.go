package main

import "fmt"

func main() {
	fmt.Println(climbStairs(3))
}

var climbList [10000]int

func climbStairs(n int) int {
	if n == 1 {
		climbList[0] = 1
		return 1
	} else if n == 2 {
		climbList[1] = 2
		return 2
	}

	if climbList[n] != 0 {
		return climbList[n]
	}

	climbList[n] = climbStairs(n-1) + climbStairs(n-2)
	return climbList[n]
}
