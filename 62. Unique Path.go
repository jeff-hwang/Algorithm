package main

import "fmt"

type position struct {
	x, y int
}

// key는 position Struct,  value는 int로 가지는 map 변수
var pathMap map[position]int = make(map[position]int) // make(map[position]int , 선언수)

func main() {
	fmt.Println(uniquePaths(7, 3))
}

func uniquePaths(m int, n int) int {
	// input 값인 m,n 을 position 타입으로
	var pos = position{m, n}

	// pathMapw[m,n] 이 0이 아니라면 값이 이미 존재하므로
	// 그 값을 바로 return
	// 메모리 효율을 위하여
	if pathMap[pos] != 0 {
		return pathMap[pos]
	}
	// m, n이 1이라면 pathMap[1,1] 에 1을 대입하고 return 1
	if m == 1 && n == 1 {
		pathMap[pos] = 1
		return 1
	} else if m == 1 || n == 1 { // m이나 n 중 하나가 1이면
		// pathMap[pos] 에 1을 대입하고 return 1
		pathMap[pos] = 1
		return 1
	}
	// pathMap[pos] 는 pos의 왼쪽 값과 위쪽 값을 더한 결과이므로
	// 더해준다.
	pathMap[pos] = uniquePaths(m-1, n) + uniquePaths(m, n-1)
	// pos 좌표의 값을 return 해줌
	return pathMap[pos]
}
