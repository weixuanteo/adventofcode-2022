package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func parseInput(inputFile string) []string {
	var rucksacks []string

	f, err := os.Open(inputFile)
	if err != nil {
		log.Fatal(err)
	}
	defer func(f *os.File) {
		if err := f.Close(); err != nil {
			log.Fatal(err)
		}
	}(f)

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		rucksacks = append(rucksacks, scanner.Text())
	}

	return rucksacks

}

func part1(inputFile string) {
	fmt.Println("Part 1...")

	rucksacks := parseInput(inputFile)
	total := 0

	for _, rs := range rucksacks {
		a := rs[:len(rs)/2]
		b := rs[len(rs)/2:]

		compare := make(map[byte]struct{})
		for i := 0; i < len(b); i++ {
			compare[b[i]] = struct{}{}
		}

		for i := 0; i < len(a); i++ {
			if _, ok := compare[a[i]]; ok {
				if int(a[i]) > 90 {
					total += int(a[i]) - 97 + 1
				} else {
					total += int(a[i]) - 65 + 27
				}
				break
			}
		}

	}

	fmt.Printf("Sum of the priorities of item types: %v\n", total)
}

func part2(inputFile string) {
	fmt.Println("Part 2...")

}

func main() {
	if len(os.Args) < 2 {
		log.Fatal("Check that the name of the input file is provided")
	}
	inputFile := os.Args[1]
	part1(inputFile)
	part2(inputFile)
}
