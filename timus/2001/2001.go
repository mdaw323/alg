package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println(time.Now())
	var a1, a2, b1, b2, c1, c2 int
	_, _ = fmt.Scan(&a1, &a2, &b1, &b2, &c1, &c2)
	fmt.Println(a1-c1, a2-b2)
}
