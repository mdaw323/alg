package main

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

type point struct {
	px, py, vx, vy int
}

func move(points []*point, times int) {
	for _, p := range points {
		p.px = p.px + times*p.vx
		p.py = p.py + times*p.vy
	}
}

func rectangle(points []*point) point {
	s := point{-100000, -100000, 100000, 100000}
	for _, p := range points {
		if p.px > s.px {
			s.px = p.px
		}

		if p.py > s.py {
			s.py = p.py
		}

		if p.vx < s.vx {
			s.vx = p.vx
		}

		if p.vy < s.vy {
			s.vy = p.vy
		}

	}

	return s
}

func drawPoints(p []*point) {
	r := rectangle(p)

}

func main() {

	lines := strings.Split(input, "\n")

	points := make([]*point, len(lines))

	re := regexp.MustCompile("-?\\d+")
	for i, line := range lines {
		f := re.FindAllString(line, 4)
		a, _ := strconv.Atoi(f[0])
		b, _ := strconv.Atoi(f[1])
		c, _ := strconv.Atoi(f[2])
		d, _ := strconv.Atoi(f[3])
		points[i] = &point{a, b, c, d}
	}
	fmt.Println(rectangle(points))
	move(points, 3)
	fmt.Println(rectangle(points))

}

var input = `position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>`
