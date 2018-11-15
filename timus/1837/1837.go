package main

import (
	"fmt"
	"math"
	"sort"
)

const UNDEFINED = math.MaxInt32

type Vertex struct {
	name     string
	distance int
	edges    []*Vertex
}

func addVertex(m map[string]*Vertex, v string) *Vertex {
	vertex, exists := m[v]
	if !exists {
		vertex = &Vertex{name: v, distance: UNDEFINED}
		m[v] = vertex
	}
	return vertex
}

func addEdge(a *Vertex, b *Vertex) {
	a.edges = append(a.edges, b)
	b.edges = append(b.edges, a)
}

func bfs(s *Vertex) {
	s.distance = 0
	queue := make([]*Vertex, 0)
	queue = append(queue, s)

	for len(queue) > 0 {
		t := queue[0]
		queue = queue[1:]
		for _, e := range t.edges {
			if e.distance == UNDEFINED { // czyli nieodwiedzony
				e.distance = t.distance + 1
				queue = append(queue, e)
			}
		}
	}
}

func main() {
	var n int
	var x, y, z string

	v := make(map[string]*Vertex)

	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		fmt.Scan(&x, &y, &z)
		vX := addVertex(v, x)
		vY := addVertex(v, y)
		vZ := addVertex(v, z)
		addEdge(vX, vY)
		addEdge(vX, vZ)
		addEdge(vY, vZ)
	}
	Isenbaev, exists := v["Isenbaev"]
	if exists {
		bfs(Isenbaev)
	}

	var keys []string
	for k := range v {
		keys = append(keys, k)
	}
	sort.Strings(keys)

	for _, k := range keys {
		if v[k].distance != UNDEFINED {
			fmt.Printf("%s %d\n", k, v[k].distance)
		} else {
			fmt.Printf("%s undefined\n", k)
		}
	}

}
