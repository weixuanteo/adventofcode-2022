package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func part1(assignments []string) {
	fmt.Println("Part 1...")

	total := 0
	for _, assignment := range assignments {
		ab := strings.Split(assignment, ",")
		a := strings.Split(ab[0], "-")
		b := strings.Split(ab[1], "-")

		a1, _ := strconv.Atoi(a[0])
		a2, _ := strconv.Atoi(a[1])
		b1, _ := strconv.Atoi(b[0])
		b2, _ := strconv.Atoi(b[1])
		if a1 >= b1 && a2 <= b2 {
			total += 1
		} else if b1 >= a1 && b2 <= a2 {
			total += 1
		}
	}

	fmt.Printf("Total number of pairs where the ranges fully overlap: %v\n", total)

}

func part2(assignments []string) {
	fmt.Println("Part 2...")

	total := 0
	for _, assignment := range assignments {
		ab := strings.Split(assignment, ",")
		a := strings.Split(ab[0], "-")
		b := strings.Split(ab[1], "-")

		a1, _ := strconv.Atoi(a[0])
		a2, _ := strconv.Atoi(a[1])
		b1, _ := strconv.Atoi(b[0])
		b2, _ := strconv.Atoi(b[1])
		if a1 <= b1 && a2 >= b1 {
			total += 1
		} else if b1 <= a1 && b2 >= a1 {
			total += 1
		}
	}

	fmt.Printf("Total number of pairs where the ranges overlap: %v\n", total)
}

func main() {
	if len(os.Args) < 2 {
		log.Fatal("Check that the name of the input file is provided!")
	}
	inputFile := os.Args[1]
	f, err := os.Open(inputFile)
	if err != nil {
		log.Fatal(err)
	}

	defer func(f *os.File) {
		if err := f.Close(); err != nil {
			log.Fatal(err)
		}
	}(f)

	var assignments []string
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		assignments = append(assignments, scanner.Text())
	}
	part1(assignments)
	part2(assignments)
}
