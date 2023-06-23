package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

var stacks = initalise()

type Action struct {
	count int
	from  int
	to    int
}

func initalise() [][]string {
	return [][]string{
		{"N", "R", "G", "P"},
		{"J", "T", "B", "L", "F", "G", "D", "C"},
		{"M", "S", "V"},
		{"L", "S", "R", "C", "Z", "P"},
		{"P", "S", "L", "V", "C", "W", "D", "Q"},
		{"C", "T", "N", "W", "D", "M", "S"},
		{"H", "D", "G", "W", "P"},
		{"Z", "L", "P", "H", "S", "C", "M", "V"},
		{"R", "P", "F", "L", "W", "G", "Z"},
	}
}

func part1(actions []Action) {
	fmt.Println("Part 1...")
	for _, a := range actions {
		for i := 0; i < a.count; i++ {
			popIdx := len(stacks[a.from-1]) - 1
			popVal := stacks[a.from-1][popIdx]
			stacks[a.from-1] = stacks[a.from-1][:popIdx]
			stacks[a.to-1] = append(stacks[a.to-1], popVal)
		}
	}
	var sb strings.Builder
	for _, s := range stacks {
		sb.WriteString(s[len(s)-1])
	}

	fmt.Printf("After rearrangement completes, the puzzle answer: %v\n", sb.String())
}

func part2(actions []Action) {
	fmt.Println("Part 2...")
	for _, a := range actions {
		var tmp []string
		//fmt.Println("count", a.count)
		for i := 0; i < a.count; i++ {
			popIdx := len(stacks[a.from-1]) - 1
			//fmt.Println("popIdx", popIdx)
			popVal := stacks[a.from-1][popIdx]
			stacks[a.from-1] = stacks[a.from-1][:popIdx]
			tmp = append(tmp, popVal)
		}
		tmpLen := len(tmp)
		for i := 0; i < tmpLen; i++ {
			popIdx := len(tmp) - 1
			popVal := tmp[popIdx]
			tmp = tmp[:popIdx]
			stacks[a.to-1] = append(stacks[a.to-1], popVal)
		}
	}

	var sb strings.Builder
	for _, s := range stacks {
		sb.WriteString(s[len(s)-1])
	}

	fmt.Printf("After rearrangement completes, the puzzle answer: %v\n", sb.String())

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

	var actions []Action
	i := 1
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		if i < 11 {
			i += 1
			continue
		}
		line := strings.Split(scanner.Text(), " ")
		count, _ := strconv.Atoi(line[1])
		frm, _ := strconv.Atoi(line[3])
		to, _ := strconv.Atoi(line[5])
		actions = append(actions, Action{count, frm, to})
		i += 1
	}

	part1(actions)
	stacks = initalise()
	part2(actions)
}
