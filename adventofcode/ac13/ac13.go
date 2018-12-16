package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {

	fmt.Print("hey")
	file, _ := os.Open("input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	b := make([][]byte, 150)
	i := 0
	for scanner.Scan() {
		b[i] = scanner.Bytes()
		fmt.Println(len(b[i]))
		i++
	}

	for i := 0; i < len(b); i++ {
		for j := 0; j < len(b[i]); j++ {
			switch b[i][j] {
			case 60:
				println(i, j, b[i][j])
			case 62:
				println(i, j, b[i][j])
			case 44:
				println(i, j, b[i][j])
			case 118:
				println(i, j, b[i][j])
			}

		}
	}
	fmt.Print(b)

}
