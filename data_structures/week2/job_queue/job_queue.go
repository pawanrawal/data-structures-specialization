package main

import "fmt"

type Node struct {
	idx          int
	nextFreeTime int
}

var workers []Node

func siftUp(idx int) {
	latest := workers[idx]

	// Getting index of parent node.
	parent := idx / 2
	if idx%2 == 0 {
		parent -= 1
	}

	if parent < 0 {
		return
	}

	if latest.nextFreeTime < workers[parent].nextFreeTime ||
		latest.nextFreeTime == workers[parent].nextFreeTime && idx < parent {
		workers[idx], workers[parent] = workers[parent], workers[idx]
		siftUp(parent)
	}
}

func siftDown(idx int) {
	min := idx
	leftChild := 2*idx + 1
	if leftChild < len(workers) && (workers[leftChild].nextFreeTime < workers[idx].nextFreeTime ||
		workers[leftChild].nextFreeTime == workers[idx].nextFreeTime && workers[leftChild].idx < workers[idx].idx) {
		min = leftChild
	}
	rightChild := 2*idx + 2
	if rightChild < len(workers) && (workers[rightChild].nextFreeTime < workers[min].nextFreeTime ||
		workers[rightChild].nextFreeTime == workers[min].nextFreeTime && workers[rightChild].idx < workers[min].idx) {
		min = rightChild
	}
	if min != idx {
		workers[min], workers[idx] = workers[idx], workers[min]
		siftDown(min)
	}
}

func insert(n Node) {
	// adding node to last position.
	workers = append(workers, n)
	siftUp(len(workers) - 1)
}

func getMin() Node {
	n := workers[0]
	workers[0] = workers[len(workers)-1]
	// Reducing size of workers.
	workers = workers[:len(workers)-1]
	siftDown(0)
	return n
}

func main() {
	// No. of threads
	n := 4
	// // No. of jobs
	// m := 20
	// Heap of workers

	jobs := [20]int{1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}

	for i := 0; i < n; i++ {
		insert(Node{idx: i, nextFreeTime: 0})
	}
	// fmt.Println(workers)

	for _, j := range jobs {
		n := getMin()
		// fmt.Println("min", n)
		fmt.Println(n.idx, n.nextFreeTime)
		n.nextFreeTime += j
		insert(n)
		// fmt.Println(workers)
	}
}
