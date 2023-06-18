package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

var shapeScores = map[string]int{
	"X": 1,
	"Y": 2,
	"Z": 3,
}

var scores = map[string]int{
	"A-X": 3,
	"A-Y": 6,
	"A-Z": 0,
	"B-X": 0,
	"B-Y": 3,
	"B-Z": 6,
	"C-X": 6,
	"C-Y": 0,
	"C-Z": 3,
}

var choices = map[string]string{
	"A-X": "Z",
	"A-Y": "X",
	"A-Z": "Y",
	"B-X": "X",
	"B-Y": "Y",
	"B-Z": "Z",
	"C-X": "Y",
	"C-Y": "Z",
	"C-Z": "X",
}

func part1(inputFile string) {
	fmt.Println("Part 1...")

	f, err := os.Open(inputFile)
	if err != nil {
		log.Fatal(err)
	}
	defer func(f *os.File) {
		err := f.Close()
		if err != nil {
			log.Fatal(err)
		}
	}(f)

	scanner := bufio.NewScanner(f)
	total := 0
	for scanner.Scan() {
		line := scanner.Text()
		plays := strings.Split(line, " ")
		total += scores[strings.Join(plays[:], "-")]
		total += shapeScores[plays[1]]
	}

	fmt.Printf("Total score: %v\n", total)
}

func part2(inputFile string) {
	fmt.Println("Part 2...")

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
	total := 0
	for scanner.Scan() {
		line := scanner.Text()
		outcomes := strings.Split(line, " ")
		choice := choices[strings.Join(outcomes[:], "-")]
		total += scores[outcomes[0]+"-"+choice]
		total += shapeScores[choice]
	}

	fmt.Printf("Total score: %v\n", total)
}

func main() {
	if len(os.Args) < 2 {
		log.Fatal("Check that the name of the input file is provided")
	}
	inputFile := os.Args[1]
	part1(inputFile)
	part2(inputFile)
}
