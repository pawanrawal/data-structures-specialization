package main

import "fmt"

var swaps [][]int

func shiftDown(i int, a []int) {
	min := i
	leftChild := 2*i + 1
	if leftChild < len(a) && a[leftChild] < a[min] {
		min = leftChild
	}
	rightChild := 2*i + 2
	if rightChild < len(a) && a[rightChild] < a[min] {
		min = rightChild
	}
	if min != i {
		swaps = append(swaps, []int{i, min})
		a[i], a[min] = a[min], a[i]
		shiftDown(min, a)
	}
}

func builder(a []int) {
	for i := len(a)/2 - 1; i >= 0; i-- {
		shiftDown(i, a)
	}
}

func main() {
	a := []int{5, 4, 3, 2, 1}
	builder(a)
	fmt.Println(len(swaps))
	for _, swap := range swaps {
		fmt.Println(swap[0], swap[1])
	}
}
