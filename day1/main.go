package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func parseInput(inputFile string) []int64 {
	var elCalories []int64

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
	var calories int64 = 0
	for scanner.Scan() {
		if scanner.Text() == "" {
			elCalories = append(elCalories, calories)
			calories = 0
			continue
		}
		calorie, err := strconv.ParseInt(scanner.Text(), 10, 64)
		if err != nil {
			log.Fatal(err)
		}
		calories += calorie
	}

	return elCalories

}

func part1(inputFile string) {
	fmt.Println("Part 1...")
	elCalories := parseInput(inputFile)
	var top int64 = 0
	for _, c := range elCalories {
		if c > top {
			top = c
		}
	}

	fmt.Printf("The elf carrying the most calories is carrying: %v\n", top)
}

func part2(inputFile string) {
	fmt.Println("Part 2...")
	elCalories := parseInput(inputFile)

	var top1, top2, top3, total int64 = 0, 0, 0, 0

	for _, c := range elCalories {
		if c > top3 {
			top3 = c
		}
		if top3 > top2 {
			top2, top3 = top3, top2
		}
		if top2 > top1 {
			top1, top2 = top2, top1
		}
	}

	total = top1 + top2 + top3
	fmt.Printf("Top 3 elfs are carrying: %v\n", total)
}

func main() {
	if len(os.Args) < 2 {
		log.Fatal("Check that the name of the input file is provided!")
	}
	inputFile := os.Args[1]
	part1(inputFile)
	part2(inputFile)
}
